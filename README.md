# 正多角形の面積一覧

## このソフトの存在意義

第二回ロボットシステム学の課題として製作したプログラムです

正3角形から順に正多角形を計算し、一覧としてみることができます。

また、しばらく放置することにより円に近い面積も見ることが出来る


## 使用方法

	ros2 launch mypkg talk_listen.launch.py

をターミナルに打つことによって正多角形の面積が連続的に出力される

listener.py の中の

	a = 1

は外接円の半径をさしているため、これを変更するによって外接円の半径も変更できる


## 必要なソフトウェア

・Python


・ROS2


## テスト環境
　
　・ubuntu

## ライセンス

このソフトパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

© 2025 Makusa Ushu


## 参考及び権利関係

このパッケージのコードは、下記のスライド
- [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025) （© 2025 Ryuichi Ueda）
のものをを、本人の許可を得て自身の著作としたものです
