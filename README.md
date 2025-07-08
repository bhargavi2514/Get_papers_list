# get-papers-list
A Python CLI tool to fetch PubMed research papers based on a search query, identify company-affiliated authors, and export results to CSV.

---

## Features

- Uses PubMed E-utilities API (`esearch`, `efetch`)
- Supports advanced PubMed queries (e.g. `"covid-19 AND vaccine"`)
- Detects non-academic authors (e.g. biotech/pharma affiliations)
- Extracts:
  - PubmedID
  - Title
  - Publication Date
  - Non-academic Author(s)
  - Company Affiliation(s)
  - Corresponding Author Email(s)

---

## Tech Stack

- Python 3.10+
- Poetry (Dependency Management & CLI packaging)
- Libraries: `requests`, `lxml`

---

## Installation

```bash
git clone https://github.com/YOUR-USERNAM
