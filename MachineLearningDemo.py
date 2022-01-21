# Machine Learning Demo - Iris Flower Problem

# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

print(dataset.shape,"\n") # Gives dimensions of dataset, how many rows, how many columns
print(dataset.head(20),"\n") # Gives first number of rows (20 here) to look at
print(dataset.describe(),"\n") # Gives a summary of all data
print(dataset.groupby('class').size(),"\n") # Tells us how the data is distributed

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False) # box and whisker plots
#pyplot.show() 

dataset.hist() # histograms
#pyplot.show() 

scatter_matrix(dataset) # scatter plot matrix
#pyplot.show()


# Split-out validation dataset
array = dataset.values
X = array[:,0:4] # Input variables, selects all rows and all columns except last
# X effectively is all data except the last column which has the results

y = array[:,4] # Output variables, selects all rows and last column
# y is only the last column which is the result data

X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVC', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print("\naccuracy_score:",accuracy_score(Y_validation, predictions),"\n")
print("confusion_matrix:\n",confusion_matrix(Y_validation, predictions),"\n")
print(classification_report(Y_validation, predictions))
