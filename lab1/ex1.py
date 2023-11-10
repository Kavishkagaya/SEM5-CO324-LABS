from urllib import request

try:
    # response = request.urlopen("https://eng.pdn.ac.lk/unknown")
    response = request.urlopen(
        "https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D")

    body = response.read()

    # print(response.headers, response.status)
    # print(type(body))
    # print(body)
    print(body.decode("utf-8"))

    response.close()

except Exception as e:
    print(e)
