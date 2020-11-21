from browser import getChrome, quit

browser = getChrome()

browser.get('https://www.transfermarkt.com.tr/')

print(browser.title)

quit(browser)