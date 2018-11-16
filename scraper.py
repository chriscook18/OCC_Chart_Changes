from lxml import html
import requests


# Get page
page = requests.get('https://www.officialcharts.com/charts/albums-chart/')
tree = html.fromstring(page.content)

# Grab information
albums = tree.xpath('//div[@class="title"]/a/text()')
artists = tree.xpath('//div[@class="artist"]/a/text()')
lastweeks = tree.xpath('//table//tr//td[position()=2]/span/text()')
positions = tree.xpath('//span[@class="position"]/text()')

#Top 10
print("[B]Top 10[/B]")
print("[LIST=1]")

for i in range(0,10):
    #Remove all caps
    artist = artists[i].title()
    album = albums[i].title()

    #If new we do want all caps
    lastweek = lastweeks[i].upper().strip()

    print("[*] " + artist + " - [I]" + album + "[/I] (" + lastweek + ")")

print("[/LIST]")

#Prepare lists of new and reentries
newentries = []
reentries = []

for i in range(10, len(artists)):
    lastweek = lastweeks[i].upper().strip()

    if lastweek == "NEW":
        newentries.append(i)
        
    elif lastweek == "RE":
        reentries.append(i)

    
#New entries
print("[B]Other new entries[/B]")
print("[LIST]")
for entry in newentries:
    #Remove all caps
    artist = artists[entry].title()
    album = albums[entry].title()

    #New so want position
    position = positions[entry].strip()

    print("[*] " + artist + " - [I]" + album + "[/I] (" + position + ")")

print("[/LIST]")

#Re-entries
print("[B]Re-entries[/B]")
print("[LIST]")
for entry in reentries:
    #Remove all caps
    artist = artists[entry].title()
    album = albums[entry].title()

    #New so want position
    position = positions[entry].strip()

    print("[*] " + artist + " - [I]" + album + "[/I] (" + position + ")")

print("[/LIST]")
