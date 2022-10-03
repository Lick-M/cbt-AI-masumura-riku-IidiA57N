def main():
    N = int(input())
    a = [int(input()) for _ in range(N)] #(N,1)行列を(1,N)行列に変換

    l = [int(x) for x in list(str(a))] #aの各桁をリストに格納
    len (l) <= 30 #桁数の上限は30桁
    
    set = [] #集合の定義
    for i in range (1, 10 ** 30): #1～10*30までの範囲指定
        if 1<=i<=9: #一桁であれば集合の要素に追加する
            set.add(i)
    for x in range (1,9):
        if (x-(x+1)==4) or (x-(x+1)==-4) : #隣接する二つの桁の数の差が4であれば，集合の要素に追加する
            set.add(i)

    for a in range(N):
        len (set)


if __name__ == '__main__':
    main()