import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

ds_path = 'ttt_ds.pkl'
with open (ds_path, mode='br') as f:
    ds = pickle.load(f)

model = Sequential()
model.add(Dense(64, input_dim=18, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(9, activation='softmax'))
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
print('\n\n\n\n\n\n')
xdata = []
ydata = []
for log in ds:
    xdata.append(np.array(log[0]).flatten())
    ydata.append(np.array(log[1]).flatten())

xdata = np.array(xdata)
ydata = np.array(ydata)
vs = .2
x_train, x_val, y_train, y_val = train_test_split(xdata, ydata,train_size=(1-vs), test_size=vs, random_state=42)












#df_sorted = df.sort_values(by=[9,0, 1, 2, 3, 4, 5, 6, 7, 8]) #used for sorting previous file format