from fastapi import FastAPI
from db import SessionLocal
from models import ScrapedItem

# Rate limiting
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from fastapi.requests import Request

# Initialize app
app = FastAPI()

# Setup limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


# Handle rate limit error
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Too many requests. Please try again later."},
    )


# Home route
@app.get("/")
def home():
    return {"message": "API is working"}


# Main endpoint (Search + Filter + Pagination + Rate limit)
@app.get("/items")
@limiter.limit("10/minute")
def get_items(
    request: Request,
    search: str = "",
    source: str = "",
    page: int = 1,
    limit: int = 10
):
    session = SessionLocal()
    query = session.query(ScrapedItem)

    # 🔍 Search
    if search:
        query = query.filter(ScrapedItem.title.contains(search))

    # 🎯 Filter
    if source:
        query = query.filter(ScrapedItem.source == source)

    # 📄 Pagination
    offset = (page - 1) * limit
    items = query.offset(offset).limit(limit).all()

    result = []
    for item in items:
        result.append({
            "id": item.id,
            "title": item.title,
            "link": item.link,
            "source": item.source,
            "scraped_at": str(item.scraped_at)
        })

    session.close()
    return result


# Analytics endpoint
@app.get("/stats")
def get_stats():
    session = SessionLocal()

    total = session.query(ScrapedItem).count()

    # count by source
    hn = session.query(ScrapedItem).filter_by(source="HackerNews").count()
    github = session.query(ScrapedItem).filter_by(source="GitHub").count()

    session.close()

    return {
        "total_items": total,
        "hackernews_items": hn,
        "github_items": github
    }