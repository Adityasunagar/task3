import requests
from bs4 import BeautifulSoup

def scrape_headlines(url="https://www.bbc.com/news", output_file="headlines.txt"):
    # Step 1: Fetch HTML
    response = requests.get(url)
    html = response.text

    # Step 2: Parse headlines
    soup = BeautifulSoup(html, "html.parser")
    headlines = soup.find_all("h2")

    titles = [h.get_text(strip=True) for h in headlines]

    # Step 3: Save to text file
    with open(output_file, "w", encoding="utf-8") as file:
        for t in titles:
            file.write(t + "\n")

    print(f"Headlines saved to {output_file}")

if __name__ == "__main__":
    scrape_headlines()
