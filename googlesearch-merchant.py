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

def save_results_to_json(filename, results):
    with open(filename, 'w') as file:
        json.dump(results, file)

def get_host(url):
    parse_url = urlparse(url)
    return parse_url.hostname

def main():
    # categories = ["玩具", "服饰鞋包", "家电", "家居", "美妆", 
    categories = ["运动", "手工DIY", "china", "made in china"]
    sites = ["myshopify.com", "myshoplaza.com", "myshopline.com", "wshopon.com", "hotishop.com","onshopbase.com"]

    unique_urls = set()
    results = set()
    i = 1

    for c in categories:
        for s in sites:
            results_list = []
            query = make_query(c, s)
            print(f"current query is: {query}")
            search_results = google_search(query)
            for result in search_results:
                result_dict = {}
                print("the "+ str(i) + " urls")
                i += 1
                hostname = get_host(result.url)
                if hostname not in unique_urls:
                    unique_urls.add(hostname)
                    result_dict['url'] = result.url
                    result_dict['title'] = result.title
                    result_dict['description'] = result.description
                    result_dict['query'] = query
                    result_dict['hostname'] = hostname
                    results_list.append(result_dict)
                else:
                    print(f"{hostname} is in the set")

            # results_list = list(results)
            save_results_to_json("./output/merchants-"+c+"-"+s+".json", results_list)
            results.clear()
            time.sleep(20)

if __name__ == "__main__":
    main()