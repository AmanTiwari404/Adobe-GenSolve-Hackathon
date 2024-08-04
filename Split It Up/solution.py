from collections import defaultdict

def min_difference(n, A, B):
    # Create adjacency list for the tree
    adj = defaultdict(list)
    for u, v in zip(A, B):
        adj[u].append(v)
        adj[v].append(u)
    
    total_sum = n * (n + 1) // 2
    min_diff = float('inf')
    subtree_sum = [0] * (n + 1)
    
    def dfs(node, parent):
        nonlocal min_diff
        curr_sum = node
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            curr_sum += dfs(neighbor, node)
        
        subtree_sum[node] = curr_sum
        diff = abs(total_sum - 2 * curr_sum)
        min_diff = min(min_diff, diff)
        return curr_sum
    
    # Start DFS from node 1 (assuming 1-indexed nodes)
    dfs(1, -1)
    
    return min_diff

# Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end="")
        print()


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())

        A = []
        B = []

        for i in range(n - 1):
            a, b = map(int, input().split())
            A += [a]
            B += [b]

        obj = Solution()
        res = obj.MinDiff(n, A, B)

        print(res)
# Driver Code Ends
