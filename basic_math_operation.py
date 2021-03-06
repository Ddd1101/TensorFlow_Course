import tensorflow as tf
import os

a = tf.constant(5.0, name="a")
b = tf.constant(10.0, name="b")

x = tf.add(a, b, name="add")
y = tf.div(a, b, name="divide")

with tf.Session() as sess:
    print("a = ", sess.run(a))
    print("b = ", sess.run(b))
    print("a + b = ", sess.run(x))
    print("a / b = ", sess.run(y))

sess.close()
