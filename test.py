import tensorflow 
import numpy as np 
A = tf.constant([[4.1, 2.8], [9.676, 6.608]], dtype=tf.float32)
Ainvnp = np.linalg.inv(A)
print(A2inv)

Ainvtf = tf.linalg.inv(A)
print(Ainvtf)