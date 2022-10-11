# social_golfer
ソーシャル・ゴルファー問題

指定されたグループ人数、グループ数、組み合わせ回数から、参加者の組み合わせの重複回数が均等になるようにグルーピングします。

## 使い方
`python social_golfer.py [グループ人数] [グループ数] [回数]`  
例：4人麻雀を3グループ(12人)作り、それを8回行う場合  
`python social_golfer.py 4 3 8`

## 出力例
スペース区切りで以下のように出力されます。  
`[組み合わせ回数][参加者][参加者]...`  
参加者はアルファベットで表記されます。  

    > python social_golfer.py 4 3 8
    グループ人数:4
    グループ数:3
    回数:8
      1 A B C D
      1 E F G H
      1 I J K L
      2 A I B E
      2 C J F G
      2 L K D H
      3 A B J H
      3 C E K L
      3 I D F G
      4 A C K F
      4 B L G H
      4 I J D E
      5 A C H I
      5 B K E F
      5 L J D G
      6 A L D F
      6 B G I K
      6 J C E H
      7 A L E G
      7 B I F H
      7 K J C D
      8 A J K G
      8 B C F L
      8 I D E H