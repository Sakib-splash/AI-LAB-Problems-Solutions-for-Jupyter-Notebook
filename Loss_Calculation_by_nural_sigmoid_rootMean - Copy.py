import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def loss(predicted, actual):
    return np.mean((predicted - actual) ** 2)

input_size = 2
output_size = 1

W1 = np.random.randn(input_size, output_size)
b1 = np.random.randn(output_size)

# Define the input for the AND gate
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

target = np.array([[0], [0], [0], [1]])

final_output = None

best_loss = float('inf')
best_W1 = None
best_b1 = None


num_iterations = 100

for iteration in range(num_iterations):
    final_output = np.dot(x, W1) + b1
    output = sigmoid(final_output)

    current_loss = loss(output, target)

    if current_loss < best_loss:
        print('New best weights found, iteration:', iteration + 1, 'loss:', current_loss)
        best_loss = current_loss
        best_W1 = W1.copy()
        best_b1 = b1.copy()
    else:
        W1 = best_W1.copy()
        b1 = best_b1.copy()

    W1 += 0.09 * np.random.randn(input_size, output_size)
    b1 += 0.09 * np.random.randn(output_size)

W1 = best_W1
b1 = best_b1

final_output = np.dot(x, W1) + b1
output = sigmoid(final_output)

print("Final output after training:")
print(output)
