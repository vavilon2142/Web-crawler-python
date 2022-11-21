from web_crawler import Crawler

#@yourvar = {'User-Agent':''}
url = " "
start_anchor = "/"
urls = Crawler.crawl(url, start_anchor)
print(len(urls), urls)
