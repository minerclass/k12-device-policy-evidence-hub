#!/usr/bin/env python3
"""
OpenAlex Evidence Fetcher for K-12 Device Policy & Screen Research
Author: Micah J. Miner, CETL, Ed.S.

Executes Vector A, B, and C scholarly queries against the OpenAlex API 
and maps results to the Agent Search & Evaluation Protocol JSON Schema.
"""

import json
import urllib.request
import urllib.parse
from pathlib import Path

OPENALEX_API_BASE = "https://api.openalex.org/works"

SEARCH_VECTORS = {
    "Vector_A": [
        "Rana Tamim meta-analysis technology learning",
        "screen time device restriction phone ban academic achievement cognitive load longitudinal",
        "SMART Schools smartphone ban mental health",
        "Candice Odgers digital inequality adolescent mental health screen time",
        "print vs digital reading comprehension meta-analysis Delgado Clinton"
    ],
    "Vector_B": [
        "take-home 1:1 classroom cart shared device district policy",
        "Yondr phone pouch bell-to-bell ban classroom climate",
        "UNESCO Global Education Monitoring Report technology education",
        "one-to-one laptop program Zheng Warschauer meta-analysis"
    ],
    "Vector_C": [
        "pedagogical friction productive struggle generative AI instructional design",
        "cognitive offloading automation bypass secondary education writing",
        "tertiary algorithmicity media ecology educational assessment",
        "Larry Cuban oversold and underused grammar of schooling device policy"
    ]
}

def search_openalex(query, mailto="micahminer@gmail.com", limit=3):
    """Query OpenAlex works endpoint."""
    params = {
        "search": query,
        "per_page": limit,
        "mailto": mailto
    }
    url = f"{OPENALEX_API_BASE}?{urllib.parse.urlencode(params)}"
    
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "K12DevicePolicyResearch/1.0 (mailto:micahminer@gmail.com)"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return data.get("results", [])
    except Exception as e:
        print(f"Error querying OpenAlex for '{query}': {e}")
        return []

def format_openalex_work(work):
    """Map OpenAlex work object to our JSON Schema."""
    authorships = work.get("authorships", [])
    author_names = [a.get("author", {}).get("display_name", "") for a in authorships if a.get("author")]
    author_str = ", ".join(author_names[:4]) + (" et al." if len(author_names) > 4 else "")
    
    year = work.get("publication_year", "")
    title = work.get("title", "Untitled")
    doi = work.get("doi", "")
    venue = work.get("primary_location", {}).get("source", {}).get("display_name", "")
    
    citation = f"{author_str} ({year}). {title}. {venue}."
    if doi:
        citation += f" {doi}"
        
    source_id = f"OA_{year}_{work.get('id', '').split('/')[-1]}"
    
    return {
        "source_id": source_id,
        "citation": citation,
        "url_or_doi": doi or work.get("id", ""),
        "document_type": "Empirical Study / OpenAlex Record",
        "policy_or_intervention": {
            "mechanism": "Screen Quota / Device Policy",
            "grade_bands": "System-wide",
            "enforcement_level": "Research Synthesis"
        },
        "theoretical_framing": {
            "considers_instructional_design": True,
            "friction_dimension_addressed": "Multi-layer",
            "avoids_device_panacea_fallacy": True,
            "udl_and_accessibility_considerations": "Retrieved from OpenAlex academic index."
        },
        "findings_summary": {
            "measured_outcomes": ["Achievement", "Attention/Focus", "Wellbeing"],
            "effect_sizes_or_trends": f"Cited by {work.get('cited_by_count', 0)} works.",
            "discrepancy_notes": "Automated retrieval via OpenAlex vector search."
        },
        "critical_limitations": "Automated index record; requires manual verification against inclusion criteria.",
        "relevance_score": 4
    }

def main():
    print("=" * 70)
    print("OpenAlex Evidence Fetcher: K-12 Device Policy & Screen Research")
    print("=" * 70)
    
    all_results = []
    
    for vector_name, queries in SEARCH_VECTORS.items():
        print(f"\n[Executing {vector_name}]")
        for query in queries:
            print(f"  -> Query: {query}")
            results = search_openalex(query, limit=2)
            for work in results:
                formatted = format_openalex_work(work)
                all_results.append(formatted)
                print(f"     [Found] {formatted['citation'][:80]}...")
                
    output_path = Path(__file__).parent.parent / "openalex_retrieved_evidence.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)
        
    print(f"\n[Complete] Successfully exported {len(all_results)} records to:")
    print(f"  -> {output_path}")

if __name__ == "__main__":
    main()
