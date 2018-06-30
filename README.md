# Specifications of the Face Recognizer System
* 透過深度學習訓練一個基本的人臉辨識系統 

## 訓練相關使用
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

## 訓練成果
* 這是有另外隔出validation set的

* 後來想到要demo的時候助教已將2張圖片隔離所以想試試看不隔出validation set的話demo的時候可以到達什麼程度，也因此val_acc必定到達1
[image]https://github.com/410421250/Face_recignition/blob/master/Performance%20Image/no_valid.jpg

