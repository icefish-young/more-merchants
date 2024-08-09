import http.client

conn = http.client.HTTPSConnection("pointsdb-bulk-whois-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "a8e9947b27msh3ff9f1fbb044747p12b6dfjsnbf6130c9c652",
    'x-rapidapi-host': "pointsdb-bulk-whois-v1.p.rapidapi.com"
}

conn.request("GET", "/whois?domains=goyard.com%2Cyijingtek.com%2Csino-cool.com%2Cfungsports.com%2Chongyuans.com%2Capollovehicle.com%2Chengwen.com%2Couyechina.com%2Cycjienaier.com%2Cyepmakeuptools.com&format=raw", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))