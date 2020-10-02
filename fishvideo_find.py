import copy
import cv2
import joblib
import os

# 学習済みデータを取り出す
clf = joblib.load("fish.pkl")
output_dir = "./bestshot"
img_last = None  # 前回の画像
fish_th = 2  # 画像を出力するかどうかのしきい値
count = 0
frame_count = 0

# output_dirがなければフォルダを作って指定する
# isdirは指定のファイルのpathがあるか見る
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

# 動画ファイルから入力を開始
cap = cv2.VideoCapture("fish.mp4")
while True:
    # 画像を取得
    is_ok, frame = cap.read()
    if not is_ok:
        break

    frame = cv2.resize(frame, (500, 250))
    # frameの値をframe2にコピー
    frame2 = copy.copy(frame)
    frame_count += 1

    # 前フレームと比較するために白黒に変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15, 15), 0)
    img_b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

    if not img_last is None:
        # 差分を得る
        frame_diff = cv2.absdiff(img_last, img_b)
        cnts = cv2.findContours(frame_diff,
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[0]
        # 差分領域に魚が映っているか調べる
        fish_count = 0
        for pt in cnts:
            # 1フレームに何箇所も同時に違いが現れると、現れた数だけ座標を得る
            x, y, w, h = cv2.boundingRect(pt)
            if w < 100 or w > 500:
                continue  # ノイズを除去
            # 抽出した領域に魚が映っているか確認
            imgex = frame[y:y + h, x:x + w]
            imagex = cv2.resize(imgex, (64, 32))
            image_data = imagex.reshape(-1, )
            pred_y = clf.predict([image_data])

            if pred_y[0] == 1:
                fish_count += 1
                cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 魚が映っているか？
        # 魚が三匹以上写っているか判断する
        if fish_count > fish_th:
            # bestshotフォルダの/fish+count.jpg形式で保存する
            fname = output_dir + "/fish" + str(count) + ".jpg"
            cv2.imwrite(fname, frame)
            count += 1

    cv2.imshow('FISH!', frame2)
    if cv2.waitKey(1) == 13:
        break
    img_last = img_b

cap.release()
cv2.destroyAllWindows()
print("ok", count, "/", frame_count)
