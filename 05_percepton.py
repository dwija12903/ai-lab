import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.random.rand(input_size + 1)  # +1 for bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    def sigmoid(self,x):
        return 1 / (1 + np.exp(-x))

    def predict(self, inputs):
        inputs = np.insert(inputs, 0, 1)  # Inserting bias term
        activation = np.dot(self.weights, inputs)
        return 1 if self.sigmoid(activation) >= 0.5 else 0

    def fit(self, X, y):
        for _ in range(self.epochs):
            for inputs, label in zip(X, y):
                prediction = self.predict(inputs)
                error = label - prediction
                update = self.learning_rate * error
                self.weights += update * np.insert(inputs, 0, 1)

# Data for AND, OR, and XOR
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_or = np.array([0, 1, 1, 1])

X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])

# Create Perceptron instances for AND, OR, and XOR
and_perceptron = Perceptron(input_size=2)
or_perceptron = Perceptron(input_size=2)
xor_perceptron = Perceptron(input_size=2)

# Train the perceptrons
and_perceptron.fit(X_and, y_and)
or_perceptron.fit(X_or, y_or)
xor_perceptron.fit(X_xor, y_xor)

# Test predictions
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

print("AND Perceptron Predictions:")
for data in test_data:
    print(f"Input: {data}, Predicted Output: {and_perceptron.predict(data)}")

print("\nOR Perceptron Predictions:")
for data in test_data:
    print(f"Input: {data}, Predicted Output: {or_perceptron.predict(data)}")

print("\nXOR Perceptron Predictions:")
for data in test_data:
    print(f"Input: {data}, Predicted Output: {xor_perceptron.predict(data)}")