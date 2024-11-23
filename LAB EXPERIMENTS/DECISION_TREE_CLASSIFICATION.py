from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = np.array([
    [170, 65, 42],
    [180, 75, 44],
    [160, 50, 38],
    [175, 70, 43],
    [165, 55, 39],
    [185, 80, 45]
])


Y = np.array([0, 1, 0, 1, 0, 1])


clf = DecisionTreeClassifier()


clf.fit(X, Y)

new_data = np.array([[168, 52, 38]])

prediction = clf.predict(new_data)

print("Predicted gender:", "Male" if prediction[0] == 1 else "Female")