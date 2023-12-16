import sys
from typing import str
def Input():
    try :
        sys.stdin = open('A.inp', 'r')
        sys.stdout = open('A.out', 'w')
    except :
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
def Solve():
    senate = list(input())
    lensenate = len(senate)
    def hendle(lensenate,senate):
        for i in range(lensenate):
            for j in range(i, lensenate):
                if senate[i] != senate[j]:
                    del senate[j]
                    lensenate = len(senate)
    def predisctpartyvictory(senate: str)-> str:
            setnate = set(senate)
            hendle(lensenate,senate)
            if len(setnate) == 1:
                if setnate[0] == "D":
                    print("Dire")
                else:
                    print("Radiant") 
            else:
                return predisctpartyvictory(senate)
    
def main():
    Input()
    Solve()
if __name__ == '__main__':
    main()