import simplejson, json
import sys

if len(sys.argv) != 4:
	print 'usage: python text_to_json.py input.txt output.json "episode title"'
	exit()

colorFile = open(sys.argv[1], 'r')

colorText = colorFile.readlines()

arcDict = {}
arcDict["title"] = sys.argv[3]

arcList = []
nodeList = []
print "Frames: " + str(len(colorText))
for i in range(len(colorText)):
	nodeList.append({'name': 'Frame ' + str(i+1),'color': '#'+colorText[i].rstrip('\n\r ')})
	for j in range(i+1, len(colorText)):
		if colorText[i] == colorText[j]:
			arcList.append([i,j])

arcDict['arcs'] = arcList
arcDict['nodes'] = nodeList

with open(sys.argv[2], 'w') as file:
	file.write(json.dumps(arcDict))

