# Anything_judge_video

## 日本語
### 使い方について説明します。
#### 初めに
筆者は魚かどうかを判断して写真として抜き出してるので、ファイル名がfish~となっていますが、魚ではなくても構いません。判別したい物体が写っている動画を用意していただいても大丈夫です。
+ 書き換え部分については、以下で説明します。

### 用意する物
ここでは魚が写っている海の動画ファイル

1. fishvideo_extract_diff.pyを実行
 + ここで、動画に一定以上の動きのあった部分を全てexfishフォルダに.jpgで抜き出している。パラメータで動く量を調整可能

2. fishフォルダと、nofishフォルダを作成する
 + なぜfishとnofishかというと、fish_train.pyの方で、そのディレクトリを指定しているからである。
    よって、そこのディレクトリ名を書き換えれば、fishやnofishの名前でなくても良い

3. exfishフォルダから、nofish(魚が写っていない部分)とfish(魚が写っている部分)に仕分けを行う
 + 次のモデル作成で、使用する為。

4. fish_train.pyを実行する。
 + ランダムフォレストで、簡易的な学習を行っている。実行後、fish.pklファイル(モデルをファイルとして保存)を作成している。

5. fishvideo_find.pyを実行する
 + bestshotフォルダが作成され、そこに動画に現れた魚の写真が保存されていく
    10行目で、魚が何匹写っている時に保存する値であり、1だと精度がやや劣るので、2に設定しておく

以上の工程で判機を実行できる。
是非、全く別のジャンルの動画でも試してもらいたい。

## English

### Instructions on how to use it.
#### Introduction.
The file name is "fish~" because I'm trying to determine if it's a fish or not, but it doesn't have to be a fish. You can also provide a video of the object you want to identify.
+ You can also prepare a movie of the object you want to identify.

### What you need to prepare.
Here's a video file of the ocean with fish

Run fishvideo_extract_diff.py
 + Here, all the parts of the video that had more than a certain amount of movement are extracted as a .jpg in the exfish folder. You can adjust the amount of movement with parameters

2. create a fish folder and a nofish folder
 + The reason why fish and nofish are so important is that fish_train.py specifies the directory in fish_train.py, so you don't have to rename it fish or nofish.
    So, if you change the name of the directory, it doesn't have to be fish or nofish

3. divide a folder into nofish and fish in the exfish folder.
 + Run fish_train.py for use in the following model creation. 4.

4. run fish_train.py.
 + The random forest is used for simple training. After running it, it creates a fish.pkl file (the model is saved as a file). 5.

5. run fishvideo_find.py
 + bestshot folder will be created and the pictures of the fish that appeared in the video will be saved in it
    In the tenth line, this is the value to be saved when the number of fishes are in the picture, and since 1 is slightly less accurate, it should be set to 2.

The above process allows you to run the sealer.
I'd like you to try it with a completely different kind of video.

![pic-1](https://i.gyazo.com/974dafe7ae4773259524df7a7ec4ce7e.png)
