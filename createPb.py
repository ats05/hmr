import os
import tensorflow as tf
import tensorflowjs as tfjs

print(tf.__version__)

# Get the current directory
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/models"
print("Current directory : " + dir_path)
save_dir = dir_path + '/Protobufs/' + tf.__version__

graph = tf.get_default_graph()

# Create a session for running Ops on the Graph.
sess = tf.Session()

print("Restoring the model to the default graph ...")

saver = tf.train.import_meta_graph(dir_path + '/model.ckpt-667589.meta')
print(dir_path + "/model.ckpt-667589")
# .index

saver.restore(sess,"/Users/atsushi/Documents/develop/hmr/models/model.ckpt-667589")
print("Restoring Done .. ")

print("Saving the model to Protobuf format: " + save_dir)

#Save the model to protobuf  (pb and pbtxt) file.
tf.train.write_graph(sess.graph_def, save_dir, "saved_model.pb", False)
tf.train.write_graph(sess.graph_def, save_dir, "saved_model.pbtxt", True)


print(tf.saved_model)

print("Saving Done .. ")
