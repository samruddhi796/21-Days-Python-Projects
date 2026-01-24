import requests
from bs4 import BeautifulSoup
import csv

URL = "https://news.ycombinator.com/"


def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.select(".titleline > a")

    headlines = []
    for item in titles:
        title = item.get_text()
        link = item.get("href")
        headlines.append((title, link))

    return headlines


def save_to_csv(headlines, filename="headlines.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        writer.writerows(headlines)


def filter_headlines(headlines, keyword):
    return [h for h in headlines if keyword.lower() in h[0].lower()]


def main():
    print("📰 Hacker News Web Scraper")

    html = fetch_page(URL)
    headlines = parse_headlines(html)

    print(f"✅ {len(headlines)} headlines fetched.")

    keyword = input("Enter keyword to filter (or press Enter to skip): ")
    if keyword:
        headlines = filter_headlines(headlines, keyword)
        print(f"🔍 {len(headlines)} headlines after filtering.")

    save_to_csv(headlines)
    print("💾 Headlines saved to headlines.csv")


main()

