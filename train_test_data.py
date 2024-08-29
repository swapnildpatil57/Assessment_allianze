
# Train/Test is a method to measure the accuracy of your model.

# It is called Train/Test because you split the data set into two sets: a training set and a testing set.

# 80% for training, and 20% for testing.

# Train the model means create the model.

# Test the model means test the accuracy of the model.


#100 customers in shop with their buying habits


#random.normal() method to get a Normal Data Distribution.

#random(maen,std_dev, size of returned array)

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
from sklearn.metrics import r2_score


# The x axis represents the number of minutes before making a purchase.

# The y axis represents the amount of money spent on the purchase.


x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

#splitting data into test and train(80 and 20)

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]



# plt.scatter(train_x, train_y)
# plt.show()

# plt.scatter(test_x, test_y)
# plt.show()


mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()


r2_train = r2_score(train_y, mymodel(train_x))

print(r2_train)

r2_test = r2_score(test_y, mymodel(test_x))


print(r2_test)

print (mymodel(5))










