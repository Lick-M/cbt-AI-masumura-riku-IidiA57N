# 問3 条件を満たす数の集合

実行時間制限：2 sec / メモリ制限：1024 MB

一桁または任意の隣り合う二つの桁の数の差が4であるような正の整数全体の集合を考える。
![N](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+N)個の数字が与えられるので、それぞれ与えられた数以下のこの集合の要素の個数をそれぞれ出力してください。
ただし、main.pyはPEP8に準拠するように準拠するように書いてください。


## 制約
 - 入力は全て整数
 - ![1 \leq N \leq 10^5](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+1+%5Cleq+N+%5Cleq+10%5E5)
 - ![1 \leq a_i \leq 10^{30}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+1+%5Cleq+a_i+%5Cleq+10%5E%7B30%7D)

## 入力
入力は以下の形式で標準入力から与えられます。
> ![N](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+N) <br>
> ![a_1](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+a_1) <br>
> ![a_2](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+a_2) <br>
> ... <br>
> ![a_n](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+a_n) <br>

## 出力

それぞれの![a_i(i=1,2,\ldots,N)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+a_i%28i%3D1%2C2%2C%5Cldots%2CN%29)の入力に対して答えを![N](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+N)行出力してください。

## 入力例1
> 2 <br>
> 5 <br>
> 15 <br>
## 出力例1
> 5 <br>
> 10 <br>

[1, 2, 3, 4, 5, 6, 7, 8, 9, 15]

15以下で条件を満たす数のリストは上記の通りなので、5以下の数で条件を満たすものの個数は5個、15以下の数で条件を満たすものの個数は10個です。

## 入力例2
> 3 <br>
> 1000 <br>
> 1000000 <br>
> 1000000000
## 出力例2
> 34 <br>
> 108 <br>
> 296 <br>

