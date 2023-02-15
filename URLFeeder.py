import BlogProcessor.RSSProcessor as RSSProcessor

class URLFeeder(object):

	"""URL Feeder"""

	def __init__(self, URL):
		rssprocessor = RSSProcessor.consumeURL(URL)

if __name__ == "__main__":
	URLs = ["https://theoryclass.wordpress.com/feed", "https://arnoldkling.substack.com/feed", "https://feeds.feedburner.com/CalculatedRisk", "https://blogs.wellesley.edu/ravisblog/feed/", "https://www.moneyandbanking.com/commentary?format=rss", "https://www.coordinationproblem.org/atom.xml", "https://www.nakedcapitalism.com/feed", "https://www.samefacts.com/feed/", "https://rogerfarmerblog.blogspot.com/feeds/posts/default?alt=rss", "http://www.irisheconomy.ie/index.php/feed/"]
	for url in URLs:
		ex = URLFeeder(url)