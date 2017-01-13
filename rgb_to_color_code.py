def color_code_for_rgb(red, green, blue):
	""" Returns the hexadecimal color code given rgb values """
	return "%02X%02X%02X" % (red, green, blue)

def rgb_values_for_color(color_code):
	""" Returns a list of RGB values for a given hexadecimal code (either 3 digit or 6 digit) """

	rgb_value = lambda x: int(str(x), 16)

	if len(color_code) == 3:
		# Use twice of the given string for colors with 3 characters
		rgb_values = [rgb_value(color_code[i:i+1] * 2) for i in range(0, 3, 1)]
	elif len(color_code) == 6:
		rgb_values = [rgb_value(color_code[i:i+2]) for i in range(0, 6, 2)]

	return rgb_values
