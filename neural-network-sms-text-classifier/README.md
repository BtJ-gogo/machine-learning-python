# Instractions  
URL: [https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/neural-network-sms-text-classifier](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/neural-network-sms-text-classifier)  

こちらのプロジェクトはGoogle Colaboratoryを使用して進めます。

リンクにアクセスした後、ご自身のアカウントかローカルにノートブックのコピーを作成してください。プロジェクトを完了し、テスト（リンクに含まれています）に合格したら、以下にプロジェクトのリンクを提出してください。Google Colaboratoryのリンクを提出する場合は、「リンクを知っている全員」に対してリンク共有をオンにしてください。

現在、機械学習カリキュラムのインタラクティブな教材を開発中です。現時点では、この認定のビデオチャレンジに取り組んでください。また、実際のプロジェクトに取り組むときと同様に、追加の学習リソースを探す必要があるかもしれません。

---

このチャレンジでは、SMSメッセージを「ham」または「spam」として分類する機械学習モデルを作成する必要があります。「ham」メッセージは友人から送られた通常のメッセージです。「spam」メッセージは広告や企業から送られるメッセージです。

`predict_message`という関数を作成してください。この関数はメッセージの文字列を引数として受け取り、リストを返します。リストの最初の要素は「ham」（0）または「spam」（1）の可能性を示す0から1の間の数値で、リストの2番目の要素は最も可能性の高い「ham」または「spam」という単語になります。

このチャレンジでは、SMS Spam Collectionデータセットを使用します。このデータセットはすでにトレーニングデータとテストデータに分けられています。

最初の2つのセルはライブラリとデータをインポートします。最後のセルはモデルと関数をテストします。これらのセルの間にコードを追加してください。
