import re
from lxml import etree
from typing import List, Dict

# Heuristic keywords to identify company affiliations
NON_ACADEMIC_KEYWORDS = ["Inc", "Ltd", "LLC", "Corporation", "GmbH", "Technologies", "Biotech", "Pharma"]
ACADEMIC_KEYWORDS = ["University", "Institute", "College", "School", "Hospital", "Center", "Lab"]

def extract_company_affiliations(xml_data: str) -> List[Dict]:
    """
    Parses XML data to extract company-affiliated authors and emails.
    Returns a list of dictionaries with relevant paper details.
    """
    results = []

    try:
        root = etree.fromstring(xml_data.encode("utf-8"))
    except Exception as e:
        print(f"❌ Error parsing XML: {e}")
        return []

    for article in root.xpath("//PubmedArticle"):
        try:
            pmid = article.xpath(".//PMID/text()")[0]
            title = "".join(article.xpath(".//ArticleTitle//text()"))
            pub_date = "".join(article.xpath(".//PubDate//text()"))

            authors_info = article.xpath(".//AuthorList/Author")
            non_acad_authors = []
            affiliations = []
            emails = []

            for author in authors_info:
                name_parts = author.xpath("./ForeName/text()") + author.xpath("./LastName/text()")
                name = " ".join(name_parts).strip()

                aff_texts = author.xpath(".//AffiliationInfo/Affiliation/text()")

                for aff in aff_texts:
                    # Check for company affiliation
                    is_non_academic = any(k in aff for k in NON_ACADEMIC_KEYWORDS)
                    is_academic = any(k in aff for k in ACADEMIC_KEYWORDS)

                    if is_non_academic and not is_academic:
                        non_acad_authors.append(name)
                        affiliations.append(aff)

                        # Try to extract email using regex
                        email_match = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}", aff)
                        if email_match:
                            emails.extend(email_match)

            if non_acad_authors:
                results.append({
                    "PubmedID": pmid,
                    "Title": title,
                    "Publication Date": pub_date,
                    "Non-academic Author(s)": "; ".join(set(non_acad_authors)),
                    "Company Affiliation(s)": "; ".join(set(affiliations)),
                    "Corresponding Author Email": "; ".join(set(emails))
                })

        except Exception as e:
            continue  # skip bad articles

    return results
