'''
with open ('homeless.csv') as f:
    text=f.read()
print(text)

import os 
print(os.getcwd())
'''
'''
with open ('homeless.csv', encoding = ascii) as f:
    text=f.read()
print(text)
'''
'''
import csv 
sizeFile = open ('class_size.csv')
sizeReader = csv.reader(sizeFile)
sizeData = list(sizeReader)


scoreFile = open ('race_score.csv')
scoreReader = csv.reader(scoreFile)
scoreData = list(scoreReader)
'''
import csv
import matplotlib.pyplot as plt

x_coordinates = [2006, 2007, 2008, 2009, 2010, 2011]
y1_asian= [687, 695, 700, 705, 703, 702]
y2_black = [644, 654, 661, 669, 669, 670]
y3_hispanic = [647, 657, 664, 673, 673, 673]
y4_white = [676, 684, 690, 696, 695, 695]

plt.plot(x_coordinates, y1_asian, label = 'Asian Students')

plt.plot(x_coordinates, y2_black, label = 'Black Students')
plt.plot(x_coordinates, y3_hispanic, label = 'Hispanic Students')
plt.plot(x_coordinates, y4_white, label = 'White Students')
plt.xlabel('Year')
plt.ylabel('Test Score Avg.')
leg = plt.legend()

plt.show()


'''
import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('class_size.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	
	for row in plots:
		x.append(row[2])
		y.append(int(row[7]))

plt.bar(x, y, color = 'g', width = 0.72, label = "Grade")
plt.xlabel('Number of Students')
plt.ylabel('Grade')
plt.title('Number of Students in Each Grade')
plt.legend()
plt.show
'''
'''
import csv as plt   
df = plt.read_csv("race_score.csv")

style = ('ggplot')

df.groupby('Race').plot(x='Year', y='Score')

plt.title('Score Avg. by Race')
plt.ylabel('Score')
plt.xlabel('year')

plt.show()
'''

'''
# this code generates a plot
import homeless.csv as plt
fig, ax = plt.subplots()
ax.bar(terms, counts) #this line does the plotting for us 
plt.show() 
'''
'''
#plot([x], y, [fmt], *, data=None, **kwargs)
#plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
import csv as plt
time = [0, 1, 2 ,3]
position = [0, 100, 200, 300]
plt.plot(time, position)
plt.xlabel('Time(hr)')
plt.ylabel('Position(km)')

'''
'''
fig, ax = plt.subplots()
ax.bar(terms, counts) #this line does the plotting for us 
plt.show() 
'''