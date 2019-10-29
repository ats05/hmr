import tensorflow as tf

modelDir = "./models/savedModel"

converter = tf.lite.TFLiteConverter.from_saved_model(modelDir)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_quant_model = converter.convert()
