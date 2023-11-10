from urllib import quote, request


def ddg_query(search_term: str, nr_results: int) -> list[str]:
    search_term = quote(search_term)
    with request.urlopen("https://duckduckgo.com/?q="+search_term+"&format=json&pretty=1") as query:
        body = query.read()
        print(body)


ddg_query("hello there", 1)
