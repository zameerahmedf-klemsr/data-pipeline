from sqlalchemy import Column, Integer, String, DateTime, JSON, UniqueConstraint
from datetime import datetime, UTC
from db import Base

class ScrapedItem(Base):
    __tablename__ = "scraped_items"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)
    source = Column(String)
    raw_data = Column(JSON)
    scraped_at = Column(DateTime, default=lambda: datetime.now(UTC))

    __table_args__ = (
        UniqueConstraint("link", "source", name="unique_item"),
    )


class ScrapeRun(Base):
    __tablename__ = "scrape_runs"

    id = Column(Integer, primary_key=True)
    source = Column(String)
    items_found = Column(Integer)
    errors = Column(Integer)
    status = Column(String)

    started_at = Column(DateTime)
    completed_at = Column(DateTime)