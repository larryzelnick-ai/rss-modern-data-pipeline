# RSS Modern Data Pipeline

## Overview

The RSS Modern Data Pipeline project demonstrates a production-style analytics engineering workflow using Python ingestion, dbt transformation modeling, and DuckDB as a local analytics warehouse.

This project demonstrates real-world data engineering concepts including:

- Data extraction from RSS feeds
- Structured ingestion pipelines
- Analytics engineering transformation modeling
- Data quality validation
- Incremental data processing

---

## Business Value

Modern organizations need reliable pipelines to convert semi-structured feed content into structured analytics datasets.

This project demonstrates how RSS-style streaming content can be converted into business-ready analytics tables for reporting and downstream analysis.

---

## Architecture
```
RSS Feed Sources  
        │
        ▼
Python Ingestion Layer  
        │
        ▼
CSV Raw Storage Layer  
        │
        ▼
DuckDB Analytics Warehouse  
        │
        ▼
dbt Transformation Models  
        │
        ▼
Business Analytics Marts
```

---

## Technologies Used

### Programming & Scripting
- Python 3.x

### Data Engineering
- dbt (Data Build Tool)
- SQL
- DuckDB

### Development
- Git
- VS Code

---

## Pipeline Design

### 1. Extraction Layer
RSS feeds are extracted using Python and stored as structured CSV data.

Example extracted fields:
- Article title
- Publication date
- Article link
- Summary content
- Source feed identifier

The ingestion script is located in:

```bash
python_scripts/ingest_rss.py
```

---

### 2. Raw Data Layer
Raw RSS data is stored as seed data or raw warehouse views.

```bash
models/seeds/rss_raw_seed.csv
models/sources/rss_sources.yml
```

---

### 3. Transformation Layer
dbt models transform raw data into analytics-ready datasets.

Models include:

#### Staging Layer
- Data cleaning and type normalization
- Incremental loading support

```bash
models/staging/stg_rss_articles.sql
```

#### Marts Layer
Business analytics tables including:
- Date dimension table
- Article fact table

```
models/marts/dim_date.sql
models/marts/fact_articles.sql
```

---

## Data Quality Testing

The project implements dbt tests to validate:
- Non-null constraints
- Unique keys
- Data integrity rules

Examples:
- Article links must be unique
- Required fields cannot be null

Tests are defined in:

```bash
models/staging/stg_rss_articles.yml
```
---

### Incremental Processing

Staging models use incremental logic to prevent reprocessing historical data.

Example pattern:

```sql
{% if is_incremental() %}
where published_date > (
    select coalesce(max(published_date), '1900-01-01')
    from {{ this }}
)
{% endif %}
```

---

## How To Run This Project

### Install Dependencies
```bash
pip install feedparser pandas dbt-duckdb prefect
```

### Run Ingestion Pipeline
```bash
python python_scripts/ingest_rss.py
```

### Run dbt Transformations

From the project root:

```bash
cd rss_modernization
dbt run
dbt test
```

---

## Project Learning Outcomes

This project demonstrates competency in:

- Modern analytics engineering workflows
- Pipeline architecture design
- Data transformation modeling
- Data quality governance
- Version-controlled data development

---

## Future Enhancements

Potential improvements include:

- Cloud warehouse migration
- Real-time streaming ingestion
- Workflow orchestration automation
- Advanced analytics metrics
- Dashboard visualization integration

---

### Project Structure

```
dbt-modernization/
│
├ python_scripts/
├ rss_modernization/
│   ├ models/
│   │   ├ staging/
│   │   ├ marts/
│   │   └ sources/
│   ├ orchestration/
│   ├ seeds/
│   └ tests/
│
├ logs/
├ venv/
└ README.md
```
---

## Author

Designed and implemented as a modern analytics engineering portfolio project.