 # -*- coding: utf-8 -*-
import requests
import json

def get_papers(auid, apikey, count=10):
    resp = requests.get("http://api.elsevier.com/content/search/scopus?query=AU-ID({0})&field=dc:identifier&count={1}".format(str(auid),str(count)),
    headers={'Accept':'application/json',
    'X-ELS-APIKey': apikey})
    results = resp.json()
    return [str(r['dc:identifier']) for r in results['search-results']["entry"]]


def get_scopus_info(SCOPUS_ID, apikey):
    url = ("http://api.elsevier.com/content/abstract/scopus_id/{0}".format(SCOPUS_ID))
    querystring = {"field":"authors,title,publicationName,volume,issueIdentifier,prism:pageRange,coverDate,article-number,doi,citedby-count,prism:aggregationType"}
    headers = {
        'accept': "application/json",
        'x-els-apikey': apikey,
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    r = response.json()
    r = r["abstracts-retrieval-response"]["coredata"]
    doistring = "{\"DOI\": \""
    doistring = doistring+r["prism:doi"]+"\"}"
    paper = None
    try:
        paper =  [r["dc:title"], int(r["prism:coverDate"].split("-")[0]), r["prism:publicationName"], r["prism:pageRange"], doistring, int(r["prism:volume"])]
    except:
        paper = [r["dc:title"], int(r["prism:coverDate"].split("-")[0]), r["prism:publicationName"], "", doistring, int(r["prism:volume"])]
    return paper
    
SCOPUS_IDS =  get_papers(7004212771,"a1dd2a75f71ee960ab1ba8b0b8db6339")

results = []
for SCOPUS_ID in SCOPUS_IDS:
    results.append(get_scopus_info(SCOPUS_ID, "a1dd2a75f71ee960ab1ba8b0b8db6339"))

print results