# Castles and Medieval Towers

## Setup:
```
Install python 3.7 and Java 1.8.0_202
This project might work with other versions too but wasn't tested with any other

change the IP Adress in "burgenServer.py" to your own at "LOCALHOST = 127.0.0.1"
change the IP Adress in "brugenClient.py to your own at "HOST = 127.0.0.1" to set it as the default

run: pip install requests
```

## How to Run:
```
To start run "burgenZaehlen.py". 
```
It creates a list with all the coordinates from these OSM entries:https://meta.wikimedia.org/wiki/Wikimedia_CH/Burgen-Dossier/FehlendeWikidataReferenzen
```
Once it has finished continue by starting "burgenServer.py"
```
It distributes the list to the clients
```
after successfully doing the first to steps you should be able to start "burgenClient.py" 
```
It gets the list on start from the server, let's you pick a starting location in said list and then tries to find any wikidata/wikipedia article at that location (300m radius).
Once it has found something it will open a new: OSM tab with the entry in question, a Google Maps tab at that location as well as all the wikidata/wikipedia articles.

```
after checking every castle on the list "TextWriter.java" can be used to speed up the process of writing "no wikidata entry found" 
```
by copying all the list from: https://meta.wikimedia.org/wiki/Wikimedia_CH/Burgen-Dossier/FehlendeWikidataReferenzen
with the left over entries and pasting them into a file named "burgen.txt" (which should be in the same directory as the .jar) 
the program will then create a new file with the data inside to past into: https://meta.wikimedia.org/wiki/Talk:Wikimedia_CH/Burgen-Dossier/FehlendeWikidataReferenzen
