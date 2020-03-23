

`wget https://people.eecs.berkeley.edu/~kanazawa/cachedir/hmr/neutral_smpl_mean_params.h5`
上記を`hmr/models/`に入れる


各種画像セットをダウンロード

mobilenetをダウンロード
`./tf-models`

moshをダウンロード
`./neutrMosh`


`src/do_train.sh`の`PRETRAINED`を、mobilenetの`.ckpt`ファイルに書き換える

データ保存場所を作る
`mkdir ~/hmr/prepared_datasets/`

`prepare_datasets.sh`の`DATA_DIR`を、上記のディレクトリのパスに修正
`prepare_datasets.sh`のいらない行を削除

`sh prepare_datasets.sh`


mobilenetがなかったので、tensorflow 15.0に更新してやってみる


https://github.com/tensorflow/models/tree/master/research
これをsite-packagesのとこにいれなきゃいけない？

git clone git@github.com:tensorflow/models.git research_models

models.pyに`sys.path.append("research_models/research/slim/nets")`を追加

だめだった

`research_models/research/slim/setup.py`を実行
`python setup.py build`
`python setup.py install`

だめ


git@github.com:tensorflow/models.gitを直にsite-packagesの下のところに突っ込んでみる
`python setup.py build`
`python setup.py install`

だめっぽい

https://setuptools.readthedocs.io/en/latest/easy_install.html


環境からリセットしてみる
3.6系にして、tensorflow/modelsを入れる

research modelsがtf2.0用になってたので、合わせる
`git checkout -b v1.12.0 refs/tags/v1.12.0`

`threed_fn = Encoder_fc3_dropout`
にたどり着くようif文を除去

はじまったっぽい


ライセンスについて考えないと、、、
https://github.com/akanazawa/hmr/blob/master/doc/train.md

- COCO : 商用NG
- LSP : 書いてないから調べる
- LSPex :
- mpii : 商用ダメかも
- mpi 3d: 商用NG
- mosh : そもそもいらないかも


商用利用可能で代用できそうなものを探す

参考
- https://github.com/arXivTimes/arXivTimes/tree/master/datasets
- https://datasetsearch.research.google.com/search?query=3D

調べる
- https://storage.googleapis.com/openimages/web/index.html
- http://www.aisl.cs.tut.ac.jp/database_HDIBPL.html
- http://rpg.ifi.uzh.ch/davis_data.html
- http://dfaust.is.tue.mpg.de/
- http://humaneva.is.tue.mpg.de/ : だめ
