from browser import getChrome, quit, ss

url = 'https://www.google.com/'

browser = getChrome()

browser.get(url)

selectors = browser.find_element_by_name('q')
selectors.send_keys('magal ufuk')
selectors.submit()

ss(browser)

print(browser.title)

quit(browser)