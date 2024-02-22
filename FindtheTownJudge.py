import sys
from typing import List
def Input():
    try :
        sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    class Solution:
        def findJudge(self, n: int, trust: List[List[int]]) -> int:
            n=int(input())
            trust=input()[2:-2].split('],[')
            trust_him=[1]*(n+1)
            he_trust=[1]*(n+1)
            for i in trust:
                if i=='': break
                i,j=map(int, i.split(','))
                trust_him[j]+=1
                he_trust[i]=0
                ans=-1
            for i in range(1,n+1):
                if he_trust[i] and trust_him[i]==n:
                    ans= i
            print(ans)
def main():
    # Input()
    Solve()
if __name__ == '__main__':
    main()