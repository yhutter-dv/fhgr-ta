import requests

data = requests.get('http://www.verfassungen.ch/graubuenden/verf2003.htm')
content = data.text

with open('./verfassung.txt', 'w') as f:
    f.writelines(content)
