import math

import src.model.polish_notation as pn
import src.view_model.check_parse as chp


def get_testing_res(exp: str):
	return pn.calc(pn.shunting_yard(chp.parse(chp.prim_pars(exp))))


if __name__ == "__main__":
	success = 0
	fail = 0

	if get_testing_res("18+2") == 18+2:
		success += 1
	else:
		fail += 1

	if get_testing_res("18-181") == 18-181:
		success += 1
	else:
		fail += 1

	if get_testing_res("sin(100)") == float(math.sin(100)):
		success += 1
	else:
		fail += 1

	if get_testing_res("sin(100)+cos(180)") == float(math.sin(100) + math.cos(180)):
		success += 1
	else:
		fail += 1

	if get_testing_res("sin(100)+cos(100)*2") == float(math.sin(100) + math.cos(100) * 2):
		success += 1
	else:
		fail += 1

	if get_testing_res("tan(10)*2-(10+5)") == float(math.tan(10) * 2 - (10+5)):
		success += 1
	else:
		fail += 1

	if get_testing_res("log(8)-sqrt(12)") == float(math.log(8, 10) - math.sqrt(12)):
		success += 1
	else:
		fail += 1

	if get_testing_res("ln(15)-asin(1)") == float(math.log(15) - math.asin(1)):
		success += 1
	else:
		fail += 1

	if get_testing_res("atan(100)-(15*228)") == float(math.atan(100) - (15 * 228)):
		success += 1
	else:
		fail += 1

	if get_testing_res("cos(1337)+sin(228)") == float(math.cos(1337) + math.sin(228)):
		success += 1
	else:
		fail += 1

	if get_testing_res("ln(15)-sin(1337)") == float(math.log(15) - math.sin(1337)):
		success += 1
	else:
		fail += 1

	if get_testing_res("(228+(1337-15)/24+sin(100))") == (228 + (1337 - 15) / 24 + math.sin(100)):
		success += 1
	else:
		fail += 1

	if get_testing_res("ln(15)-asin(1)") == float(math.log(15) - math.asin(1)):
		success += 1
	else:
		fail += 1

	if get_testing_res("3/(cos(1337)+sin(228))") == float(3 / (math.cos(1337) + math.sin(228))):
		success += 1
	else:
		fail += 1

	if get_testing_res("cos(1337)*2+sin(228)") == float(math.cos(1337)*2+math.sin(228)):
		success += 1
	else:
		fail += 1

	if get_testing_res("-58-1337+sin(100)") == float(-58-1337+math.sin(100)):
		success += 1
	else:
		fail += 1

	if get_testing_res("tan(90)-atan(90)") == float(math.tan(90) - math.atan(90)):
		success += 1
	else:
		fail += 1

	if get_testing_res("(tan(90)-9)*atan(90)-(17-log(10))") == float((math.tan(90) - 9) * math.atan(90) - (17 - math.log(10, 10))):
		success += 1
	else:
		fail += 1

	if get_testing_res("1--2") == float(1--2):
		success += 1
	else:
		fail += 1

	if get_testing_res("5%4*sin(360)") == float(5 % 4 * math.sin(360)):
		success += 1
	else:
		fail += 1
	
	print(f"success:{success}")
	print(f"fail:{fail}")
	
