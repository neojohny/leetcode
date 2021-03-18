from collections import deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        if not seqs or seqs[0]==[]:
            return org == []
        seq_c = sum(seqs,[])
        if set(seq_c) != set(org):
            return False
        indeg = [0 for _ in org+[0]]
        indeg[0] = 100 # handing index 0
        neigh = [[] for _ in org+[0]]
        q = deque()

        for s in seqs:
            for i in range(len(s)-1):
                indeg[s[i+1]] += 1
                neigh[s[i]].append(s[i+1])

        q = deque([indeg.index(0)])
        toporder = []
        while q:
            #print(q)
            head = q.popleft()
            if len(q) > 0:
                return False

            toporder.append(head)
            for n in neigh[head]:
                indeg[n] -= 1
                if not indeg[n]:
                    q.append(n)
        return toporder == org