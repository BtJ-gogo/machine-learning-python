# Instractions  
URL: [https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/book-recommendation-engine-using-knn](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/book-recommendation-engine-using-knn)  
このプロジェクトは Google Colaboratory で作業します。

そのリンクにアクセスした後、自分のアカウントまたはローカルにノートブックのコピーを作成してください。プロジェクトが完了し、テスト（リンクに含まれています）に合格したら、プロジェクトのリンクを以下に提出してください。Google Colaboratory のリンクを提出する場合は、「リンクを知っている全員がアクセスできるように」リンクの共有設定をオンにすることを忘れないでください。

現在、機械学習カリキュラムの対話型教材は開発中です。そのため、認証のビデオチャレンジを通じて進めることができます。また、実際のプロジェクトに取り組む際と同様に、追加の学習リソースを探す必要があるかもしれません。

このチャレンジでは、K-Nearest Neighbors を使用して書籍推薦アルゴリズムを作成します。

使用するのは Book-Crossings データセットです。このデータセットには、90,000人のユーザーによる270,000冊の書籍に対する1.1百万件の評価（1〜10のスケール）が含まれています。

データをインポートしてクリーンアップした後、`sklearn.neighbors` の NearestNeighbors を使用して、指定された書籍に似た書籍を表示するモデルを開発します。Nearest Neighbors アルゴリズムは、インスタンスの「近さ」を判断するために距離を測定します。

`get_recommends` という名前の関数を作成し、引数として書籍タイトル（データセットから）を取り、その書籍に似た5冊の書籍とその距離をリストで返すようにします。

このコード：

```python
get_recommends("The Queen of the Damned (Vampire Chronicles (Paperback))")
```

は、以下のような結果を返すべきです：

```python
[
  'The Queen of the Damned (Vampire Chronicles (Paperback))',
  [
    ['Catch 22', 0.793983519077301],
    ['The Witching Hour (Lives of the Mayfair Witches)', 0.7448656558990479],
    ['Interview with the Vampire', 0.7345068454742432],
    ['The Tale of the Body Thief (Vampire Chronicles (Paperback))', 0.5376338362693787],
    ['The Vampire Lestat (Vampire Chronicles, Book II)', 0.5178412199020386]
  ]
]
```

`get_recommends()` から返されるデータはリストです。リストの最初の要素は、関数に渡された書籍タイトルです。リストの2番目の要素は、5冊の書籍とその距離を含むリストです。各サブリストには、推薦された書籍と、関数に渡された書籍からその推薦された書籍までの距離が含まれています。

データセットをグラフ化すると（オプション）、多くの書籍が頻繁に評価されていないことに気付くでしょう。統計的有意性を確保するために、200件未満の評価を持つユーザーと100件未満の評価を持つ書籍はデータセットから削除してください。

最初の3つのセルには、必要なライブラリのインポートとデータのロードが含まれています。最後のセルはテスト用です。これらのセルの間にすべてのコードを書いてください。
