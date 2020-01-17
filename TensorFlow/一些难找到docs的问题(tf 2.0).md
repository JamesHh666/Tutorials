# 1 Change learning rate 
For training, I did not use `model.compile` and `model.fit` to train, so how can I change lr during training? </br>
Thanks to [Stewart_R](https://stackoverflow.com/users/2455494/stewart-r)'s answer at [stackoverflow](https://stackoverflow.com/questions/57301698/how-to-change-a-learning-rate-for-adam-in-tf2), he shows a solution where you can define your own **lr scheduler** 
```python
class LearningRateReducerCb(tf.keras.callbacks.Callback):

  def on_epoch_end(self, epoch, logs={}):
    old_lr = self.model.optimizer.lr.read_value()
    new_lr = old_lr * 0.99
    print("\nEpoch: {}. Reducing Learning Rate from {} to {}".format(epoch, old_lr, new_lr))
    self.model.optimizer.lr.assign(new_lr)
```
Or you can refer to the source code from keras [ReduceLROnPlateau](https://github.com/keras-team/keras/blob/master/keras/callbacks/callbacks.py#L946)

# 2 Add a list of `tf.Tensor` together
Just use `tf.reduce_sum`
```python
list_sum = tf.reduce_sum(list_of_tensors)
```
