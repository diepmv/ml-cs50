"""
Classifying images
"""
import numpy as np
import matplotlib.pyplot as plt


#Load the digits dataset from sklearn

from sklearn import datasets

digits = datasets.load_digits()
#(The dataset contains 1797 images.Two arrays: digits.images and digits.target )

print(digits.images[0])

#Let plot this!

plt.figure()
plt.imshow(digits.images[0], cmap = plt.cm.gray_r, interpolation = 'nearest')
plt.show()


#Print true label

print(digits.target[0])


#Create the training set by choosing the first 10 images in the data set:
X_train = digits.data[0:10]
Y_train = digits.target[0:10]

#Choose a test image
X_test = digits.data[345]

#PLot it
plt.figure()
plt.imshow(digits.images[345], cmap = plt.cm.gray_r, interpolation="nearest")
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


print("Number of mistakes done in testing 100 images:")

no_errors = 0
distance = np.zeros(num)

for j in range(1697, 1797):
  X_test = digits.data[j]
  for i in range(num):
    distance[i] = dist(X_train[i], X_test)
  min_index = np.argmin(distance)
  if Y_train[min_index] != digits.target[j]:
    no_errors += 1
print(no_errors)


#Impove the perfomance
#Enlarge the training data from 10 to 1000 images:
X_train = digits.data[0:1000]
Y_train = digits.target[0:1000]


print("Number of mistakes done in testing 100 images:")

num = len(X_train)
no_errors = 0
distance = np.zeros(num)

for j in range(1697, 1797):
  X_test = digits.data[j]
  for i in range(num):
    distance[i] = dist(X_train[i], X_test)
  min_index = np.argmin(distance)
  if Y_train[min_index] != digits.target[j]:
    no_errors += 1
print(no_errors)


#CIFAR-10 - Object Recognition in Images: https://www.kaggle.com/c/cifar-10
