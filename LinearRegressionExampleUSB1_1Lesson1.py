import tensorflow
x = np.array([1,2,3])
weights = np.array([0.5, 0.35, 0.2])
bias = np.array([1,1,1])
def function(inputs):
  return tf.matmul(weights, inputs) + b 
print(function(x))
