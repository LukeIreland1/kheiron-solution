from src import infix

input1 = "( 1 + 2 )"
answer1 = 3
assert infix.run(input1) == answer1, "{} != {}".format(input1, answer1)

input2 = "( 1 + ( 2 * 3 ) )"
answer2 = 7
assert infix.run(input2) == answer2, "{} != {}".format(input2, answer2)

input3 = "( ( 1 * 2 ) + 3 )"
answer3 = 5
assert infix.run(input3) == answer3, "{} != {}".format(input3, answer3)

input4 = "( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"
answer4 = -1.8
assert infix.run(input4) == answer4, "{} != {}".format(input4, answer4)

print("Infix test success")
