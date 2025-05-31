# Country ETL (Docker)

An ETL project that extracts country data from the public API `https://restcountries.com/v3.1/all`, transforms it using pandas, and loads it into a PostgreSQL database using Docker Compose.

## Features

- **Extract**: Pulls raw JSON data from the API
- **Transform**: Uses `pandas` to clean and shape the data
- **Load**: Loads structured data into a PostgreSQL table
- All components run inside containers with `Docker Compose`

---

## Tech Stack

- Python 3.10  
- Pandas  
- Requests  
- PostgreSQL 14  
- Docker & Docker Compose  
- `.env` for config  
- Logging to `.log` file

---

## How to Run

### 1. Create a `.env` file

```env
DB_HOST=db
DB_PORT=5432
DB_NAME=country_etl
DB_USER=postgres
DB_PASSWORD=postgres