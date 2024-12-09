def isoperand(char):
    if char.isalpha():
        return True

def isoperator(char):
    operator="+-/*^"
    if char in operator:
        return True

def postfix(expression):
    result=""
    stack=[]
    prec={"+":0,"-":0,"*":1,"/":1,"^":2}    
    for i in expression:
        if isoperand(i):
            result+=i
        elif isoperator(i):
            while True:
                if not stack or stack[-1]=="(":
                    stack.append(i)
                    break
                else:
                    if prec[stack[-1]]<prec[i]:
                        stack.append(i)
                        break
                    else:
                        result+=stack.pop()         
        elif i=="(":
            stack.append(i)
        elif i==")":
            cpop=stack.pop()
            while(cpop!="("):
                result+=cpop
                cpop=stack.pop()
    while (len(stack)!=0):
        cpop=stack.pop()
        result+=cpop
    return result

a="a+b*(c^d-e)^(f+g*h)-i"
print(postfix(a))
        
        