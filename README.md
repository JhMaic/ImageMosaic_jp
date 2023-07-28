## インストール
```shell
pip install Pillow==9.4.0 easyocr
```

## モデル説明
### カスケード分類器
#### 一言紹介
`xml`を訓練して
`cv2.CascadeClassifier(xmlPath)`として使う

#### 調整可能なパラメーターは
- `scaleFactor` 検出された四角形のスケール率
- `minNeighbors` 信頼度（0, 1, 2, ...）
- `minSize` 検出する最小のサイズ

#### 利用場面
> 独自でxml訓練すればどこでも使える。
> 
>opencvがいくつのxmlを提供している.
> ``https://github.com/opencv/opencv/tree/master/data/haarcascades``

### easyOCR
#### 一言紹介
**深層学習**による文字検出器, pytorchが使われる。

商用可能ライセンス。