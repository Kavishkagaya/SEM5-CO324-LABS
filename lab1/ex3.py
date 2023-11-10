import json
from urllib import request
from urllib.parse import quote


def ddg_query(search_term: str, nr_results: int) -> list[str]:
    search_term = quote(search_term)
    query_link = f"https://duckduckgo.com/?q={search_term}&format=json"
    with request.urlopen(query_link) as query:
        body = query.read()
        body = json.loads(body)

        if "Results" in body:
            results = body["Results"]
            links = [result["FirstURL"] for result in results]
            links = links[0:nr_results]
            return links
        else:
            return []


result_links = ddg_query("University of Ruhuna", 1)
for link in result_links:
    print(link)
