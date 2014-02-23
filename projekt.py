# vim:fileencoding=utf8:
from sympy import *
# Vi har to uafhængige variable x og y.
x, y = symbols('x y')
# Omregning mellem grader og radianer.
DEG = 180/pi

print("Opgave 1")
print("========\n")

def circle(x_0, y_0, r):
    return Eq(r**2, (x - x_0)**2 + (y - y_0)**2)

print("15^2 = x^2 + y^2")
print("")

print("Opgave 2")
print("========\n")

print("Cirklens ligning er:")
print(" r^2 = (x - x_0)^2 + (y - y_0)^2")
print("")

r = 10+15

print("Radius:")
print("   r = %s" % r)
print("")

a = {x:3, y:38}
b = {x:26, y:25}

print("De to givne punkter på cirklen er:")
print("   A = (%s, %s)" % (a[x], a[y]))
print("   B = (%s, %s)" % (b[x], b[y]))
print("")

# solve() returnerer en liste med to elementer [{x:x_1, y:y_1}, {x:x_2, y:y_2}]
# der angiver de to skæringer mellem cirklerne.
# filter() returnerer en liste med ét element [{x:x_0, y:y_0}]
# som er det skæringspunkt, vi er interesserede i.
# Notationen "o," pakker listen ud og henter elementet indeni.
o, = filter(lambda p: p[y] > a[y],
        solve((circle(a[x], a[y], r),
               circle(b[x], b[y], r))))

print("Ud fra dette bestemmes cirklens centrum, idet dette ligger over punktet A:")
print(" x_0 = %s = %s" % (o[x], N(o[x])))
print(" y_0 = %s = %s" % (o[y], N(o[y])))
print("")

print("Opgave 4")
print("========\n")

a_theta = atan2(a[y]-o[y], a[x]-o[x])
b_theta = atan2(b[y]-o[y], b[x]-o[x])

print("Vi beregner ∠A og ∠B vha. arctan:")
print("  ∠A = %s°" % N(a_theta%(2*pi)*DEG))
print("  ∠B = %s°" % N(b_theta%(2*pi)*DEG))
print("")

c_theta = a_theta + 91/DEG
c = {x: o[x] + r*cos(c_theta), y: o[y] + r*sin(c_theta)}

print("C findes ved at rotere 91° mod uret:")
print("  ∠C = ∠A + 91°")
print("     = %s°" % N(c_theta%(2*pi)*DEG))
print("   C = (%s, %s)" % (N(c[x]), N(c[y])))
print("")

d_theta = c_theta + (c_theta - b_theta)
d = {x: o[x] + r*cos(d_theta), y: o[y] + r*sin(d_theta)}

print("D er spejlingen af B om C i cirklen:")
print("  ∠D = ∠C + (∠C - ∠B)")
print("     = %s°" % N(d_theta%(2*pi)*DEG))
print("   D = (%s, %s)" % (N(d[x]), N(d[y])))
print("")

print("Vinklen mellem tangenterne gennem A og C er")
print("       |∠A - ∠C|")
print("     = %s°" % abs(N((a_theta - c_theta)*DEG)))
print("")

print("Vinklen mellem tangenterne gennem B og D er")
print("       |∠B - ∠D|")
print("     = %s°" % abs(N((b_theta - d_theta)*DEG)))
print("")
