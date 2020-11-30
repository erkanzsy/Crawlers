from browser import getChrome, quit, ss
from bs4 import BeautifulSoup
import csv

def get_html(url):
    browser = getChrome()
    browser.get(url)
    return browser.page_source

def screped_data(card):
    try:
        h2 = card.h2
    except:
        title = ''
        url = ''
    else:
        title = h2.text.strip()
        url = h2.a.get('href')

    try:
        price = card.find('span', {'class': 'a-price-whole'}).text.strip()
        decimal = card.find('span', {'class': 'a-price-fraction'}).text.strip()
    except:
        price = ''
        decimal = ''
    else:
        price = price + decimal

    data = {'title': title, 'price': price, 'url': url}

    return data

def write_csv(data):
    with open('xiaomi.csv', 'a') as f:
        fields = ['title', 'price', 'url']

        writer = csv.DictWriter(f, fieldnames=fields)

        for datum in data:
            writer.writerow(datum)

def main():
    html = get_html("https://www.amazon.com/s?k=xiaomi&rh=n%3A9818047011&ref=nb_sb_noss")
    soup = BeautifulSoup(html, 'lxml')

    cards = soup.find_all('div', {'data-asin': True, 'data-component-type': 's-search-result'})

    all_data = []

    for card in cards:
        data = screped_data(card)
        all_data.append(data)

    write_csv(all_data)

if __name__ == '__main__':
    main()