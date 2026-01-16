import tensorflow as tf
print(tf.__version__)

# Check GPU (Metal)
print(tf.config.list_physical_devices('GPU'))
