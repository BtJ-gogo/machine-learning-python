# Instractions  
URL: [https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/linear-regression-health-costs-calculator](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/linear-regression-health-costs-calculator)  
このプロジェクトは Google Colaboratory で作業を行います。

指定されたリンクにアクセスした後、自分のアカウントまたはローカルにノートブックのコピーを作成してください。プロジェクトが完了し、テストに合格したら、プロジェクトリンクを以下に提出してください。Google Colaboratory のリンクを提出する場合は、「リンクを知っているすべての人がアクセスできる」ようにリンク共有を有効にしてください。

現在、機械学習カリキュラムのインタラクティブな教育コンテンツを開発中です。それまでの間、この認証のビデオチャレンジを通じて学習を進めることができます。また、実際のプロジェクトで行うように、追加の学習リソースを探す必要があるかもしれません。

---

このチャレンジでは、回帰アルゴリズムを使用して医療費を予測します。

医療費に関する情報を含む異なる人々のデータセットが提供されます。このデータを使用して、新しいデータに基づいて医療費を予測します。

ノートブックの最初の2つのセルでは、ライブラリとデータのインポートを行います。

カテゴリカルデータを数値に変換してください。データの80%をトレーニングデータセット（train_dataset）として使用し、20%をテストデータセット（test_dataset）として使用してください。

これらのデータセットから「expenses」列を取り除き、train_labels および test_labels という新しいデータセットを作成します。モデルのトレーニング時にこれらのラベルを使用します。

モデルを作成し、train_dataset でトレーニングしてください。ノートブックの最後のセルを実行して、モデルを確認します。最後のセルでは、見えない test_dataset を使用してモデルの一般化性能をチェックします。

チャレンジに合格するためには、model.evaluate が 3500 未満の平均絶対誤差 (Mean Absolute Error) を返す必要があります。つまり、医療費を $3500 以内で正確に予測できることが求められます。

最後のセルでは、test_dataset を使用して医療費を予測し、結果をグラフで表示します。
