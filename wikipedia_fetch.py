import requests
import json
from bs4 import BeautifulSoup

parameters = {'action':'query', 'prop':'extracts', 'format': 'json', 'titles':'Dog'}
url = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)

text = json.loads(url.text)
exactly = text['query']['pages']['4269567']['extract']
soup = BeautifulSoup(exactly, 'html5lib')

all_spans = soup.find_all('span')
readable_text = str(soup.get_text())
#print(type(readable_text))
#with open('readable_dog.txt', 'w', encoding=('utf8')) as readable_dog:
#    readable_dog.write(readable_text)

#and I got this:
#The dog (Canis familiaris when considered a distinct species or Canis lupus 
#familiaris when considered a subspecies of the wolf) is a domesticated carnivore 
#of the family Canidae. It is part of the wolf-like canids, and is the most widely 
#abundant terrestrial carnivore. The dog and the extant gray wolf are sister taxa as 
#modern wolves are not closely related to the wolves that were first domesticated, 
#which implies that the direct ancestor of the dog is extinct. 
#The dog was the first species to be domesticated, and has been selectively bred over 
#millennia for various behaviors, sensory capabilities, and physical attributes.
#Their long association with humans has led dogs to be uniquely attuned to human behavior, 
#and they can thrive on a starch-rich diet that would be inadequate for other canids. 
#Dogs vary widely in shape, size, and colors. They perform many roles for humans, 
#such as hunting, herding, pulling loads, protection, assisting police and military, 
#companionship, and, more recently, aiding disabled people, and therapeutic roles. 
#This influence on human society has given them the sobriquet of "man's best friend."
