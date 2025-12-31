# 正多角形の面積一覧

# このソフトの存在意義

第二回ロボットシステム学の課題として製作したプログラムです

正3角形から順に正多角形を計算し、一覧としてみることができます。

また、しばらく放置することにより円に近い面積も見ることが出来る


# 使用方法

	ros2 launch mypkg talk_listen.launch.py

をターミナルに打つことによって正多角形の面積が連続的に出力される

listener.py の中の

	a = 1

は外接円の半径をさしているため、これを変更するによって外接円の半径も変更できる


# 必要なソフトウェア

・Python


・ROS2


# テスト環境
　
　・ubuntu

# ライセンス

このソフトパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

© 2025 Makusa Ushu


# 参考及び権利関係

このパッケージのコードは、下記のスライド
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson1.html#4
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson2.html#6
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson3.html#4
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson5.html#23
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson6.html#1
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson7.html#1
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson8.html#29
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson9.html#6
https://ryuichiueda.github.io/slides_marp/robosys2025/lesson10.html#6
を参考に自作したものをです
