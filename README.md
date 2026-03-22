# Data Pipeline Scraper

## Overview

This project is a simple data pipeline that scrapes real data from websites and stores it in a SQLite database.

I built this to understand how scraping, data cleaning, and database storage work together in a real workflow.

---

## What it does

The pipeline collects data from:

* Hacker News
* GitHub Trending

For each source, it scrapes useful fields and stores them in a database while avoiding duplicates.

---

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

---

## Tech Used

* Python
* requests
* BeautifulSoup
* SQLAlchemy
* SQLite

---

## Project Structure

data-pipeline/
│
├── db.py
├── models.py
├── scraper_hn.py
├── scraper_github.py
├── main.py
├── scraper.db
└── README.md


## How it works

1. Scrapers collect data from websites
2. Data is cleaned and validated
3. Duplicate entries are skipped
4. Data is stored in SQLite
5. Each run is logged in a separate table

---

## Running the project

### Setup

python -m venv venv
venv\Scripts\activate
pip install requests beautifulsoup4 sqlalchemy

### Run

python main.py

---

## Example Output

HackerNews: 60 items stored
GitHub: 11 items stored
All scraping completed!

---

## Database Tables

### scraped_items

Stores all scraped data.

### scrape_runs

Stores logs of each run:

* number of items
* errors
* status
* timestamps

---

## Viewing the Database

### Option 1: SQLite CLI

sqlite3 scraper.db
.tables
SELECT * FROM scraped_items;

---

### Option 2: DB Browser for SQLite

Open `scraper.db` using DB Browser and view tables in a UI.

---

### Option 3: VS Code (SQL Viewer Extension)

* Install SQL Viewer extension
* Open the project in VS Code
* Connect to `scraper.db`
* View tables and run queries

---

## Features

* Scrapes real data
* Stores data in SQLite
* Prevents duplicate entries
* Handles errors without crashing
* Logs every run

---

## Notes

* No scraping frameworks were used
* Everything is built using basic tools (requests + BeautifulSoup)
* The pipeline is simple but can be extended further

---

## Future Improvements

* Build an API using FastAPI
* Add search and filtering
* Schedule automatic scraping
* Move to PostgreSQL

---

## Author

Zameer Ahmed F 
