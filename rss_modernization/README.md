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
Pipeline Orchestration (Prefect)
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

## Production Pipeline Characteristics

This project simulates production analytics engineering practices including:

- Modular transformation modeling using dbt
- Incremental data processing for efficiency
- Automated data quality validation
- Pipeline orchestration readiness and operational scalability
- Pipeline observability and operational monitoring readiness for production reliability

The pipeline is designed to support continuous feed ingestion patterns typical in modern data platforms.

---

## Technologies Used

DuckDB was used to simulate a lightweight analytical warehouse suitable for local development and portfolio demonstration.

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
Raw data is materialized using dbt seed datasets and source views to maintain lineage and reproducibility.

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
- Staging models enforce schema standardization and prepare data for dimensional modeling patterns

```bash
models/staging/stg_rss_articles.sql
```

#### Marts Layer
Business analytics tables including:
- Date dimension table
- Article fact table

```bash
models/marts/dim_date.sql
models/marts/fact_articles.sql
```

---

## Technical Implementation Details

### Ingestion Layer
Python-based RSS feed ingestion:
- Uses feedparser for RSS parsing
- Converts semi-structured data into structured datasets
- Outputs normalized CSV datasets

### Transformation Layer
dbt is used to implement:
- Staging transformations
- Business logic modeling
- Data quality testing

### Analytics Layer
Analytical marts provide:
- Dimensional modeling structures
- Fact-based analytics metrics

---

## Pipeline Governance & Reliability

The pipeline incorporates reliability engineering concepts including:

- Schema enforcement through dbt modeling
- Data lineage tracking via dbt sources and refs
- Incremental load protection mechanisms
- Automated data quality testing frameworks
- Reproducible analytics modeling using dbt version-controlled transformations

---

## Incremental Modeling Strategy

The staging models use incremental logic to optimize pipeline performance:

- Only new records are processed
- Historical data is preserved
- Query performance is improved for repeated pipeline runs

Incremental logic is based on tracking publication timestamps and comparing against previously processed records.

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

## Real-World Relevance

This project simulates modern data platform development patterns including:
- Analytics engineering workflows
- Modular pipeline design
- Data quality governance
- Incremental transformation strategies

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

Designed and implemented as a modern analytics engineering portfolio demonstration project.