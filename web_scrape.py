#code to return snippets for each keyword as found in keywords, from google search

import requests
from keywords import keywords_all

def search_google(query, api_key, cx):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cx,
        'q': query
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    if 'items' in data:
        top_result = data['items'][0]

        top_url = top_result['link']
        snippet = top_result['snippet']

        return top_url, snippet
    else:
        return None, None

# Example usage
for i in keywords_all:
    
    api_key = 'AIzaSyBPzMQhIAOQzaK7GfrZBUI8BE8sYqkgVMI'
    cx = 'b2793d053345043ec'

    top_url, snippet = search_google(i, api_key, cx)
    if top_url and snippet:
        print (i)
        #print("Top URL:", top_url)
        print(snippet[:700])  # Print the first 200 characters of the snippet
    else:
        print("No results found.")
