from db import SessionLocal, engine, Base
from models import ScrapedItem, ScrapeRun
from scraper_hn import scrape_hackernews
from scraper_github import scrape_github
from datetime import datetime, UTC

Base.metadata.create_all(bind=engine)


def run_scraper(scrape_func, source_name):
    session = SessionLocal()

    run_log = ScrapeRun(
        source=source_name,
        started_at=datetime.now(UTC),
        status="running",
        items_found=0,
        errors=0
    )

    session.add(run_log)
    session.commit()

    count = 0
    errors = 0

    try:
        data = scrape_func()

        if not data:
            run_log.status = "failed"
            return

        for item in data:
            try:
                exists = session.query(ScrapedItem).filter_by(
                    link=item["link"],
                    source=item["source"]
                ).first()

                if exists:
                    continue

                new_item = ScrapedItem(**item)
                session.add(new_item)
                count += 1

            except Exception as e:
                errors += 1
                print("Item error:", e)

        session.commit()

        run_log.items_found = count
        run_log.errors = errors
        run_log.status = "success"

    except Exception as e:
        run_log.status = "failed"
        print(f"{source_name} failed:", e)

    finally:
        run_log.completed_at = datetime.now(UTC)
        session.commit()
        session.close()

    print(f"{source_name}: {count} items stored, {errors} errors")


if __name__ == "__main__":
    run_scraper(scrape_hackernews, "HackerNews")
    run_scraper(scrape_github, "GitHub")

    print("✅ All scraping completed!")