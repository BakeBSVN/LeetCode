from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set1,set2 = map(set,zip(*paths))
        print("".join(list(set2 - set1)))
def main():
    x = Solution()
    x.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
if __name__ == '__main__':
    main()