import cv2, os

img_last = None # 前回の画像
no = 0 # 画像の枚数
save_dir = "./exfish" # 保存ディレクトリ名
os.mkdir(save_dir) # ディレクトリを作成

# 動画ファイルから入力を開始
cap = cv2.VideoCapture("fish.mp4")
frame_diff = 0

while True:
    # 画像を取得
    is_ok, frame = cap.read()
    if not is_ok: break #frameがこれ以上ない時、即ち動画が終わった時
    frame = cv2.resize(frame, (1000, 800))

    # 白黒画像に変換 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (15, 15), 0)
    img_b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

    # 差分を確認する
    if not img_last is None:
        frame_diff = cv2.absdiff(img_last, img_b)
        cnts = cv2.findContours(frame_diff, 
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[0]

        # 差分があった領域をファイルに出力
        for pt in cnts:
            x, y, w, h = cv2.boundingRect(pt)
            if w < 100 or w > 500: continue # ノイズを除去

            # 抽出した領域を画像として保存
            imgex = frame[y:y+h, x:x+w]
            outfile = save_dir + "/" + str(no) + ".jpg"
            cv2.imwrite(outfile, imgex)
            no += 1
    img_last = img_b
print("ok")
