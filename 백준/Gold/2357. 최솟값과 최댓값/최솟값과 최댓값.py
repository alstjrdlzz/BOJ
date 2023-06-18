import sys


input = sys.stdin.readline

def min_init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start+end)//2
        lmin = min_init(arr, tree, node*2, start, mid)
        rmin = min_init(arr, tree, node*2+1, mid+1, end)
        tree[node] = min(lmin, rmin)

    return tree[node]

def max_init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start+end)//2
        lmax = max_init(arr, tree, node*2, start, mid)
        rmax = max_init(arr, tree, node*2+1, mid+1, end)
        tree[node] = max(lmax, rmax)
        
    return tree[node]

def min_query(tree, node, start, end, left, right):
    # LSER
    if left <= start and end <= right:
        return tree[node]
    
    # SELR or LRSE
    if end < left or right < start:
        return 1e+9
    
    mid = (start+end)//2
    lmin = min_query(tree, node*2, start, mid, left, right)
    rmin = min_query(tree, node*2+1, mid+1, end, left, right)
    return min(lmin, rmin)
    
def max_query(tree, node, start, end, left, right):
    # LSER
    if left <= start and end <= right:
        return tree[node]
    
    # SELR or LRSE
    if end < left or right < start:
        return -1
    
    mid = (start+end)//2
    lmax = max_query(tree, node*2, start, mid, left, right)
    rmax = max_query(tree, node*2+1, mid+1, end, left, right)
    
    return max(lmax, rmax)

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree_size = 4*n
min_tree = [-1]*tree_size
max_tree = [-1]*tree_size

min_init(arr, min_tree, 1, 0, n-1)
max_init(arr, max_tree, 1, 0, n-1)

for _ in range(m):
    l, r = map(int, input().split())
    print(min_query(min_tree, 1, 0, n-1, l-1, r-1), max_query(max_tree, 1, 0, n-1, l-1, r-1))