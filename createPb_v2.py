# coding:utf-8
# tensorflow version1.13.1
import tensorflow as tf

saver = tf.train.import_meta_graph('models/model.ckpt-667589.meta', clear_devices=True)

with tf.Session() as sess:

  chpt_state = tf.train.get_checkpoint_state('models/model.ckpt-667589')

 # if chpt_state:
    # last_model = chpt_state.model_checkpoint_path
  last_model = "models/model.ckpt-667589"
  saver.restore(sess,last_model)
  print ("model was loaded",last_model)
#  else:
#    print ("model cannot loaded")
#    exit(1)

  graph = tf.get_default_graph()
  graph_def = graph.as_graph_def()

  x = graph.get_tensor_by_name('x:0')
  out = graph.get_tensor_by_name('reduce/out:0')
  tf.saved_model.simple_save(sess, './models', inputs={"x": x}, outputs={"reduce/out": out})
