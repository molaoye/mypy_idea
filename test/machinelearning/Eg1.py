# coding=utf-8

'''
入门机器学习的第一个程序！（python版） - CSDN博客.mhtml
'''

from sklearn import tree

feature=[[178, 1], [155, 0], [177, 0], [165, 0], [169, 1], [160, 0], [176, 1]]

label=['male', 'female', 'female', 'male', 'male', 'female', 'male']

clf=tree.DecisionTreeClassifier()

clf=clf.fit(feature, label)

print(clf.predict([[158, 0]]))

print(clf.predict([[172, 1]]))
