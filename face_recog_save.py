# -*- coding: utf-8 -*-

import cv2

#顔のカスケード分類器のファイルを同じディレクトリに入れてパス指定
cascade_path = "haarcascade_frontalface_alt.xml"

#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)

#対象の人物の写真を入れる。デフォルトは有名なLennaさんと、徳川慶喜。
photo_name = "Lenna.png"
#photo_name = "yoshinobu.jpg"

img = cv2.imread(photo_name)
#img = cv2.imread('Lenna.png')

# 顔を検知
faces = cascade.detectMultiScale(img, minSize=(100,100))#顔miniサイズを追加

#このコードでは、一つの写真には一人だけ写っている前提
for (x,y,w,h) in faces:
    # 検知した顔を矩い青の四角形で囲む
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #顔の部分だけのカット写真を作る。
    cut_img = img[y:y+h,x:x+w]

# 画像表示
cv2.imshow('img',img)

# 以下、「PythonとOpenCVで画像処理①【読み込み、表示、保存】
#http://rasp.hateblo.jp/entry/2016/01/22/201534」を参考に記述。

#キーが押されるまで画像を表示したままにする。
#戻り値: 押されたキーコード
keycode = cv2.waitKey(0)

# "S"を押すと、face_of_写真名というファイル名で顔の部分の写真を保存する。
if keycode == ord('s'):
    #画像を保存
     #第一引数: 保存するファイル名
     #第一引数: 保存したい画像
    cv2.imwrite("face_of_" + photo_name,cut_img)

# 作成したウィンドウをすべて破棄
cv2.destroyAllWindows()
