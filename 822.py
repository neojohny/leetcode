# this is a default code for 822
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad=set([a for a,b in zip(fronts,backs) if a==b])
        return min([el for el in fronts+backs if el not in bad],default=0)