print('Hello friend. Please input the number of trophies you have to see how many points you are from the next level.')

bronze = input('Bronze trophies: ')
silver = input('Silver trophies: ')
gold = input('Gold trophies: ')
platinum = input('Platinum trophies: ')

points = 15 * bronze + 30 * silver + 90 * gold + 180 * platinum

levelArray=[0,200,600,1200,2400,4000]
i = 0
j = 0
k = 0
while i < 6:
	levelArray.append(levelArray[i+5] + 2000)
	i += 1
while j < 14:
	levelArray.append(levelArray[j+11] + 8000)
	j += 1
while points > levelArray[-1]:
	levelArray.append(levelArray[k+25] + 10000)
	k += 1
level = 1
while points > levelArray[level-1]:
	level += 1
else:
	left = levelArray[level-1] - points
	print('You are currently at level ' + str(level-1) + '. You need ' + str(left) + ' points until level ' + str(level) + '.')