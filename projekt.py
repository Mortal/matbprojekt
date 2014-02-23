from sympy import *
import logging

x, y = symbols('x y')
DEG = 180/pi

def circle(x0, y0, r):
    return (Eq((x - x0)**2 + (y - y0)**2, r**2),)

def line_dir(p, dx, dy):
    return (Eq(dx * (y - p[y]), dy * (x - p[x])),)

def line_thru(p1, p2):
    return line_dir(p1, p2[x]-p1[x], p2[y]-p1[y])

def ray_dir(p, dx, dy):
    return (Ge(x * dx, p[x] * dx), Ge(y * dy, p[y] * dy)) + line_dir(p, dx, dy)

def ray_rotate(x0, y0, theta):
    return {x: x0*cos(theta) - y0*sin(theta), y: x0*sin(theta) + y0*cos(theta)}

a = {x:3, y:38}
b = {x:26, y:25}
r = 25
o, = filter(lambda p: p[y] > a[y], solve(circle(a[x], a[y], r) + circle(b[x], b[y], r)))
a_theta = atan2(a[y]-o[y], a[x]-o[x])
b_theta = atan2(b[y]-o[y], b[x]-o[x])
c_theta = a_theta + 91/DEG
d_theta = c_theta + (c_theta - b_theta)
c = {x: o[x] + r*cos(c_theta), y: o[y] + r*sin(c_theta)}
d = {x: o[x] + r*cos(d_theta), y: o[y] + r*sin(d_theta)}

#rundkreds = circle(o[x], o[y], 25)
#oc = {k: N(v) for k,v in ray_rotate(a[x]-o[x], a[y]-o[y], 91*pi/180).items()}
#print(oc)
#def intersect_circle_line(circle, line):
#    print("Solve circle for y")
#    cy1, cy2 = solve(circle[0], y)
#    print("Solve line for y")
#    ly, = solve(line[0], y)
#    print("Find circle/line intersection (1/2)")
#    eqn = Eq(cy1, ly)
#    print(eqn)
#    x1, = solve(eqn)
#    print("Find circle/line intersection (2/2)")
#    x2, = solve(Eq(cy2, ly))
#    print("Substitute solution (1/2)")
#    y1 = cy1.subs(x, x1)
#    print("Substitute solution (2/2)")
#    y2 = cy2.subs(x, x2)
#    print("Return")
#    return ({x:x1, y:y1}, {x:x2, y:y2})
#c = tuple(filter(lambda p: N(p[x]*oc[x]) > N(o[x]*oc[x]) and N(p[y]*oc[y]) > N(o[y]*oc[y]), intersect_circle_line(rundkreds, line_dir(o, oc[x], oc[y]))))

print("Opgave 1")
print("========")
print()
print("15^2 = x^2 + y^2")
print()

print("Opgave 2")
print("========")
print()
print("Cirklens ligning er:")
print(" r^2 = (x - x_0)^2 + (y - y_0)^2")
print()
print("Radius:")
print("   r = %s" % r)
print()
print("De to givne punkter på cirklen er:")
print("   A = (%s, %s)" % (a[x], a[y]))
print("   B = (%s, %s)" % (b[x], b[y]))
print()
print("Ud fra dette bestemmes cirklens centrum, idet dette ligger over punktet A:")
print(" x_0 = %s = %s" % (o[x], N(o[x])))
print(" y_0 = %s = %s" % (o[y], N(o[y])))
print()

print("Opgave 4")
print("========")
print()
print("Vi beregner ∠A og ∠B vha. arctan:")
print("  ∠A = %s°" % N(a_theta%(2*pi)*DEG))
print("  ∠B = %s°" % N(b_theta%(2*pi)*DEG))
print()
print("C findes ved at rotere 91° mod uret:")
print("  ∠C = ∠A + 91°")
print("     = %s°" % N(c_theta%(2*pi)*DEG))
print("   C = (%s, %s)" % (N(c[x]), N(c[y])))
print()
print("D er spejlingen af B om C i cirklen:")
print("  ∠D = ∠C + (∠C - ∠B)")
print("     = %s°" % N(d_theta%(2*pi)*DEG))
print("   D = (%s, %s)" % (N(d[x]), N(d[y])))
print()
print("Vinklen mellem tangenterne gennem A og C er")
print("       |∠A - ∠C|")
print("     = %s°" % abs(N((a_theta - c_theta)*DEG)))
print()
print("Vinklen mellem tangenterne gennem B og D er")
print("       |∠B - ∠D|")
print("     = %s°" % abs(N((b_theta - d_theta)*DEG)))
