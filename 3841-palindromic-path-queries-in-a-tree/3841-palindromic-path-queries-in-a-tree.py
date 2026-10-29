import sys

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # 1. Build Adjacency List
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Iterative DFS for Euler Tour (tin/tout) and Binary Lifting
        # Using a stack to prevent recursion depth issues in deep trees
        LOG = 20
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        
        timer = 0
        current_mask = [1 << (ord(c) - ord('a')) for c in s]
        initial_xor = [0] * n
        
        # Stack entries: (node, parent, state) 
        # state: 0 = entering, 1 = exploring children
        stack = [(0, 0, 0)]
        children_iter = [iter(adj[i]) for i in range(n)]
        
        while stack:
            u, p, state = stack[-1]
            if state == 0:
                timer += 1
                tin[u] = timer
                up[u] = up[p].copy() if u != 0 else [0] * LOG
                if u != 0:
                    up[u] = up[p][:]
                # Update binary lifting transitions
                for i in range(1, LOG):
                    up[u] = [0] * LOG # Re-instantiating inside logic safely:
                
                # Inline standard sparse table calculation
                up[u] = [0] * LOG
                up[u][0] = p
                for i in range(1, LOG):
                    up[u][i] = up[up[u][i-1]][i-1]
                
                initial_xor[u] = (initial_xor[p] if u != 0 else 0) ^ current_mask[u]
                
                # Change state to child processing
                stack[-1] = (u, p, 1)
            else:
                try:
                    v = next(children_iter[u])
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
                except StopIteration:
                    tout[u] = timer
                    stack.pop()

        # 3. Binary Indexed Tree (Fenwick Tree) for Range XOR
        bit = [0] * (n + 2)
        
        def update_bit(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query_bit(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # Initialize the BIT with the prefix XOR difference array values
        for i in range(n):
            # Simulated range update equivalent to giving `tin[i]` its value
            update_bit(tin[i], initial_xor[i])
            update_bit(tin[i] + 1, initial_xor[i])

        # 4. Lowest Common Ancestor (LCA) via Binary Lifting
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            # Lift u to the same depth as v
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            # Lift both together
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # 5. Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                
                old_m = current_mask[u]
                new_m = 1 << (ord(c) - ord('a'))
                diff = old_m ^ new_m
                current_mask[u] = new_m
                
                # Apply XOR update over u's entire subtree range
                update_bit(tin[u], diff)
                update_bit(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                
                lca = get_lca(u, v)
                mask_u = query_bit(tin[u])
                mask_v = query_bit(tin[v])
                
                # The XOR sum of paths from u to v
                path_mask = mask_u ^ mask_v ^ current_mask[lca]
                
                # Palindrome check: at most one bit set to 1
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
                
        return ans
