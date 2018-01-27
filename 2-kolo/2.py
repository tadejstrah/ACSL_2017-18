x = []
oklepaji = [None] * 4
oklepaji_pos = [None] * 4
manjkajoc = 0
manjkajoc_pos = 0

with open("input") as y:
	for neki in y:
		x.append(neki)

for line in x:
	for i in range(4):
		oklepaji[i] = False
		oklepaji_pos[i] = 0


	for i in range(len(line)):

		if line[i] == "[":
			oklepaji[0] = True
			oklepaji_pos[0] = i+1
		if line[i] == "]":
			oklepaji[1] = True
			oklepaji_pos[1] = i+1
		if line[i] == "(":
			oklepaji[2] = True	
			oklepaji_pos[2] = i+1
		if line[i] == ")":
			oklepaji[3] = True
			oklepaji_pos[3] = i+1

	for i in range(len(oklepaji)):
		if oklepaji[i] == False:
			manjkajoc = i


	print(line.strip())
	#for i in range(len(oklepaji)):
	#	print(oklepaji[i],oklepaji_pos[i])

	print(manjkajoc)
	#print(oklepaji,oklepaji_pos)
	print()
