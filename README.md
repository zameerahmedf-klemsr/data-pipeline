# Data Pipeline Scraper with FastAPI API

## Overview

This project is a complete data pipeline that scrapes real data from websites, stores it in a SQLite database, and exposes it through a FastAPI REST API.

The goal of this project is to understand how scraping, data processing, database storage, and API development work together in a real-world backend system.


## What it does

The pipeline collects data from:

* Hacker News
* GitHub Trending

The collected data is:

* Cleaned and validated
* Stored in a SQLite database
* Served through a REST API


## Data Collected

### Hacker News

* Title
* Points
* Author
* Number of comments
* Link

### GitHub Trending

* Repository name
* Description
* Stars
* Language
* Today's stars


## Tech Stack

* Python
* requests
* BeautifulSoup
* SQLAlchemy
* SQLite
* FastAPI
* Uvicorn
* SlowAPI (Rate Limiting)


## Project Structure

data-pipeline/
│
├── db.py
├── models.py
├── scraper_hn.py
├── scraper_github.py
├── main.py
├── api.py
├── scraper.db
└── README.md


## How it works

1. Scrapers collect data from websites
2. Data is cleaned and validated
3. Duplicate entries are skipped
4. Data is stored in SQLite
5. Each run is logged in a separate table
6. FastAPI serves the stored data via REST endpoints


## Running the Project

### 1. Setup

python -m venv venv
venv\Scripts\activate
pip install requests beautifulsoup4 sqlalchemy fastapi uvicorn slowapi

### 2. Run Scraper

python main.py

### 3. Run API

python -m uvicorn api:app --reload


### API Endpoints

### 1. Home

GET /

Response:

{"message": "API is working"}


## 2. Get All Items

GET /items

Returns all scraped data.


## 3. Search Items

Search items by title.

GET /items?search=AI

Example:

/items?search=python


## 4. Filter Items

Filter items based on source.

GET /items?source=HackerNews

Example:

/items?source=GitHub


## 5. Pagination

Control how many results are returned.

GET /items?page=1&limit=5

Example:

/items?page=2&limit=10

## 6. Combined Usage

You can combine all features together.

/items?search=AI&source=HackerNews&page=1&limit=5


## 7. Analytics

Get statistics about stored data.

GET /stats

Response:

{
  "total_items": 71,
  "hackernews_items": 60,
  "github_items": 11
}

## Features

* Scrapes real-time data
* Stores data in SQLite
* Prevents duplicate entries
* Handles errors safely
* Logs each scraping run
* REST API built using FastAPI
* Search functionality
* Filtering by source
* Pagination support
* Rate limiting to prevent abuse
* Analytics endpoint


## Database Tables

### scraped_items

Stores all scraped data.

### scrape_runs

Stores logs of each scraping run:

* number of items
* errors
* status
* timestamps


## Viewing the Database

### Option 1: SQLite CLI

sqlite3 scraper.db
.tables
SELECT * FROM scraped_items;


### Option 2: DB Browser for SQLite

Open `scraper.db` using DB Browser for a graphical view.


### Option 3: VS Code (SQL Viewer Extension)

* Install SQL Viewer extension
* Open the project
* Connect to `scraper.db`
* Run queries


## Future Improvements

* Add authentication to API
* Deploy API online
* Schedule automated scraping
* Move to PostgreSQL
* Add dashboard/visualization


## Author

Zameer Ahmed F 