
class Canavar:
    def __init__(N, Ai, Bi, Ci):
        self.No = N
        self.Ai = Ai
        self.Bi = Bi
        self.Ci = Ci



t = int(input())
N, D, Ai, Bi, Ci = []
for i in range(t):
  liste = input()
  xN, xD = map(int,liste.split())
  N.append(xN)
  D.append(xD)
  for i in range(N):
    liste = input()
    xAi, xBi, xCi = map(int,liste.split())
    Ai.append(xAi)
    Bi.append(xBi)
    Ci.append(xCi)


