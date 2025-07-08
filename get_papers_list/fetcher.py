import requests

def get_pubmed_ids(query: str, max_results: int = 50) -> list[str]:
    """
    Use PubMed E-utilities to search for paper IDs matching the query.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # raises error if status != 200

    return response.json()["esearchresult"]["idlist"]


def fetch_paper_metadata(pubmed_ids: list[str]) -> str:
    """
    Fetch full paper metadata in XML format using paper IDs.
    """
    if not pubmed_ids:
        return ""

    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.text
