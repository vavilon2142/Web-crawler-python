from web_crawler import Crawler

url = "https://www.gov.uk"
start_anchor = "/"
urls = Crawler.crawl(url, start_anchor)
print(len(urls), urls)