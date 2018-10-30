import tensorflow as tf
import numpy as np
#Model Generator
x=tf.placeholder(tf.float32)
W=tf.Variable(.3,tf.float32)
b=tf.Variable(.4,tf.float32)
Model=W*x+b
y=tf.placeholder(tf.float32)
error=tf.reduce_sum(tf.square(Model-y))
#Selected Optimizer
optimizer=tf.train.GradientDescentOptimizer(0.01)
#Minimized Function
train=optimizer.minimize(error)
#Modules
variables_starter=tf.global_variables_initializer()
#Session
ses=tf.Session()
#Start all the Variables with default Values
ses.run(variables_starter)
for i in range(1000):
    ses.run(train,{x:[1,2,3,4],y:[2,4,6,8]})
print(ses.run(error,{x:[1,2,3],y:[3,4,5]}))
print(W.value())
