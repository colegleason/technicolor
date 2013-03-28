import simplejson, json

from pprint import pprint

colorFile = open('/home/yala1/cs467/technicolor/test_colors.txt', 'r')

colorText = colorFile.readlines()

arcList = []

for i in range(0, len(colorText)):
	for j in range(0, len(colorText)):
		if colorText[i] == colorText[j] and j <> i:
			pair = []
			pair.append(i)
			pair.append(j)
			if not pair in arcList and not pair[::-1] in arcList:
				arcList.append(pair)

arcDict = {}

arcDict['arcs'] = arcList

nodeList = []

for i in range(0, len(colorText)):
	nodeList.append({'name': 'Episode ' + str((i+1)),'color': colorText[i]})

arcDict['nodes'] = arcList

#make empty list
#make a dict with color and name
#add values for color and name

with open("test_color.json", "w") as file:
	file.write(json.dumps(arcDict))
			
#testDict = {}
#testDict['arcs'] = [0,5]
#testDict['arcs'] = [0,7]
#print json.dumps(testDict)

#for color in colorText:
#	print color

#colorText = [line.split(',') for line in colorFile]

#colorText[0] = colorText[0].split('\n')

#print colorText
