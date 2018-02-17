def main():
    tc = int(input("testcases > "))
    for i in range(tc):
        text = input("text > ")
        if check_parenthesis(text) == True:
            print("통과")
        else:
            print("거부")

def check_parenthesis(text):
    """
    코드 작성 영역
    """
    stack = []
    
    for c in text:
        if c == '(':
            stack.append(c)
        elif c == '{':
            if len(stack) > 0:
                if stack[-1] == '(':
                    return False
            stack.append(c)
        elif c == '[':
            if len(stack) > 0:
                if (stack[-1] == '(' or stack[-1] == '{'):
                    return False
            stack.append(c)
    
    
        elif c == ')':
            if len(stack) == 0:
                return False
            last = stack[-1]
            if not(last == '('):
                return False
            stack.pop()
        elif c == '}':
            if len(stack) == 0:
                return False
            last = stack[-1]
            if not(last == '{'):
                return False
            stack.pop()
        elif c == ']':
            if len(stack) == 0:
                return False
            last = stack[-1]
            if not(last == '['):
                return False
            stack.pop()
        else:
            pass
    
    return len(stack) == 0

if __name__ == "__main__":
    main()
