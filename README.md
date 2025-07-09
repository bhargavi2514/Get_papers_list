# get-papers-list

A Python CLI tool that fetches PubMed articles based on a search query, identifies company-affiliated authors (non-academic), and exports the relevant information to a CSV file.
---
## How the Code is Organized :

get-papers-list/
├── get_papers_list/
│ ├── init.py # Marks the folder as a Python package
│ ├── fetcher.py # Handles PubMed API calls (esearch & efetch)
│ ├── parser.py # Parses XML to extract company-affiliated authors
│ ├── utils.py # Utility functions like CSV writing
│ └── main.py # CLI entry point; connects all modules
├── README.md # Documentation
├── pyproject.toml # Poetry configuration for dependencies & CLI
└── test_output.csv # Sample output file

---

##  How to Install and Run

### Prerequisites

- Python 3.10 or later

---

### Install Dependencies

Open a terminal in the project directory and run:
>>poetry install
>>poetry run get-papers-list "covid-19 AND vaccine" -f output.csv -n 20 -d


## LLM's i have used:
ChatGPT 4 for planning,code modularization,CLI design
