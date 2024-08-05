import json
import time
from urllib.parse import urlparse
from googlesearch import search

def make_query(category, site):
    return category + " site:" + site

def google_search(query):
    # results = search(query, num_results=50, sleep_interval=5, region="us", lang="zh", advanced=True)
    results = search(query, num_results=200, sleep_interval=10, region="us", advanced=True)
    return results

def save_results_to_file(filename, results):
    with open(filename, 'w') as file:
        file.write(str(results))
        # json.dump(results, f)

def get_host(url):
    parse_url = urlparse(url)
    return parse_url.hostname

def main():
    categories = ["玩具", "服饰鞋包", "家电", "家居", "美妆", "运动", "手工DIY", "china", "made in china"]
    # categories = ["家电", "家居", "美妆", "运动", "手工DIY", "china", "made in china"]
    sites = ["myshopify.com", "myshoplaza.com", "myshopline.com", "onshopbase.com", "wshopon.com", "hotishop.com"]

    unique_urls = set()
    results = set()
    i = 1

    for c in categories:
        for s in sites:
            query = make_query(c, s)
            print(f"current query is: {query}")
            search_results = google_search(query)
            for result in search_results:
                print("the "+ str(i) + " urls")
                i += 1
                hostname = get_host(result.url)
                if hostname not in unique_urls:
                    unique_urls.add(hostname)
                    result.query = query
                    results.add(result)
                else:
                    print(f"{hostname} is in the set")

            results_list = list(results)
            save_results_to_file("./output/merchants-"+c+"-"+s+".txt", results_list)
            results.clear()
            time.sleep(20)

if __name__ == "__main__":
    main()