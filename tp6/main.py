import column
import grid
import pawn

print("Exerxice 1 :")

c=column.Column(4)
print(c)

print("Exerxice 2 :")

c.drop(pawn.Pawn("X"))
c.drop(pawn.Pawn("O"))
c.drop(pawn.Pawn("X"))

print("Exerxice 3 :")

g=grid.Grid(4,3)
p1=pawn.Pawn('X')
g.drop(2,p1)


