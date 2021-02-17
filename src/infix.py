ops = ["+", "-", "*", "/"]


def execute(right, op, left):
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return left / right


operand_stack = []
operator_stack = []


def calc(args):
    for arg in args:
        if arg in ops:
            operator_stack.append(arg)
        elif arg == "(":
            operator_stack.append(arg)
        elif arg == ")":
            operand_stack.append(
                execute(
                    operand_stack.pop(), operator_stack.pop(), operand_stack.pop()
                )
            )
            operator_stack.pop()
        else:
            operand_stack.append(float(arg))
    return operand_stack.pop()


def run(text):
    args = [arg for arg in text.split() if arg]
    return calc(args)


def main():
    print(__name__)
    while True:
        text = input("> ")
        print(run(text))


if __name__ == "__main__":
    main()
