from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
X = [[ 1, 2, 3], # 2 samples, 3 features
    [11, 12, 13]]
y = ['a', 'b'] # class labels of each sample
clf.fit(X, y) # model fiGng

print(clf.predict([[4, 5, 6], [14, 15, 16], [5, 7, 4]]))