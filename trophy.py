print('Hello friend. Please input the number of trophies you have to see how many points you are from the next level.')

bronze = input('Bronze trophies: ')
silver = input('Silver trophies: ')
gold = input('Gold trophies: ')
platinum = input('Platinum trophies: ')

points = 15 * bronze + 30 * silver + 90 * gold + 180 * platinum

level_array=[0,200,600,1200,2400,4000]
i = 5
while i < 11:
	level_array.append(level_array[i] + 2000)
	i += 1
while i < 25:
	level_array.append(level_array[i] + 8000)
	i += 1
while points > level_array[-1]:
	level_array.append(level_array[i] + 10000)
	i += 1
level = 1
while points > level_array[level-1]:
	level += 1
else:
	left = level_array[level-1] - points
	print 'You are currently at level ' + str(level-1) + '. You need ' + str(left) + ' points until level ' + str(level) + '.'