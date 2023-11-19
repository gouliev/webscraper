import requests
from bs4 import BeautifulSoup
import sys

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else 'No title found'

        # Extract all links
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return title, links
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python scraper.py [URL]")
        return

    url = sys.argv[1]
    title, links = scrape_website(url)
    
    print(f"Title: {title}")
    print("Links found on the page:")
    for link in links:
        print(link)

if __name__ == "__main__":
    main()
