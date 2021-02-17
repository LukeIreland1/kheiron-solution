import src.web_client as web_client

input1 = "( 1 + 2 )"
answer1 = 3
assert web_client.infix(input1) == answer1

input2 = "( 1 + ( 2 * 3 ) )"
answer2 = 7
assert web_client.infix(input2) == answer2

input3 = "( ( 1 * 2 ) + 3 )"
answer3 = 5
assert web_client.infix(input3) == answer3

input4 = "( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"
answer4 = -1.8
assert web_client.infix(input4) == answer4

input5 = "3"
answer5 = 3
assert web_client.prefix(input5) == answer5

input6 = "+ 1 2"
answer6 = 3
assert web_client.prefix(input6) == answer6

input7 = "+ 1 * 2 3"
answer7 = 7
assert web_client.prefix(input7) == answer7

input8 = "+ * 1 2 3"
answer8 = 5
assert web_client.prefix(input8) == answer8

input9 = "- / 10 + 1 1 * 1 2"
answer9 = 3
assert web_client.prefix(input9) == answer9

input10 = "- 0 3"
answer10 = -3
assert web_client.prefix(input10) == answer10

input11 = "/ 3 2"
answer11 = 1.5
assert web_client.prefix(input11) == answer11

print("Web test success")