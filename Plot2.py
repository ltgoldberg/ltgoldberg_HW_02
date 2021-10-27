import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('class_size.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter = ',')
	
	for row in plots:
		x.append(row[3])
		y.append(row[8])
x.pop(0)
y.pop(0)

plt.bar(x, y, color = 'g', width = 0.72)
plt.xlabel('Course')
plt.ylabel('Number of Students')
plt.title('Number of Students in Each Course')
plt.legend()
plt.show()
