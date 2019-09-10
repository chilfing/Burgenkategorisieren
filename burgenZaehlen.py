import urllib.request
import re
import webbrowser
import requests
import json

#print("here----------------------------------------------------------------------")
#webbrowser.open_new_tab('https://www.openstreetmap.org/{category}/{line_id}'.format(category=category,line_id=line_id))

#get missing castles website
fp = urllib.request.urlopen("https://meta.wikimedia.org/wiki/Wikimedia_CH/Burgen-Dossier/FehlendeWikidataReferenzen")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
mySplit = mystr.split('\n')
fp.close()

#this List will contain all coordinates
coordinate_list = []

counter = 0

#get missing castles link
for line in mySplit:
    if '<td><a rel="nofollow" class="external text" href="https://www.openstreetmap.org/' in line:
        line = line.replace('<td><a rel="nofollow" class="external text" href="https://www.openstreetmap.org/','').split('"',1)[0]
        line_id = re.findall('\d+', line )[0]
        if 'node' in line:
            category = 'node'
        if 'way' in line:
            category = 'way'
        if 'relation' in line:
            category = 'relation'
            
        #reset
        relation_to_way = False
        way_to_node = False
        

        #go to website and get coordinations of the nodes
        if category == 'relation':
            fp = urllib.request.urlopen('https://www.openstreetmap.org/{category}/{line_id}'.format(category=category,line_id=line_id))
            mybytes = fp.read()

            mystr = mybytes.decode("utf8")
            mySplit = mystr.split('\n')
            fp.close()
            #get first way
            for line in mySplit:
                if 'Way <a title="" rel="nofollow" href="/way/' in line:
                    way = line.replace('  Way <a title="" rel="nofollow" href="/way/','').split('"',1)[0]
                    #print(way)
                    relation_to_way = True
                    break
                

        if category == 'way' or relation_to_way == True:
            if relation_to_way == False:
                fp = urllib.request.urlopen('https://www.openstreetmap.org/way/{line_id}'.format(category=category,line_id=line_id))
            else:
                fp = urllib.request.urlopen('https://www.openstreetmap.org/way/{way}'.format(way=way))
            mybytes = fp.read()

            mystr = mybytes.decode("utf8")
            mySplit = mystr.split('\n')
            fp.close()
            #get first node
            for line in mySplit:
                if '<a class="node" title="" rel="nofollow" href="/node/' in line:
                    node = line.replace('            <a class="node" title="" rel="nofollow" href="/node/','').split('"',1)[0]
                    #print(node)
                    way_to_node = True
                    break
                

        if category == 'node' or way_to_node == True:
            if way_to_node == False:
                fp = urllib.request.urlopen('https://www.openstreetmap.org/node/{line_id}'.format(category=category,line_id=line_id))
            else:
                fp = urllib.request.urlopen('https://www.openstreetmap.org/node/{node}'.format(node=node))
            mybytes = fp.read()

            mystr = mybytes.decode("utf8")
            mySplit = mystr.split('\n')
            fp.close()
            #get first node
            for line in mySplit:
                #print(line)
                if '<a href="/#map=18/' in line:
                    #get coordinates and add to List
                    coordinates = line.replace('  <a href="/#map=18/','').split('"',1)[0]
                    x = coordinates.split('/',1)[0]
                    y = coordinates.split('/',1)[1]
                    coordinate_list.append(category+'/'+line_id+'/'+y+' '+x)
                    counter += 1
                    print(counter)
                    break
#save as json file
with open('coordinates.json','w') as f:
    json.dump(coordinate_list,f)
    
