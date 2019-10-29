

## モデル生成
`python -m demo --img_path data/coco1.png`
プレースホルダの作成とかがかなり深い階層にいっちゃってるので、
わざわざそれ用のコードを書かずに流用するため、学習済みモデルの実行と同時にモデルの出力を行うようにしています。

`models/savedModel`にsavedModel形式のファイルが出力されます。


## モデル変換
`tensorflowjs_converter --input_format=tf_saved_model --output_node_names='joints,verts,cams,joints3d,theta' --saved_model_tags=serve --quantization_bytes=1  "./models/savedModel" "./tfjs/1byte"`


まだ下記エラーが解決できていない。
```
Converted 283 variables to const ops.
Unsupported Ops in the model
MatrixDiag, ScatterNd, BatchMatMul
```

ScatterNdとBatchMatMulはモジュールのバージョンをあげたらいけた

tensorflowjs=0.8.0
numpy==1.16.0
keras==1.1.0
matrixdiagが解決できない

ここ参考にしたらいけそう
https://medium.com/@spspspspsps/tfjs-converter-tips-matrixdiag-parseexample-7ac8db41cfd

tf.eye()を置き換える
tf.constant([[1, 0, 0], [0, -1, 0], [0, 0, -1]])

置き換えたあと、ちゃんとモデル生成し直すこと

こんなエラーがでた
ValueError: numpy.ufunc size changed, may indicate binary incompatibility. Expected 216 from C header, got 192 from PyObject

numpyのバージョンが合わないと出るらしい




書き出しできた！読み込めるか？
