import time
print("Think of a number Between 1-60")
time.sleep(2)
print("Is it in ")
print(" 1, 3, 5, 7, 9")
print("11,13,15,17,19")
print("21,23,25,27,29")
print("31,33,35,37,39")
print("41,43,45,47,49")
print("51,53,55,57,59")
card_one = input('[y/n]') 

print("Is it in ")
print(" 2, 3, 6, 7,10")
print("11,14,15,18,19")
print("22,23,26,27,30")
print("31,34,35,38,39")
print("42,43,46,47,50")
print("51,54,55,58,59")
card_two = input('[y/n]')

print("Is it in ")
print(" 4, 5, 6, 7,12")
print("13,14,15,20,21")
print("22,23,28,29,30")
print("31,36,37,38,39")
print("44,45,46,47,52")
print("53,54,55,60")
card_three = input('[y/n]')

print("Is it in ")
print(" 8, 9,10,11,12")
print("13,14,15,24,25")
print("26,27,28,29,30")
print("31,40,41,42,43")
print("44,45,46,47,56")
print("57,58,59,60")
card_four = input('[y/n]')

print("Is it in ")
print("16,17,18,19,20")
print("21,22,23,24,25")
print("26,27,28,29,30")
print("31,48,49,50,51")
print("41,43,54,55,56")
print("57,58,59,60")
card_five = input('[y/n]')

print("Is it in ")
print("32,33,34,35,36")
print("37,38,39,40,41")
print("42,43,44,45,46")
print("47,48,49,50,51")
print("52,53,54,55,56")
print("57,58,59,60")
card_six = input('[y/n]')
num = 0
if (card_one == ("y")):
	num = num + 1
if (card_two == ("y")):
	num = num + 2
if (card_three == ("y")):
	num = num + 4
if (card_four == ("y")):
	num = num + 8
if (card_five == ("y")):
	num = num + 16
if (card_six == ("y")):
	num = num + 32

	
print("Your number is " + str(num));
	
