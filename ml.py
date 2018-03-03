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


