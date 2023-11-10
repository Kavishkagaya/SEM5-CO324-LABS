from urllib import request

# with request.urlopen("https://www.duckduckgo.com/?q=Rocco%27s+basilisk") as query:
with request.urlopen("https://duckduckgo.com/?va=q&t=hb&q=%E0%B6%9A%E0%B7%80%E0%B7%92%E0%B7%81%E0%B7%8A%E0%B6%9A&ia=web") as query:

    headers = query.headers.items()

    body = query.read()

    for h in headers:
        print(h)
    print(body)
