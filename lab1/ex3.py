import json
from urllib import request
from urllib.parse import quote


def ddg_query(search_term: str, nr_results: int) -> list[str]:
    search_term = quote(search_term)
    query_link = f"https://duckduckgo.com/?q={search_term}&format=json"
    try:
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
    except Exception as e:
        print(e)
        return []


def last_modified(url: str) -> str:
    try:
        req = request.Request(url, method="HEAD")
        with request.urlopen(req) as query:
            return query.headers["Last-Modified"]
    except Exception as e:
        print(e)
        return "None"


result_links = ddg_query("w3schools", 2)
for link in result_links:
    print(link, last_modified(link))
