
def plus(x,y): #플러스 연산
    return x + y

def minus(x,y): #마이너스 연산
    return x - y    

def multiply(x,y): #곱하기 연산
    return x * y
    
#메인함수
if __name__ == "__main__":

    userinput = input()
    result = float(userinput)
    
    if userinput == '7503':
        quit("Software Interaction Lab")
    

    error = True #에러 확인
    
    operator1 = input()

    if userinput.isdigit() != True: #정수인지 판별
        error = False
        
    elif operator1 not in('+','-','*'): #다른 연산자 들어갈시 오류
        error = False

    operator = operator1

    while True:
        
        suminput = input()
        
        if suminput == '7503':
            quit("Software Interaction Lab")
            
        if suminput.isdigit() != True:
            error = False
        
        suminput = float(suminput)
        
        
        if operator == '+':
            result = plus(result,suminput)
        elif operator == '-':
            result = minus(result,suminput)
        elif operator == '*':
            result = multiply(result,suminput)
        
        operator = input()
        
        if operator == '=': # = 입력시 계산 종료
            break
        
        if operator1 != operator:
            error = False
        

if error == True: # 에러가 아닐시 정상출력
    print(int(result))
else:               #에러시 에러메시지 출력
    print("ERROR!") 
    
        
    

    
    