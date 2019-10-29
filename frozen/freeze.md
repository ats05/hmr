


実行したいコマンド
```
bazel-bin/tensorflow/python/tools/freeze_graph --input_graph=../models/savedModel/savedModel.pb --input_checkpoint=../models/model --output_graph=./frozenModel --output_node_names='joints,verts,cams,joints3d,theta'
```

まずbazelが必要になるらしい
```
$ brew tap bazelbuild/tap
$ brew install bazelbuild/tap/bazel
```
bazelでfreeze_graphをビルド
```
$ git clone https://github.com/tensorflow/tensorflow.git
$ cd tensorflow
$ bazel build tensorflow/python/tools:freeze_graph
```

sixが入ってないとエラー。入ってるはずなのに。
anaconda環境だから？
```
ModuleNotFoundError: No module named 'six'
```

bash（fish）がデフォルトで見にいくpython環境に対してインストールしたらいけた
自分の環境ではpip→anaconda環境 pip3→デフォルト環境　になってる（っぽい）
```
$ pip3 install six
```

次のエラー
```
ERROR: missing input file '@local_config_git//:gen/head':/private/var/tmp/_bazel_xxx/43a4dd70c569cbc7c94448fcd8697faf/external/local_config_git/gen/head (No such file or directory)

```
