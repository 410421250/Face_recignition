[valid]:https://github.com/410421250/Face_recignition/blob/master/Performance%20Image/with_valid.jpg
[novalid]:https://github.com/410421250/Face_recignition/blob/master/Performance%20Image/no_valid.jpg
[correct]:https://github.com/410421250/Face_recignition/blob/master/Performance%20Image/perform.jpg
[incorrect]:https://github.com/410421250/Face_recignition/blob/master/Performance%20Image/incorrect.jpg


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
上面是我們使用的model。  
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
```
這部分是資料預處理，因為原資料庫是一個人15張照片，已經有兩張被抽取起來做demo時使用，所以就將剩餘的13張全數丟入model訓練。

## (c)how we test our recognizer to evaluate its recognition rate

1. 隨機在除了5和9以外，1至15之間取兩個數字。
2. 將那兩個數字的圖片抽出當作validation set，以測試辨識率。
3. 將全部13x50張照片丟入model訓練，觀察辨識率。
4. 將訓練好的model載入，並將照片丟入model，觀察結果。

## (d)the problems suffered in our development
* model不知道該用甚麼形狀(層數、filter數量、是否Dropout等等)，將每一種形狀都訓練一次，慢慢測試後才決定用現在的model。
* optimizer測試過Adam,RMSProp,Adadelta後差別不大，最後決定用Adadelta。
* batch size最初是使用128，但GPU無法承受，但用1正確率非常慘，最後決定用16。
* 資料預處理的時候，最初是將後兩張(編號14,15)當作validation set，其他11張當作train data訓練。後來突發奇想，改成隨機抽取兩張當作validation set，正確率並沒有提升。後來想到將demo時要測試的2x50張照片當作validation set，剩下的全部當作training data，所以就將全部13x50張照片丟入model訓練。(所以每個階段的model各有一個，總共三個model，demo時所使用的是最後一個no_valid_model.h5)

## (e)分工方式

* 蕭子渝:思考資料預處理的方式，model的雛型，model形狀的發想，照片統一大小。
* 黃英聰:model形狀的實作，資料預處理後續實作，程式優化及debug。
* 王泰翔:model的雛形，辨識程式的實作，資料預處理初步架構。

## (f)特殊功能

* 在測試時，當預測出的答案和正確答案不同時，會要求input當作暫停。(但不包含最高可能性前五個中的後4個)

## 訓練成果
* 這是有另外隔出validation set的
![valid]

* 後來想到要demo的時候助教已將2張圖片隔離所以想試試看不隔出validation set的話demo的時候可以到達什麼程度，也因此val_loss非常的低
![novalid]
## 辨識成果
***
|辨識準確      |辨識不準確    |
|:-----------:|:-----------:|
|![correct]   |![incorrect] |

## (g)心得感想
* 蕭子渝:原先專題就是用類似的技術，所以整體來說技術上沒有太大的困難，真要說的話只有發現照片大小不一的reshape和資料預處理的部分需要查一下，最後就是model的形狀，層數和一些參數的選擇比較花時間而已。最後demo的成果雖然沒有到心中的目標95%，不過還可以接受。
* 黃英聰:
* 王泰翔:


