import sys


input = sys.stdin.readline

def init(arr, tree, idx2node, node, start, end):
    if start == end:
        tree[node] = arr[start]
        idx2node[start] = node # bottom-up 방식으로 update할 때 사용
        return tree[node]
    else:
        mid = (start+end)//2
        lsum = init(arr, tree, idx2node, node*2, start, mid)
        rsum = init(arr, tree, idx2node, node*2+1, mid+1, end)
        tree[node] = lsum + rsum
    return tree[node]

def query(tree, node, start, end, left, right):
    # LSER
    if left <= start and end <= right:
        return tree[node]
    # SELR or LRSE
    if end < left or right < start:
        return 0
    
    mid = (start+end)//2
    lsum = query(tree, node*2, start, mid, left, right)
    rsum = query(tree, node*2+1, mid+1, end, left, right)
    return lsum + rsum

def update(tree, node, value):
    diff = value - tree[node]
    while node > 0:
        tree[node] += diff
        node //= 2

# main
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [0] * (4 * n)
idx2node = [0] * n
init(arr, tree, idx2node, 1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(tree, idx2node[b-1], c)
    elif a == 2:
        print(query(tree, 1, 0, n-1, b-1, c-1))