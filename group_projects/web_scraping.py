import requests
import re
from bs4 import BeautifulSoup

def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    [s.extract() for s in soup(['iframe', 'script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]+', '\n', stripped_text)
    return stripped_text


data = requests.get('http://www.verfassungen.ch/graubuenden/verf2003.htm')
content = data.text
clean_content = strip_html_tags(content)

with open('./verfassung.txt', 'w') as f:
    f.writelines(clean_content)
