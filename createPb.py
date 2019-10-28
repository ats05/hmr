import os
import tensorflow as tf
import tensorflowjs as tfjs

print(tf.__version__)

# Get the current directory
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/models"
print("Current directory : " + dir_path)
save_dir = dir_path + '/Protobufs/' + tf.__version__


# Create a session for running Ops on the Graph.

print("Restoring the model to the default graph ...")

print(dir_path + "/model.ckpt-667589")
saver = tf.train.import_meta_graph(dir_path + '/model.ckpt-667589.meta')
graph = tf.get_default_graph()
input_graph_def = graph.as_graph_def()
sess = tf.Session()
saver.restore(sess,dir_path + "/model.ckpt-667589")

for v in tf.trainable_variables():
  vars[v.value().name] = v.eval() 

# .index


g_2 = tf.Graph()
consts = {}
with g_2.as_default():
  with tf.Session() as sess:
    for k in vars.keys():
      consts[k] = tf.constant(vars[k])

    tf.import_graph_def(g_1.as_graph_def(), input_map=consts, name="")
    tf.train.write_graph(g_2.as_graph_def(), './', 'trained_graph.pb', as_text=False)

print("Restoring Done .. ")

exit();

print("Saving the model to Protobuf format: " + save_dir)

#Save the model to protobuf  (pb and pbtxt) file.
tf.train.write_graph(sess.graph_def, save_dir, "saved_model.pb", False)
tf.train.write_graph(sess.graph_def, save_dir, "saved_model.pbtxt", True)


print(tf.saved_model)

print("Saving Done .. ")
