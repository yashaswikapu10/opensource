N, X, Y = map(int, input().split())
if X % Y == 0 and X <= N * Y:
    print("YES")
else:
    print("NO")
