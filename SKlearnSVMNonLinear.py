#Team Members:
# Dhruv Bajpai - dbajpai - 6258833142
# Anupam Mishra - anupammi - 2053229568

from sklearn import svm
import numpy as np
import sys

def getData():
    fil = open(sys.argv[1])
    aa = fil.readlines()
    aa = [line[:-1] for line in aa ]
    data = np.array([[ float(ele) for ele in line.split(',')] for line in aa])
    Y = data[:,-1]
    Y = Y.reshape(len(data),-1)
    X = data[:,:-1]
    return X,Y

def main():
    X,Y = getData()
    clf = svm.SVC(kernel='poly',random_state=0,degree=2)
    clf.fit(X, Y.T.tolist()[0])
    print("Support Vectors: {}".format(clf.support_vectors_))

if __name__ == '__main__':
    main()