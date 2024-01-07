import requests
def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url = 'https://www.dawn.com/'
#r = requests.get(url)
fetchAndSaveToFile(url,"new_dawn.html")
print(r.text)