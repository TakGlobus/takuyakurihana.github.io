from scholarly import scholarly
import yaml

def fetch_scholar_papers(author_name, output_file="_data/publications.yml"):
    """Fetches a list of papers from Google Scholar and saves them in a YAML file."""
    author = next(scholarly.search_author(author_name))
    scholarly.fill(author, sections=["publications"])

    papers = []
    for pub in author["publications"]:
        scholarly.fill(pub)

        # Try to get the direct PDF URL (could be a DOI link or URL to PDF)
        paper_url = pub.get("pub_url", "")  # Direct link to PDF or publisher's page
        
        # If no direct URL, fall back to DOI-based URL
        if not paper_url:
            doi = pub["bib"].get("doi", "")
            if doi:
                # Construct the DOI URL that may lead to the publisher's page or PDF
                paper_url = f'https://doi.org/{doi}'
   
        if  pub['bib'].get('title'):
            papers.append({
                "title": pub["bib"].get("title", "Unknown Title"),
                "authors": pub["bib"].get("author", author),
                "year": pub["bib"].get("pub_year", "N/A"),
                "citation": pub["bib"].get("citation", ""),
                "url" :  paper_url,
                #"url": f'https://scholar.google.com/scholar?cluster={pub.get("citedby_url", "")}'
            })
    
    with open(output_file, "w") as file:
        yaml.dump({"publications": papers}, file, default_flow_style=False)
    
    print(f"Saved {len(papers)} papers to {output_file}")

# Replace with your Google Scholar profile name
fetch_scholar_papers("Takuya Kurihana")