import requests
from bs4 import BeautifulSoup

def clean_text(text):
    return text.strip().replace("\n", "").replace("  ", "")

def scrape_github():
    items = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            "https://github.com/trending",
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(response.text, "html.parser")

        repos = soup.find_all("article", class_="Box-row")

        for repo in repos:
            try:
                # Repo name + link
                title_tag = repo.h2.a
                repo_name = clean_text(title_tag.text)
                link = "https://github.com" + title_tag["href"]

                # Description
                desc_tag = repo.find("p")
                description = clean_text(desc_tag.text) if desc_tag else None

                # Language
                lang_tag = repo.find("span", itemprop="programmingLanguage")
                language = clean_text(lang_tag.text) if lang_tag else None

                # Stars (total)
                stars_tag = repo.find_all("a", href=lambda x: x and x.endswith("/stargazers"))
                stars = clean_text(stars_tag[0].text) if stars_tag else None

                # Today's stars
                today_tag = repo.find("span", class_="d-inline-block float-sm-right")
                today_stars = clean_text(today_tag.text) if today_tag else None

                item = {
                    "title": repo_name,
                    "link": link,
                    "source": "GitHub",
                    "raw_data": {
                        "description": description,
                        "stars": stars,
                        "language": language,
                        "today_stars": today_stars
                    }
                }

                if repo_name and link:
                    items.append(item)

            except Exception as e:
                print("Repo parse error:", e)
                continue

    except Exception as e:
        print("GitHub error:", e)

    return items