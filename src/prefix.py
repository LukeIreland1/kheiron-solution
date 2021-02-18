ops = ["+", "-", "*", "/"]


def execute(left, op, right):
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return left / right


def calc(args):
    arg = args.pop()
    if arg in ops:
        left = calc(args)
        right = calc(args)
        return execute(left, arg, right)
    return float(arg)

def run(text):
    args = [arg for arg in text.split() if arg]
    args = args[::-1]
    return calc(args)

def main():
    while True:
        text = input("> ")
        print(run(text))


if __name__ == "__main__":
    main()
