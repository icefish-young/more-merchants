import csv
from urllib.parse import urlparse
from googlesearch import search

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines

def append_csv(filename, list):
    with open(output_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list)

def google_search(query):
    # results = search(query, num_results=50, sleep_interval=5, region="us", lang="zh", advanced=True)
    results = search(query, num_results=10, sleep_interval=10, advanced=True)
    return results

def get_host(url):
    parse_url = urlparse(url)
    return parse_url.hostname

def main():
    input_filename = "./input/suppliers.txt"
    output_filename = "./output/suppliers.csv"
    block_list = ["www.made-in-china.com","www.topchinasupplier.com","www.findsupply.com","www.importgenius.cn","www.exporthub.com","www.globalsources.com"]
    query_list = read_file(input_filename)

    i = 1
    for query in query_list: 
        result_dict = []
        print(f"search the {i} supplier {query}")
        results = google_search(query)
        for result in results:
            # if not in block_list, save
            hostname = get_host(result.url)
            print(f"hostname is: {hostname}")
            if hostname not in block_list:
                result_dict.append(result.url)
                result_dict.append(query)
                result_dict.append(result.title)
                result_dict.append(result.description)

                append_csv(output_filename, result_dict)
                break
        # persist info

if __name__ == "__main__":
    main()







