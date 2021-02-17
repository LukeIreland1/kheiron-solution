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


stack = []


def calc(args):
    for arg in args:
        if arg in ops:
            stack.append(
                execute(stack.pop(), arg, stack.pop())
            )
        else:
            stack.append(float(arg))
    return stack.pop()


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
