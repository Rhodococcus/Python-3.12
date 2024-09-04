from fractions import Fraction
import sympy

x = sympy.symbols("x")

f = sympy.Eq(x*Fraction('2/5'), 1760)

result = sympy.solve(f)

remains = result[0] - 1760

print('남은 돈은 {}원 입니다'.format(remains))

