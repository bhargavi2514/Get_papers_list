import argparse
import sys

from get_papers_list.fetcher import get_pubmed_ids, fetch_paper_metadata
from get_papers_list.parser import extract_company_affiliations
from get_papers_list.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers and extract company-affiliated authors."
    )
    parser.add_argument(
        "query",
        help="PubMed search query (e.g., 'COVID-19 AND vaccine')"
    )
    parser.add_argument(
        "-f", "--file",
        help="Output CSV filename (if omitted, prints results to console)",
        default=None
    )
    parser.add_argument(
        "-n", "--num",
        type=int,
        help="Maximum number of articles to fetch (default: 50)",
        default=50
    )
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Enable debug logging"
    )

    args = parser.parse_args()

    try:
        if args.debug:
            print(f"[DEBUG] Query: {args.query}")
            print(f"[DEBUG] Max Results: {args.num}")

        # Step 1: Fetch PubMed IDs
        ids = get_pubmed_ids(args.query, args.num)
        if args.debug:
            print(f"[DEBUG] Retrieved {len(ids)} IDs: {ids}")

        # Step 2: Fetch metadata XML
        xml_data = fetch_paper_metadata(ids)
        if args.debug:
            print(f"[DEBUG] Retrieved XML data length: {len(xml_data)}")

        # Step 3: Parse for company-affiliated authors
        results = extract_company_affiliations(xml_data)
        if args.debug:
            print(f"[DEBUG] Parsed {len(results)} articles with non-academic authors")

        # Step 4: Output
        if args.file:
            save_to_csv(results, args.file)
        else:
            if not results:
                print("No company-affiliated authors found.")
            else:
                for entry in results:
                    print(entry)

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
