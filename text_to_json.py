import simplejson, json

colorFile = open('/home/yala1/cs467/technicolor/test_colors.txt', 'r')

colorText = colorFile.readlines()

arcDict = {}

for i in range(0, len(colorText)):
	for j in range(0, len(colorText)):
		if colorText[i] == colorText[j] and j <> i:
			print i, j

#for color in colorText:
#	print color

#colorText = [line.split(',') for line in colorFile]

#colorText[0] = colorText[0].split('\n')

#print colorText
