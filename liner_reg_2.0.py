import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv("examscore and tutoring sessions.csv")
print(data)
plt.scatter(data.Tutoring_Sessions, data.Exam_Score)
plt.show()

# def loss_function(m, b, points):
#     total_error = 0
#     for i in range(len(points)):
#         x = points.iloc[i].Tutoring_Sessions
#         y = points.iloc[i].Exam_score
#         total_error += (y - (m * x + b)) ** 2
#     total_error / float(len(points))

def gradient_descent(m_now, b_now, points, L ):
    m_gradient = 0
    b_gradient = 0

    n = len(points)
    for i in range(n):
        x = points.iloc[i].Tutoring_Sessions
        y = points.iloc[i].Exam_Score

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return m, b
    
m = 0
b = 0
L = 0.0001
epochs = 500

for i  in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, data, L)
print("Final Values ", m, b)

plt.scatter(data.Tutoring_Sessions, data.Exam_Score, color = "black")
plt.plot(list(range(0,10)), [m * x+b for x in range(0, 10)], color="red")
plt.show()










