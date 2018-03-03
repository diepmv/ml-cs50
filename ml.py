import numpy as np
import matplotlib.pyplot as plt

X_train = np.array([[1,1], [2, 2.5], [3, 1.2], [5.5, 6.3], [6,9], [7,6]])
Y_train = ['red', 'red', 'red', 'blue', 'blue', 'blue']

#Create a test point:
X_test = np.array([3, 4])

plt.figure()
plt.scatter(X_train[:,0], X_train[:,1], s=170, color=Y_train[:])
plt.scatter(X_test[0], X_test[1], s=170, color='green')
plt.show()



#Distance function
def dist(x, y):
  return np.sqrt(np.sum((x-y)**2))



# for each point X_train we compute its distance to X_test:

num = len(X_train)
distance = np.zeros(num)
for i in range(num):
  distance[i] = dist(X_train[i], X_test)
print(distance)



#Choose the point in X_train with the minimal distance from X_new

min_index = np.argmin(distance)

print(Y_train[min_index])
