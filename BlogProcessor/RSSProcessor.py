import feedparser
import requests
import regex as re
import sqlite3
import sys
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename = 'logger.log', filemode='w')

class RSSProcessor(object):

	"""Parser to take in Substack Feed and write it to DB"""

	def __init__(self, url_name):
		self.url_name = url_name

	def extractContentAndWriteToDB(self):
		logging.info("Processing link: " + self.url_name)
		conn = sqlite3.connect("summary.db")
		cursor = conn.cursor()
		feed = feedparser.parse(self.url_name)
		for entry in feed['entries']:
			title = entry['title']
			link = entry['link']
			published = entry['published']
			numOfContents = 0
			cursor.execute(""" INSERT INTO links (title, link, published_date) VALUES (?, ?, ?) """, (title, link, published, ))
			logging.info("published to links table successfully")
			conn.commit()
			cursor.execute("""SELECT max(id) FROM links""")
			last_id = cursor.fetchone()[0]
			if 'content' in entry:
				for content in entry['content']:
					value = content['value']
					summary = re.sub('[^a-zA-Z0-9 \n\\.]', '', value)
					summary = "summary"
					# summary = summarize("summary")
					cursor.execute(""" INSERT INTO passages (id, value, summary) VALUES (?, ?, ?) """, (last_id, value, summary))
			elif 'summary' in entry:
				# print("star")
				value = entry['summary']
				summary = re.sub('[^a-zA-Z0-9 \n\\.]', '', value)
				summary = "summary"
				# summary = summarize("summary")
				cursor.execute(""" INSERT INTO passages (id, value, summary) VALUES (?, ?, ?) """, (last_id, value, summary))

			logging.info("published to passages table successfully")

def consumeURL(url):
	rssProcessor = RSSProcessor(url)
	rssProcessor.extractContentAndWriteToDB()
