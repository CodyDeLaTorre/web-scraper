import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Spider-Man'


def helper(r):
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find_all(title="Wikipedia:Citation needed")


def polish(text):
    polished = re.sub(r"\[(.*?)\]", "", text)
    return polished

def get_citations_needed_count(url):
  needs = helper(requests.get(url))
  print("Number of citations needed: ", len(needs))
  

def get_citations_needed_report(url):
  try:
    needs = helper(requests.get(url))
    for need in needs:
      text = polish(need.find_parent("p").text)
      print(text)
  except:
      print("No citations needed")


if __name__ == '__main__':
     get_citations_needed_count(url)
     get_citations_needed_report(url)
