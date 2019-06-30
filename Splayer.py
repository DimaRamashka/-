import requests
import json
import socket

author_name = str(input())
page_size = 10
resp = requests.get("https://frs.noosphere.ru/solr/search/select?wt=json&fl=search.resourceid&fl=location.coll&fl=handle&dc.date&fl=dc.title&fl=dc.source&fl=dc.creator&fl=dc.rights&fl=dc.type&sort=bi_sort_3_sort+desc&rows=16&start=0&q=search.resourcetype%3A2&fq=type%3A%22%D0%BC%D1%83%D0%B7%D1%8B%D0%BA%D0%B0%22&omitHeader=true")
# json = json.loads()
j = json.loads(resp.text)
aou = [] ##array of urls
aon = [] #names
aoid = [] #file id
# print(j["response"])
for i in range(page_size):
	aon.append(j["response"]["docs"][i]['dc.title'])
	# aou.append(j["response"]["docs"][i]['dc.title'])
	aoid.append(j["response"]["docs"][i]['handle'])
	print(aon[i][0])

choose = str(input())


for i in range(page_size):
	if choose == i:
		pass
	pass

sock = socket.socket()
music = requests.get("https://frs.noosphere.ru/xmlui/bitstream/handle/20.500.11925/1270235/20.500.11925/1270235")
# print(socket.gethostbyname('https://frs.noosphere.ru/xmlui/bitstream/handle/20.500.11925/1270235/20.500.11925/1270235'))
# socket.connect()
print(type(music))

