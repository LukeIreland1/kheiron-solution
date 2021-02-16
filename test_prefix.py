import prefix

input1 = "3"
answer1 = 3
assert prefix.run(input1) == answer1

input2 = "+ 1 2"
answer2 = 3
assert prefix.run(input2) == answer2

input3 = "+ 1 * 2 3"
answer3 = 7
assert prefix.run(input3) == answer3

input4 = "+ * 1 2 3"
answer4 = 5
assert prefix.run(input4) == answer4

input5 = "- / 10 + 1 1 * 1 2"
answer5 = 3
assert prefix.run(input5) == answer5

input6 = "- 0 3"
answer6 = -3
assert prefix.run(input6) == answer6

input7 = "/ 3 2"
answer7 = 1.5
assert prefix.run(input7) == answer7