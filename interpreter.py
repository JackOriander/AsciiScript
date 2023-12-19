memory = dict()

def b_sec_decode(b_section:list)->str:
    ascii = 0
    keywords = ['(', '-', '>', ')', '*']
    limit = []
    string = []
    loop_flag = False
    #b_section.reverse()
    for index, l in enumerate(b_section):
        if l not in keywords:
            ascii = ascii*10 + int(l)
        if l in keywords:
            if (l == "-" and b_section[index+1] == ">") or (l==")"):
                limit.append(ascii)
                ascii = 0
            elif (l == "*"):
                loop_flag = True
                
    #print(x_list)
    #print(string)
    for i in range(limit[0], limit[1]+1):
        string.append(chr(i))
    if loop_flag == True:
        t = int(''.join(b_section[b_section.index("*")+1:]))
        return (''.join(string))*t
    #print(limit)
    elif loop_flag == False:
        return ''.join(string)
    
def var_declare(var_section:list):
    data = list((list(var_section)[list(var_section).index("M")+1:]))
    data.pop()
    if data[0].isnumeric() == False:
        f = list(var_section)[list(var_section).index("=")+1:]
        f.pop()
        memory[data[0]] = int(''.join(f))
    elif data[0].isnumeric() == True:
        return -9999
    #print(memory)

def task_executor(task_list:list):
    x = []
    for i in task_list:
        x.append(chr(int(i)))
    return ''.join(x)
    
def tokenize_text(text, task_executor):
    variable_token = text[0]
    if not (len(variable_token) == 1 and variable_token.isalpha()):
        raise ValueError("Variable token must be a single alphabetic character.")

    if variable_token not in memory:
        raise ValueError(f"Variable '{variable_token}' not found in memory dictionary.")

    variable_value = memory[variable_token]

    condition_token, condition_value = text[1:3], int(text[4])

    compare_funcs = {
        "<": lambda a, b: a < b,
        ">": lambda a, b: a > b,
        "<=": lambda a, b: a <= b,
        ">=": lambda a, b: a >= b,
        "==": lambda a, b: a == b,
    }

    if compare_funcs[condition_token](variable_value, condition_value):
        # Execute tasks if condition is true
        task_list = text[6:-1].split("-")
        task_result = task_executor(task_list)
        return task_result
    else:
        # Condition is false, return empty string
        return -9999

def condition_decode(condition_section):
    parts = condition_section #str(condition_section).split()
    variable = None
    condition = None
    task = None
    print(parts)
    for part in parts:
        if part in memory:
            variable = part
        elif part == '<':
            condition = part
        elif part == '>':
            condition = part
        elif part == '<=':
            condition = part
        elif part == '>=':
            condition = part
        elif part not in [';', '?']:
            if task is None:
                task = part
            else:
                task = f" {part}"
        elif part == ';':
            break
    
    if not all([variable, condition, task]):
        return -9999
    else:
        #print(variable)
        #print(condition)
        #print(task)
        pass
    
    
def decode(filename:str)->str:
    string = []
    
    with open(filename) as f:
        code = (f.read()).split()
    
    for index, ascii in enumerate(code):
        try:
            string.append(chr(int(ascii)))
            
        except Exception as e:
            try:
                b_sec = list(str(code[index]))
                string.append(b_sec_decode(b_sec))
            except:
                try:
                    x = var_declare(b_sec)
                    if x == -9999:
                        print(f"Error at line {index+1}: {e}")
                except:
                    try:
                        print(''.join(b_sec))
                        x = tokenize_text(''.join(b_sec), task_executor)
                        print(x)
                        if x == -9999:
                            print(f"Error at line {index+1}: {e}")
                        else:
                            string.append(x)
                    except:
                        print(f"Error at line {index+1}: {e}")
    #print(string)
    return ''.join(string)

file = input("Enter the .ascs file: ")
if file.endswith(".ascs"):
    print(decode(file))
else:
    print("ERROR: Not a AsciiScript File!")
