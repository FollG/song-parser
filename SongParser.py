import requests
from lxml import etree
import lxml.html
import csv

def parse(url):
    try:
        api = requests.get(url)
    except:
        return

    tree = lxml.html.document_fromstring(api.text)    
    textOriginal = tree.xpath('//*[@id="click_area"]/div//*[class="original"]/text()')
    textTranslate = tree.xpath('//*[@id="click_area"]/div//*[class="traslate"]/text()')

    with open("text.csv", "w", newline='') as csv_file:
        write = csv.writer(csv_file)

        for i in range(len(textOriginal)):
            write.writerow(textOriginal[i])
            write.writerow(textTranslate[i])


def main():
    link = input("gimme link")
    parse(link)


if __name__ == "__main__":
    main()