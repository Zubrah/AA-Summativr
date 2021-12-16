
from collections import defaultdict

# import heap
import heapq


#define shortest path function
def shortest_path(S, N, G):
    D    = {}
    H    = [(0, S)]

    for n in range(1, N + 1):
        D[n] = float('inf')

    D[S] = 0

    # loop through all nodes
    while H:
        t = heapq.heappop(H)
        for h in G[t[1]]:
            if D[h[0]] > D[t[1]] + h[1]:
                D[h[0]] = D[t[1]] + h[1]
                if (h[1], h[0]) in H:
                    H.remove((h[1], h[0]))
                    heapq.heapify(H)
                heapq.heappush(H, (D[h[0]], h[0]))

    return D

#define main function
def main():
    T = int(input())

    #loop through inputs and strip
    for _ in range(T):
        N, M = [int(i) for i in input().split()]

        G    = defaultdict(set)

        for _ in range(M):
            e = [int(i) for i in input().split()]
            G[e[0]].add((e[1], e[2]))
            G[e[1]].add((e[0], e[2]))

        S    = int(input())

        # assign shortest_path function to D
        D    = shortest_path(S, N, G)
        print(' '.join(str(D[n]) if D[n] != float('inf') else '-1' for n in range(1, N + 1) if n != S))


if __name__ == "__main__":
    main()
    
    
    
    
    """
    Test Values :
    1
    4 4
    1 2 24
    1 4 20
    3 1 3
    4 3 12
    1
    Answer  : 24 3 15
    
    Second test values: 
    1
    5 3
    1 2 10
    1 3 6
    2 4 8
    2
    Answer : 10 16 8 -1
    """