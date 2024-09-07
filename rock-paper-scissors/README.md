# Instractions  
URL: [https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors)  

じゃんけん
このチャレンジでは、じゃんけんをするプログラムを作成します。ランダムに選択するプログラムは、通常 50% の確率で勝ちます。このチャレンジに合格するには、プログラムが 4 つの異なるボットと対戦し、各対戦で少なくとも 60% のゲームに勝つ必要があります。

このプロジェクトでは、Gitpod スターター コードを使用します。

機械学習カリキュラムのインタラクティブな指導部分はまだ開発中です。今のところ、このチャレンジに合格する方法を学ぶには、他のリソースを使用する必要があります。

---

[RPS.py](http://rps.py/) ファイルには、player という関数が用意されています。この関数は、対戦相手の最後の動きを表す文字列 ("R"、"P"、または "S") を引数として受け取ります。この関数は、次に実行する動きを表す文字列 ("R"、"P"、または "S") を返す必要があります。

player 関数は、前のプレイがないため、試合の最初のゲームでは引数として空の文字列を受け取ります。

[RPS.py](http://rps.py/) ファイルには、更新する必要がある関数の例が示されています。この関数の例は、2 つの引数 

(player(prev_play, target_history = [])) で定義されています。この関数は 2 番目の引数で呼び出されることはないため、1 つは完全にオプションです。

この関数の例に 2 番目の引数 (opponent_history = []) が含まれているのは、それが player 関数の連続呼び出し間で状態を保存する唯一の方法だからです。 versus target_history を追跡したい場合にのみ、引数が必要です。

ヒント: 4 人の対戦相手全員を倒すには、対戦相手のプレイに応じて変化する複数の戦略をプログラムに用意する必要があります。

### 開発

RPS_game.py を変更しないでください。すべてのコードを [RPS.py](http://rps.py/) に記述します。開発では、[main.py](http://main.py/) を使用してコードをテストできます。

[main.py](http://main.py/) は、RPS_game.py からゲーム関数とボットをインポートします。

コードをテストするには、play 関数を使用してゲームをプレイします。play 関数は、次の 4 つの引数を取ります:

- 対戦する 2 人のプレイヤー (プレイヤーは実際には関数です)
- 試合でプレイするゲームの数
- 各ゲームのログを表示するためのオプションの引数。これらのメッセージを表示するには、これを True に設定します。

```python
play(player1, player2, num_games[, verbose])
```

たとえば、player と quincy が互いに 1000 ゲームをプレイし、各ゲームの結果を確認したい場合は、次のように関数を呼び出します:

```python
play(player, quincy, 1000, verbose=True)
```

### テスト

このプロジェクトの単体テストは test_module.py にあります。利便性のために、test_module.py から [main.py](http://main.py/) にテストをインポートしました。[main.py](http://main.py/) の最後の行のコメントを解除すると、コンソールで python [main.py](http://main.py/) を実行するたびにテストが自動的に実行されます。

### 送信

プロジェクトの URL をコピーして、freeCodeCamp に送信します。
