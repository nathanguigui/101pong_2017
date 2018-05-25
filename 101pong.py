#!/usr/bin/env python
import math
import sys

def main(x0, y0, z0, x1, y1, z1, n):
	x0 = float(x0)
	y0 = float(y0)
	z0 = float(z0)
	x1 = float(x1)
	y1 = float(y1)
	z1 = float(z1)
	n = int(n)

	assert n >= 0
	frost = 0.00
	angle = 0.00
	radian = 0.00
	x = float(x1 - x0)
	y = float(y1 - y0)
	z = float(z1 - z0)
	xfinal = x * n + x1
	yfinal = y * n + y1
	zfinal = z * n + z1
	t = -z1 / z

	frost = math.sqrt(math.pow(x * t, 2) + math.pow(y * t, 2))
	radian = math.atan(z1 / frost)
	angle = (180 * radian) / math.pi

	print("The speed vector coordinates are :")
	print("({0:.2f};{1:.2f};{2:.2f})".format(x, y, z))
	print("At time t+", n, ", ball coordinates will be :")
	print("({0:.2f};{1:.2f};{2:.2f})".format(xfinal, yfinal, zfinal))
	if angle >= 0 and angle <= 90:
		print("The incidence angle is :\n{0:.2f} degrees".format(angle))
	else :
		print("The ball won't reach the bat.")
	return 0

if __name__ == "__main__" :
	main(*sys.argv[1:])