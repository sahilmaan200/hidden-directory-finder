#created by Sahil maan
# # # finding active dir

import requests
def request(url):
    try:
        return requests.get("https://" + url)
        except requests.exceptions.ConnectionError:
            pass
target_url ="google.com"
with open("dir_location","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+]discovered dir -->  " + test_url)
