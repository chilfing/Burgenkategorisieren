import json
import webbrowser
import requests
import socket
import time

HOST = input("Enter IP-address or hit 'Enter' for default address: ")
if HOST == "":
    HOST = "152.96.214.132"
PORT = 9991

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(bytes(','.join(coordinate_list), 'utf-8'))
    lengh = s.recv(100)
    print(int(lengh.decode("utf-8")))
    data = s.recv(int(lengh.decode("utf-8")))

print('Received data from Server')
coordinate_list = data.decode("utf-8").split(',')

#display info about list and select start position in list
print('The List has '+str(len(coordinate_list))+' items')
index = input('start: ')
index = int(index)
#go through list

while index < len(coordinate_list):
    x = coordinate_list[index]
    #get info
    print('current index: '+str(index))
    category = x.split('/',1)[0]
    second_part = x.split('/',1)[1]
    coordinates = second_part.split('/',1)[1]
    line_id = second_part.split('/',1)[0]

    #wikidata
    url = 'https://query.wikidata.org/sparql'
    query = 'SELECT * WHERE {SERVICE wikibase:around {?place wdt:P625 ?location .bd:serviceParam wikibase:center "Point('+coordinates+')"^^geo:wktLiteral .bd:serviceParam wikibase:radius "0.1".}}'
    r = requests.get(url, params = {'format': 'json', 'query': query})
    try:
        data = r.json()
    except:
        #TODO To many requests handeling
        #time.sleep(1000)
        index -= 1
        print('error--------------------')
        continue
    amount_of_results = len(data['results']['bindings'])

    #convert to usable format
    xcoord = coordinates.split(' ',1)[0]
    ycoord = coordinates.split(' ',1)[1]
    #reset wikipedia boolean
    wikipedia_data = False

    #get all the wikipedia data in different languages
    languages = ['de','en','fr','it']
    for language in languages:
        fp = 'https://{language}.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=300&gscoord={ycoord}%7C{xcoord}&format=json'.format(xcoord=xcoord,ycoord=ycoord,language=language)
        r = requests.get(fp)
        try:
            wiki_data = r.json()
            for result in wiki_data['query']['geosearch']:
                #display result from wikipedia searches
                print(result)
                wikipedia_data = True
                webbrowser.open_new_tab('https://'+language+'.wikipedia.org/?curid='+ str(result['pageid']))
        except:
            #TODO proper error handeling
            print('wikipedia json')

    
    #display result for wikidata and open google / openstreetmap
    if(amount_of_results > 0 or wikipedia_data):
        #open needed websites
        webbrowser.open_new_tab('https://www.openstreetmap.org/{category}/{line_id}'.format(category=category,line_id=line_id))
        x = coordinates.split(' ',1)[0]
        y = coordinates.split(' ',1)[1]
        webbrowser.open_new_tab('https://www.google.com/maps/?q='+y+' '+x)
        if(amount_of_results > 0):
            for f in data['results']['bindings']:
                webbrowser.open_new_tab(f['place']['value'])
                print(f['place']['value']+'         '+line_id)

        wikipedia_data = False

        #ask what to do next
        controll = input('continue? (yes (y) / no (n) / repeat (r))')
        if(controll == 'y'):
            pass
        elif(controll == 'r'):
            index -= 1
            pass
        else:
            break
    else:
        print('no results found')

    index += 1
