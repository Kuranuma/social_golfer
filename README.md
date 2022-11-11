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
      2 C J D F
      2 K L G H
      3 A C K G
      3 B L D E
      3 I J F H
      4 A K D F
      4 B I C G
      4 J L E H
      5 A J E G
      5 B C L F
      5 I K D H
      6 A F I L
      6 B J D G
      6 C K E H
      7 A B H J
      7 C D E I
      7 K L F G
      8 A C L H
      8 B E F K
      8 I J D G
