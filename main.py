# Import the feedparser library
import feedparser

# List of RSS feed URLs
feed_urls = [
   "http://www.reddit.com/r/python/.rss",
   "https://medium.com/feed/topic/technology",
   "https://codeburst.io/feed/",
   "https://practicaldatascience.co.uk/feed/",
   "https://unbiased-coder.com/feed/"
]

# Iterate over the list of RSS feed URLs
for feed_url in feed_urls:
   # Parse the RSS feed
   feed = feedparser.parse(feed_url)

   # Open a file in append mode
   with open('rss_feeds.txt', 'a') as file:
       # Write the feed title to the file
       file.write(f"Feed Title: {feed.feed.title}\n")
       file.write(f"Feed URL: {feed_url}\n\n")

       # Write the entries to the file
       file.write("Entries:\n")
       for entry in feed.entries:
           file.write(f"Title: {entry.title}\n")
           file.write(f"Link: {entry.link}\n")
           file.write(f"Published: {entry.published}\n\n")
       file.write("\n")
