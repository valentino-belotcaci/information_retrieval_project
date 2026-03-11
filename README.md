# Tattoo Design Search Engine

## Overview

This project implements a full-stack search engine for tattoo design articles collected from multiple websites.  
The system automatically scrapes content, builds a dataset, indexes documents using an information retrieval model, and provides a web interface for searching and exploring results.

The goal of the project is to experiment with information retrieval techniques and build a functional search system that allows users to discover tattoo design ideas through keyword queries.

---

## System Architecture

The project consists of four main components:

```
backend/
frontend/
index_3docs/
tattoo_design/
```

### Web Scraping

The `tattoo_design` directory contains a Scrapy project used to crawl tattoo-related websites and collect:

- article titles
- article links
- textual content

The collected data is stored as a JSON dataset used for indexing.

Technologies used:
- Python
- Scrapy
- XPath / CSS selectors

---

### Indexing and Retrieval

The dataset is indexed using **PyTerrier**, a Python framework for information retrieval.

Steps:
1. Load the scraped dataset
2. Convert it into a Pandas DataFrame
3. Build a searchable index
4. Retrieve documents using the **BM25 ranking model**

Technologies used:
- PyTerrier
- Pandas

The index is stored in:

```
index_3docs/
```

---

### Backend API

The backend is implemented using **FastAPI** and exposes an endpoint for search queries.

Example request:

```
GET /?query=tattoo+dragon
```

The API retrieves relevant documents using BM25 and returns results in JSON format.

Technologies used:
- FastAPI
- PyTerrier
- Pandas

---

### Frontend Interface

The frontend is built using **Vue.js** and provides a simple interface to search and browse results.

Features include:
- search input
- ranked search results
- clickable article links
- simple relevance feedback buttons

Technologies used:
- Vue.js
- Axios
- HTML / CSS
- 
---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/project-name.git
cd project-name
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Project

### Run the scraper

```
cd tattoo_design
scrapy crawl tattoodo
scrapy crawl tattooton
```

### Start the backend

```
cd backend
uvicorn service:app --reload
```

The API will run at:

```
http://localhost:8000
```

### Start the frontend

```
cd frontend
npm install
npm run serve
```

---

## Information Retrieval Model

The search engine uses **BM25**, a probabilistic ranking algorithm that scores documents based on:

- term frequency
- document length
- inverse document frequency

This allows the system to return the most relevant tattoo design articles for a given query.

---

## Learning Objectives

This project explores practical aspects of:

- web scraping
- dataset creation
- information retrieval systems
- backend API development
- full-stack web applications
