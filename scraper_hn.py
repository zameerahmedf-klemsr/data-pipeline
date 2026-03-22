import requests
from bs4 import BeautifulSoup

def scrape_hackernews(pages=2):
    items = []

    for page in range(1, pages + 1):
        url = f"https://news.ycombinator.com/?p={page}"

        try:
            response = requests.get(url, timeout=10)
            
            soup = BeautifulSoup(response.text, "html.parser")

            rows = soup.select(".athing")

            for row in rows:
                try:
                    title_tag = row.select_one(".titleline a")
                    if not title_tag:
                        continue

                    title = title_tag.text
                    link = title_tag["href"]

                    subtext = row.find_next_sibling("tr")

                    score = subtext.select_one(".score") if subtext else None
                    author = subtext.select_one(".hnuser") if subtext else None
                    comments = subtext.select("a")[-1] if subtext else None

                    items.append({
                        "title": title,
                        "link": link,
                        "source": "HackerNews",
                        "raw_data": {
                            "points": score.text if score else None,
                            "author": author.text if author else None,
                            "comments": comments.text if comments else None,
                        }
                    })

                except Exception:
                    continue

        except Exception as e:
            print("HackerNews page error:", e)

    return items