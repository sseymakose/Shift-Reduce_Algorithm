action = {
    0:{'id': 's5', '(': 's4'},
    1:{'+': 's6', '$': 'acc'},
    2:{'+': 'r2', '*': 's7', ')': 'r2', '$': 'r2'},
    3:{'+': 'r4', '*': 'r4', ')': 'r4', '$': 'r4'},
    4:{'id': 's5', '(': 's4'},
    5:{'+': 'r6', '*': 'r6', ')': 'r6', '$': 'r6'},
    6:{'id': 's5', '(': 's4'},
    7:{'id': 's5', '(': 's4'},
    8:{'+': 's6', ')': 's11'},
    9:{'+': 'r1', '*': 's7', ')': 'r1', '$': 'r1'},
    10:{'+': 'r3', '*': 'r3', ')': 'r3', '$': 'r3'},
    11:{'+': 'r5', '*': 'r5', ')': 'r5', '$': 'r5'}
}

go_to = {
    0:{'E': 1, 'T': 2, 'F': 3},
    4:{'E': 8, 'T': 2, 'F': 3},
    6:{'T': 9, 'F': 3},
    7:{'F': 10}
}
def parse(input_string):
    tokens = list(input_string)
    nw_tokens = []
    for a in tokens:
        if a == 'i':
            nw_tokens.append('id')
        elif a == 'd':
            continue
        else:
            nw_tokens.append(a)
    tokens = nw_tokens
    stack = [0]

    i = 0

    output = ""

    while stack[0] != 'acc':
        top = stack[-1]

        if top in action:
            if i >= len(tokens):
                token = '$'
            else:
                token = tokens[i]

            if token not in action[top]:
                print("INVALID string entered. SYNTAX ERROR!")
                return

            a = action[top][token]

            if a[0] == "s":
                stack.append(token)
                stack.append(int(a[1:]))
                output += token + " "
                i += 1
            elif a[0] == "r":
                rule_num = int(a[1:])
                index = 0
                stack.pop()
                if rule_num == 6:
                    for old in range(len(stack)):
                        if stack[old] == 'id':
                            index = old
                    stack[old] = 'F'
                elif rule_num == 5:
                    new_stack = []
                    for old in range(len(stack)):
                        if stack[old] == '(' and (stack[old+2] == 'E' and stack[old + 4] == ')'):
                            index = old
                    for old2 in range(len(stack)):
                        if old2 == index:
                            new_stack.append('F')
                        elif old2 == index+1 or (old2 == index+2 or (old2 == index+3 or old2 == index+4)):
                            continue
                        else:
                            new_stack.append(stack[old2])
                    stack = new_stack
                elif rule_num == 4:
                    for old in range(len(stack)):
                        if stack[old] == 'F':
                            index = old
                    stack[old] = 'T'
                elif rule_num == 3:
                    new_stack = []
                    for old in range(len(stack)):
                        if stack[old] == 'T' and (stack[old+2] == '*' and stack[old + 4] == 'F'):
                            index = old
                    for old2 in range(len(stack)):
                        if old2 == index:
                            new_stack.append('T')
                        elif old2 == index+1 or (old2 == index+2 or (old2 == index+3 or old2 == index+4)):
                            continue
                        else:
                            new_stack.append(stack[old2])
                    stack = new_stack
                elif rule_num == 2:
                    for old in range(len(stack)):
                        if stack[old] == 'T':
                            index = old
                    stack[old] = 'E'
                elif rule_num == 1:
                    new_stack = []
                    for old in range(len(stack)):
                        if stack[old] == 'E' and (stack[old+2] == '+' and stack[old + 4] == 'T'):
                            index = old
                    for old2 in range(len(stack)):
                        if old2 == index:
                            new_stack.append('E')
                        elif old2 == index+1 or (old2 == index+2 or (old2 == index+3 or old2 == index+4)):
                            continue
                        else:
                            new_stack.append(stack[old2])
                    stack = new_stack
                go_to_result = go_to[stack[-2]][stack[-1]]
                stack.append(go_to_result)
            elif a == 'acc':
                print("VALID string entered. ACCEPTED!")
                return
        else:
            print("INVALID string entered. SYNTAX ERROR!")
            return

    print(output)

text = input()
text = text.replace(" ","")
parse(text)

