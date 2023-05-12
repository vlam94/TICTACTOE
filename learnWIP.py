import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import seaborn as sns
from os.path import getsize



try: 
    model_path = 'tic_tac_toe_model.h5'
    assert getsize(model_path) < 13, "\nWHOA! It seems you've already trained the model!\nContinuing will overwrite it\n\n ABORTING!\n"
except AssertionError as e:
    print (e)
    exit()
ds_path = 'ttt_ds.pkl'

with open (ds_path, mode='br') as f:
    ds = pickle.load(f)

model = Sequential()
model.add(Dense(64, input_dim=18, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(9, activation='softmax'))
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['top_k_categorical_accuracy'])
print('\n\n\n\n\n\n')
xdata = []
ydata = []
for log in ds:
    xdata.append(np.array(log[0]).flatten())
    ydata.append(np.array(log[1]).flatten())

xdata = np.array(xdata)
ydata = np.array(ydata)
vsize = .15
x_train, x_val, y_train, y_val = train_test_split(xdata, ydata,train_size=(1-vsize), test_size=vsize, random_state=42)
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=6, batch_size=15)

# Plot the training and validation loss curves
sns.set_style('whitegrid')
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss Curves')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Plot the training and validation accuracy curves
plt.plot(history.history['top_k_categorical_accuracy'], label='Training Top-5 Accuracy')
plt.plot(history.history['val_top_k_categorical_accuracy'], label='Validation Top-5 Accuracy')
plt.title('Training and Validation Top-2 Accuracy Curves')
plt.xlabel('Epochs')
plt.ylabel('Top-5 Accuracy')
plt.legend()
plt.show()


model.save(model_path)










#df_sorted = df.sort_values(by=[9,0, 1, 2, 3, 4, 5, 6, 7, 8]) #used for sorting previous file format