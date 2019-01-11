import json
from pprint import pprint

with open('tracked_conversation.json') as f:
    data=json.load(f)

events = data['events']

f = open("generated_tree.md", "w+")
f.write("##Generated Story\n")

for i in events:
    if(i['event'] == 'action' or i['event'] == 'user'):
        print(i['event'])
    if(i['event'] == 'user'):
        f.write("* ")
        f.write(i['parse_data']['intent']['name'])
        if(len(i['parse_data']['entities']) == 0):
            f.write("\n")
        else:
            entities = i['parse_data']['entities']
            str = '{'
            for j in entities:
                str = str + '"'+ j['entity'] +'": ' + '"' + j['value'] + '"'
                str = str + ','
            str = str[:-1]
            str = str + '}'
            f.write(str+'\n')

    if(i['event'] == 'action'):
        if(i['name'] != 'action_listen'):
            f.write('    - ' + i['name'] + '\n')
    if(i['event'] == 'slot'):
        f.write('    - slot{' + '"' +i['name'] + '": ' + '"'+ i['value'] +'"}\n')