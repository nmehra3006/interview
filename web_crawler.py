from collections import deque
def web_crawler(startUrl):

    queue = deque([])
    visited = set()

    queue.append(startUrl)
    visited.add(startUrl)

    def get_base_domain(url):

        return url.split("http://")[1].split("/")[0]

    base_domain = get_base_domain(startUrl)


    while queue:
        next_url = queue.popleft()

        get_urls = htmlParser.getUrls(next_url)

        for u in get_urls:
            if get_base_domain(u) == base_domain and u not in visited:
                queue.append(u)
                visited.add(u)

    return visited


print web_crawler("http://news.yahoo.com")