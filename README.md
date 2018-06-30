# Specifications of the Face Recognizer System
* 透過深度學習訓練一個基本的人臉辨識系統 

## 組員
* 410421250 王泰翔
* 410421216 蕭子渝
* 410421230 黃英聰

## (a)訓練相關使用
* 語言 - Python
* 工具 - Keras , PIL
* 神經網路結構 - CNN 
* Model - Sequential
* Batch size - 16
* Optimizer - Adadelta (放棄: Adam , RMSProp)


## 相關技術
* Conv2D
* Dropout
* MaxPooling2D
* activation - Relu , Softmax
* Same Padding
* Crossentropy

## (b)the modules enclosed in your recognizer and their functions
```
model = Sequential()

model.add(Conv2D(128, 3, activation="relu", input_shape=(240, 180, 3),padding='same'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, 3 , activation="relu",padding='same'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, 3, activation="relu",padding='same'))
model.add(Dropout(0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(51, activation='softmax'))
model.summary()
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

train_history = model.fit(x_data,x_label,
          batch_size=16,
          epochs=20,
          verbose=1,
          shuffle=True,
          validation_data=(y_data,y_label))
```
```
for filename in os.listdir(path):
    if(filename[0] == 's'):
        test = Image.open(path+'\\'+filename)
        
        num = int(filename[1]) * 10 + int(filename[2]) 
        matrix = np.array(test) / 255
        num_temp = int(filename[4]) * 10 + int(filename[5]) 
        #print(matrix[0][0])
        
        if(n!=num):
            n=num
            random_list=[1,2,3,4,6,7,8,10,11,12,13,14,15]
            random.shuffle(random_list)
        if(num_temp==random_list[0] or num_temp==random_list[1]):
            y_test.append(matrix)
            y_one_hot.append(num)
            
        x_train.append(matrix)
        x_one_hot.append(num)
            
        '''
        else:
            x_train.append(matrix)
            x_one_hot.append(num)
        '''
            
        '''
        if(num_temp >= 14):
            y_test.append(matrix)
            y_one_hot.append(num)
           
        else:
            x_train.append(matrix)
            x_one_hot.append(num)
        '''
  
x_data = np.array(x_train)
x_label = np.array(x_one_hot)          

y_data = np.array(y_test)
y_label = np.array(y_one_hot)
```

## (c)how we test our recognizer to evaluate its recognition rate


## 訓練成果
* 這是有另外隔出validation set的
![image](https://github.com/410421250/Face_recignition/blob/master/Performance%20Image/with_valid.jpg)

* 後來想到要demo的時候助教已將2張圖片隔離所以想試試看不隔出validation set的話demo的時候可以到達什麼程度，也因此val_acc必定到達1
![image](https://github.com/410421250/Face_recignition/blob/master/Performance%20Image/no_valid.jpg)

## 辨識成果
![image](https://github.com/410421250/Face_recignition/blob/master/Performance%20Image/perform.jpg)



