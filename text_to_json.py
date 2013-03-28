import simplejson, json
import sys
from pprint import pprint

if len(sys.argv) != 4:
	print 'usage: python text_to_json.py input.txt output.json "episode title"'
	exit()

colorFile = open(sys.argv[1], 'r')

colorText = colorFile.readlines()

arcDict = {}
arcDict["title"] = sys.argv[3]

arcList = []

for i in range(0, len(colorText)):
	for j in range(0, len(colorText)):
		if colorText[i] == colorText[j] and j <> i:
			pair = []
			pair.append(i)
			pair.append(j)
			if not pair in arcList and not pair[::-1] in arcList:
				arcList.append(pair)

arcDict['arcs'] = arcList

nodeList = []

for i in range(0, len(colorText)):
	nodeList.append({'name': 'Frame ' + str((i+1)),'color': '#'+colorText[i].rstrip('\n ')})

arcDict['nodes'] = nodeList

#make empty list
#make a dict with color and name
#add values for color and name

with open(sys.argv[2], 'w') as file:
	file.write(json.dumps(arcDict, indent = 4, sort_keys = True))
			
#testDict = {}
#testDict['arcs'] = [0,5]
#testDict['arcs'] = [0,7]
#print json.dumps(testDict)

#for color in colorText:
#	print color

#colorText = [line.split(',') for line in colorFile]

#colorText[0] = colorText[0].split('\n')

#print colorText
