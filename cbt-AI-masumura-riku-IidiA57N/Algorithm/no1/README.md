# 問1 アルゴリズムの基本問題

以下の問題に対する答えをyamlファイルに記載してください。

## Section 1
---

#### データ構造に関する次の記述のうち、正しいものにはTを、正しくないものにはFを答えよ。

A. 要素xを配列の最後尾に追加するときの平均時間計算量は ![O(1)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%281%29) である。

B. 要素xを配列の特定の要素の直後に挿入するときの平均時間計算量は ![O(N)](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+O%28N%29) である。ただし、特定の要素のメモリ上の位置は既知であるとする。

C. 要素xを連結リストの最後尾に追加するときの平均時間計算量は ![O(1)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%281%29) である。ただし、連結リストの末尾の要素のメモリ上の位置は不明であるとする。

D. 要素xを連結リストの特定の要素の直後に挿入するときの平均時間計算量は ![O(N)](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+O%28N%29) である。ただし、特定の要素のメモリ上の位置は既知であるとする。

E. 配列の中に特定の要素が含まれるか探索するときの平均時間計算量は ![O(1)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%281%29) である。

F. set(集合)の中に特定の要素が含まれるか探索するときの平均時間計算量は ![O(N)](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+O%28N%29) である。

G. 平衡二分探索木の中に特定の要素が含まれるか探索するときの平均時間計算量は ![O(\log N)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%28%5Clog+N%29) である。

H. 配列の中の最大値(最小値)を探索するときの平均時間計算量は ![O(N \log N)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%28N+%5Clog+N%29) である。

<br>

## Section 2
---

次のpythonコードはintからなる配列Lの要素を**昇順**に並べ替えるものである。これを踏まえて以下の問いに答えよ。
```
N = len(L)
for i in range(N-1):
    for j in range(N-1, i, -1):
        if L[j] < L[j-1]:
            L[j], L[j-1] = L[j-1], L[j]
```

<br>

#### Q1: このソートアルゴリズムの名称として最も適切なものを1つ選べ.

A. クイックソート

B. マージソート

C. バブルソート

D. シェルソート

<br>

#### Q2: このソートアルゴリズムを用いると、1回のソートにおいて![L_{j}](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+L_%7Bj%7D)と![L_{j-1}](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+L_%7Bj-1%7D)は何回比較が行われるか。最も適切なものを1つ選べ。

A. ![N^2](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+N%5E2)

B. ![N \log N](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+N+%5Clog+N)

C. ![N^2 + N](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+N%5E2+%2B+N)

D. ![\dfrac{N^2 - N}{2}](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+%5Cdfrac%7BN%5E2+-+N%7D%7B2%7D)

<br>

#### Q3: 昇順にソートするとき、要素間（![L_{j}](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+L_%7Bj%7D)と![L_{j-1}](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+L_%7Bj-1%7D)）の交換が最も多くなると考えられる配列の初期状態として、最も適切なものを1つ選べ。

A. 昇順に並んでいる

B. 降順に並んでいる

C. 配列の真ん中の要素までは降順で、それ以降は昇順に並んでいる

D. 配列の真ん中の要素までは昇順で、それ以降は降順に並んでいる

<br>

#### Q4: このソートアルゴリズムの平均計算時間として最も適切なものを1つずつ選べ.

A. ![O(1)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%281%29)

B. ![O(N)](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+O%28N%29)

C. ![O(N \log N)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%28N+%5Clog+N%29)

D. ![O(N^2)](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+O%28N%5E2%29)

<br>

#### Q5: このソートアルゴリズムを、要素の入れ替えが発生しなくなった時点で処理を打ち切るように改良した。そのとき、最良の場合の計算時間として最も適切なものを1つ選べ。

A. ![O(1)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%281%29)

B. ![O(N)](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+O%28N%29)

C. ![O(N \log N)](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+O%28N+%5Clog+N%29)

D. ![O(N^2)](https://render.githubusercontent.com/render/math?math=%5Ctextstyle+O%28N%5E2%29)

<br>