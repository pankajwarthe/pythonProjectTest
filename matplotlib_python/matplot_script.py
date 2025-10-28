
from matplotlib import pyplot as plt

x_values = [1,2,3,4]
y_values = [5,4,6,2]

plt.plot(x_values, y_values)
plt.show()

plt.scatter(x_values,y_values)
plt.show()

plt.bar(x_values,y_values)
plt.show()

plt.xlabel('x values')
plt.ylabel('y values')

plt.title('My first matplotlib graph')
plt.show()

#plt.pie(x_values,y_values)
#plt.show()
