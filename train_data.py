import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)
X = np.random.rand(100, 1)
y = 2.0 + 3.0 * X + np.random.randn(100, 1) * 0.5  # y = 2 + 3x + noise

# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_dim=1)  # Dense layer with 1 unit (output) and 1 input dimension
])

# Compile the model
model.compile(optimizer='sgd', loss='mse')  # Using stochastic gradient descent optimizer and mean squared error loss

# Print model summary
model.summary()

# Train the model
history = model.fit(X, y, epochs=30, batch_size=10, verbose=1)

# Plot training history
plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

# Predict using the trained model
X_test = np.array([[0.1], [0.2], [0.3]])
predictions = model.predict(X_test)
print("Predictions:")
print(predictions)
