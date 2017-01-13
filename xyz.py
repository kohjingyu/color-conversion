def xyz_for_color(red, green, blue, rounding=3):
	if red > 0.04045:
		red = ((red + 0.055)/1.055) ** 2.4
	else:
		red /= 12.92

	if green > 0.04045:
		green = ((green + 0.055)/1.055) ** 2.4
	else:
		green /= 12.92

	if blue > 0.04045:
		blue = ((blue + 0.055)/1.055) ** 2.4
	else:
		blue /= 12.92

	red *= 100
	green *= 100
	blue *= 100

	x = round(red * 0.4124 + green * 0.3576 + blue * 0.1805, rounding)
	y = round(red * 0.2126 + green * 0.7152 + blue * 0.0722, rounding)
	z = round(red * 0.0193 + green * 0.1192 + blue * 0.9505, rounding)

	return [x, y, z]

def xyz_to_Yxy(xyz_values, rounding=3):
	x, y, z = xyz_values[0], xyz_values[1], xyz_values[2]

	denominator = (x + y + z)
	result_x = round(x/denominator, rounding) if denominator != 0 else 0
	result_y = round(y/denominator, rounding) if denominator != 0 else 0

	return [y, result_x, result_y]

def xyz_to_cielab(xyz_values, rounding=3):
	x = xyz_values[0]/95.047
	y = xyz_values[1]/100
	z = xyz_values[2]/108.883

	if x > 0.008856:
		x = x ** (1/3)
	else:
		x = 7.787 * x + (16/116)

	if y > 0.008856:
		y = y ** (1/3)
	else:
		y = 7.787 * y + 16/116

	if z > 0.008856:
		z = z ** (1/3)
	else:
		z = 7.787 * z + 16/116

	l = round(116 * y - 16, rounding)
	a = round(500 * (x - y), rounding)
	b = round(200 * (y - z), rounding)

	return [l, a, b]

print(xyz_for_color(0.01, 0.5, 0.1))