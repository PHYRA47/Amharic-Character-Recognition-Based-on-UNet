import tensorflow as tf

from keras.models import load_model

print(tf.__version__)

model = load_model("datasets/Amharic character Image dataset/models/fcnn-arct/paper_best_val_loss_model.h5")

loss, _, _, row_acc, col_acc = model.evaluate(test_data, [test_labels_row,test_labels_col], verbose=False)

print('row_accuracy: {:5.4f}%'.format(100 * row_acc))
print('col_accuracy: {:5.4f}%'.format(100 * col_acc))
print()
print('accuracy: {:5.4f}%'.format(100 * (row_acc + col_acc)/2))
print('val_loss: {:5.4f}%'.format(100 * loss))