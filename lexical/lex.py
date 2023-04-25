def isKeyword(ch):
    listKeyword = ['int', 'float', 'while', 'do', 'if', 'sort']
    if ch in listKeyword:
        return 'keyword'
    return False


def isOperator(ch):
    listOperator = ['+', '-', '*', '/', '<', '>', '=']
    if ch in listOperator:
        return 'operator'
    return False


def isInteger(ch):
    listInteger = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if ch in listInteger:
        return True
    return False


def isIndentifier(ch):
    if isInteger(ch[0]):
        return False
    return True


str = "float x = a + b"
characters = str.split(" ")
for ch in characters:
    if isKeyword(ch):
        print(f"{ch} is a valid Keyord")
    elif isOperator(ch):
        print(f"{ch} is a valid Operator")
    elif isInteger(ch):
        print(f"{ch} is a valid Integer")
    elif isIndentifier(ch):
        print(f"{ch} is a valid Identifier")
    else:
        print(f"{ch} is not valid")
