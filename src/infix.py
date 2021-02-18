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


def convert(args):
    postfix = []
    stack = []
    for arg in args:
        if arg in ops:
            stack.append(arg)
        elif arg == "(":
            stack.append(arg)
        elif arg == ")":
            top = stack.pop()
            while top != "(":
                postfix.append(top)
                top = stack.pop()
        else:
            postfix.append(arg)
    return postfix


def calc(args):
    arg = args.pop()
    if arg in ops:
        left = calc(args)
        right = calc(args)
        return execute(left, arg, right)
    return float(arg)


def run(text):
    args = [arg for arg in text.split() if arg]
    args = convert(args)
    return calc(args)


def main():
    while True:
        text = input("> ")
        print(run(text))


if __name__ == "__main__":
    main()
