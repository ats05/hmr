
import tensorflow as tf


RECORD_NAME = "./prepared_datasets/coco/train_0072_wmeta.tfrecord"


example = next(tf.python_io.tf_record_iterator(RECORD_NAME))
print(tf.train.Example.FromString(example))



cnt = len(list(tf.python_io.tf_record_iterator(RECORD_NAME)))
print("data counts : {}".format(cnt))
