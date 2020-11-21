from browser import getChrome, quit

browser = getChrome()

res = browser.get('https://www.transfermarkt.com.tr/')
print(res.title)
quit(browser)