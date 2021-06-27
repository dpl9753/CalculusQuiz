### 모듈 불러오기 ###
import random  # random(난수 생성) 모듈 불러오기
from sympy import *  # Sympy 모듈로부터 기능 불러오기
from sympy import Integral, Symbol  # Sympy 모듈로 부터 Integral, Symbol 기능 불러오기
import sys  # sys 모듈 불러오기
import os   #os 모듈 불러오기


### 정답 함수 ###
def correctAnswer(number):
    print("★정답입니다.★")
    global score

    for i in range(0, 3, 1):
        if number == i:
            score[i] += 1
            
    print("===========================================")
    print("미분 식 구하기 점수 :", score[0])
    print("미분계수 값 구하기 점수 :", score[1])
    print("정적분 값 구하기 점수 :", score[2])
    print("===========================================")
    print()


### 오답 함수 ###
def wrongAnswer(answer):
    global score
    print("오답입니다.")
    print()
    print("정답", answer)
    print()
    print("===========================================")
    print("미분 식 구하기 점수 :", score[0])
    print("미분계수 값 구하기 점수 :", score[1])
    print("정적분 값 구하기 점수 :", score[2])
    print("===========================================")
    print()


### 진행 함수 ###
def progress():
    print("퀴즈를 이어서 진행하시겠습니까?")

    while True:
        Q = int(input("진행(1) / 종료(2) >> "))
        print()

        if (Q == 1):
            break
        elif (Q == 2):
            print("============================")
            print("퀴즈를 종료합니다. Good Bye!")
            print("============================")
            sys.exit()
        else:
            print("오류입니다. 다시 입력해주세요.")
            print()
            continue


### 다항 함수 ###
def polynomialFunction():
    
    ## 다항함수 1단계
    print()
    print("<1단계>")
    a = (random.sample(range(-10, 10), 1))  # 3차 계수 난수 생성
    b = (random.sample(range(-10, 10), 1))  # 2차 계수 난수 생성
    c = (random.sample(range(-10, 10), 1))  # 1차 계수 난수 생성
    d = (random.sample(range(-10, 10), 1))  # 상수항 난수 생성
    x = Symbol('x')  # x를 변수로 설정
    f = a[0] * x ** 3 + b[0] * x ** 2 + c[0] * x + d[0]  # 원함수 f(x)
    print("-" * 40)
    print("f(x) =", f)
    print("함수 f(x)의 도함수 f'(x)를 구하시오.")
    print("-" * 40)
    derivativePoly = Derivative(f, x).doit()  # 도함수 f'(x)

    while (1):
        print("치팅코드:", derivativePoly) # 치팅코드
        fp = derivativePoly  # 도함수 f'(X) 답안 출력
        print()
        inputfpPoly = input("f'(x) = ")
        print()
        comAnswerfpPoly = str(fp)
        inputfpPoly_ = inputfpPoly.replace(" ", "")
        comAnswerfpPoly_ = comAnswerfpPoly.replace(" ", "")
        mathComAnswerfpPoly = sympify(comAnswerfpPoly_)
        mathInputfpPoly = sympify(inputfpPoly_)

        if (mathComAnswerfpPoly - mathInputfpPoly) == 0 :
            correctAnswer(0)
            break
        else :
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerfpPoly)
                progress()

    
    ## 다항함수 2단계
    print()
    print("<2단계>")
    k = (random.sample(range(1, 5), 1))  # 미분계수의 x 값 난수 생성
    fpx = fp.doit().subs({x: k[0]})  # 미분계수 x 값
    print("-" * 40)
    print("f'(x) =", derivativePoly, "입니다.")
    print("x = %d 에서의 미분계수 값을 구하시오." % k[0])
    print("-" * 40)

    while (1):
        print("치팅코드:", fpx) # 치팅코드
        print()
        inputfpxPoly = input("답 >> ")  # 미분계수 구하기 문제 답 입력
        print()
        comAnswerfpxPoly = str(fpx)
        inputfpxPoly_ = inputfpxPoly.replace(" ", "")
        comAnswerfpxPoly_ = comAnswerfpxPoly.replace(" ", "")
        mathComAnswerfpxPoly = sympify(comAnswerfpxPoly_)
        mathInputfpxPoly = sympify(inputfpxPoly_)

        if (mathComAnswerfpxPoly - mathInputfpxPoly) == 0 :
            correctAnswer(1)
            break
        else :
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(" >> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerfpxPoly)
                progress()

    
    ## 다항함수 3단계
    print()
    print("<3단계>")
    critical = solve(derivativePoly)  # f'(x) = 0 을 만족하는 x값 계산
    print("f'(x) = 0 인 x값(극값이 되는 x값)은\n"
          "x =", critical, "입니다.")  # f'(x) = 0 을 만족하는 x값 출력
    print()
    x = Symbol('x')  # x 변수 설정
    F = Integral(f, x).doit()  # 부정적분을 통해 원시함수 F 계산
    print("-" * 60)
    print("원시함수 F(x) =", F)
    bottom = random.randint(-5, 2)  # 아래 끝 난수 생성
    top = random.randint(2, 7)  # 위 끝 난수 생성
    V = Integral(f, (x, bottom, top)).doit()  # 정적분 값 구하기
    print("***************주어진 구간***************")
    print()
    print(' ' * 15, "위 끝:", top)
    print()
    print(' ' * 14, "아래 끝:", bottom)
    print()
    print("*****************************************")
    print("제시된 구간에서의 정적분 값을 구하시오")
    print("-" * 60)

    while (1):
        print("치팅코드:", V)  # 정적분 값 출력
        print()
        inputDintegralPoly = input("답 >> ")  # 정적분 값 구하기 문제 답 입력
        comAnswerDintegralPoly = str(V)
        inputDintegralPoly_ = inputDintegralPoly.replace(" ", "")
        comAnswerDintegralPoly_ = comAnswerDintegralPoly.replace(" ", "")
        mathComAnswerDintegralPoly = sympify(comAnswerDintegralPoly_)
        mathInputDintegralPoly = sympify(inputDintegralPoly_)

        if (mathComAnswerDintegralPoly - mathInputDintegralPoly) == 0 :
            correctAnswer(2)
            break
        else:
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(" >> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerDintegralPoly)
                progress()

                
### 지수 함수 ###
def exponentialFunction():
    
    ## 지수함수 1단계
    print()
    print("<1단계>")
    x = Symbol('x')
    # 지수함수 랜덤 생성
    a = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    b = random.randint(1, 4)
    c = random.randint(0, 3)
    global oriExponentialFunction
    oriExponentialFunction = a * exp(b * x) + c
    exprd = sympify(oriExponentialFunction)  # 수식화
    global exprD
    exprD = diff(exprd, x)  # 도함수 추출
    global comAnswerfpExp
    comAnswerfpExp = str(exprD)
    print("-" * 40)
    print("f(x) =", oriExponentialFunction)
    print("함수 f(x)의 도함수 f'(x)를 구하시오.")
    print("-" * 40)

    while (1):
        print("치팅코드:", comAnswerfpExp)  # 치팅코드
        global inputfpExp
        print()
        inputfpExp = str(input("f'(x) = "))
        print()
        inputfpExp_ = inputfpExp.replace(" ", "")
        comAnswerfpExp_ = comAnswerfpExp.replace(" ", "")
        mathComAnswerfpExp = sympify(comAnswerfpExp_)
        mathInputfpExp = sympify(inputfpExp_)

        if (mathComAnswerfpExp - mathInputfpExp) == 0 :
            correctAnswer(0)
            break
        else:
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerfpExp)
                progress()

    
    ## 지수함수 2단계
    print()
    print("<2단계>")
    k = random.randint(-5, 5)  # 미분계수의 x 값 난수 생성
    DCV = exprD.subs(x, k)
    global comAnswerfpxExp
    comAnswerfpxExp = str(DCV)
    print("-" * 40)
    print("함수 f'(x) =", exprD, "입니다.")
    print("x =", k, "에서의 미분계수를 구하시오.")
    print("-" * 40)

    while (1):
        print("치팅코드", comAnswerfpxExp)  # 치팅코드
        global AfpxExp
        print()
        inputfpxExp = str(input("답 >> "))
        print()
        inputfpxExp_ = inputfpxExp.replace(" ", "")
        comAnswerfpxExp_ = comAnswerfpxExp.replace(" ", "")
        mathComAnswerfpxExp = sympify(comAnswerfpxExp_)
        mathInputfpxExp = sympify(inputfpxExp_)

        if (mathComAnswerfpxExp - mathInputfpxExp) == 0 :
            correctAnswer(1)
            break
        else:
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerfpxExp)
                progress()
                
    
    ## 지수함수 3단계
    print()
    print("<3단계>")
    critical = solve(exprD)  # critical point를 만족하는 x값 계산
    print("f'(x) = 0 인 x값(극값이 되는 x값)\n"
          'x =', critical, "입니다")  # f'(x) = 0 을 만족하는 x값
    print()
    expri = sympify(oriExponentialFunction)
    exprI = integrate(expri, x)  # f(x) 적분
    print("-" * 60)
    print("원시함수 F(x) =", exprI)
    bottom = random.randint(0, 5)  # 아래끝 난수 생성
    top = random.randint(0, 10)  # 위끝 난수 생성
    ITV = integrate(exprI, (x, top, bottom))
    comAnswerDintegralExp = str(ITV)
    print("***************주어진 구간***************")
    print()
    print(' ' * 15, "위 끝:", top)
    print()
    print(' ' * 14, "아래 끝:", bottom)
    print()
    print("*****************************************")
    print("제시된 구간에서의 정적분 값을 구하시오")
    print("-" * 60)
    
    while (1):
        print("치팅코드:", comAnswerDintegralExp)  # 치팅코드
        print()
        inputDintegralExp = input("답 >> ")
        print()
        inputDintegralExp_ = inputDintegralExp.replace(" ", "")
        comAnswerDintegralExp_ = comAnswerDintegralExp.replace(" ", "")
        mathComAnswerDintegralExp = sympify(comAnswerDintegralExp_)
        mathInputDintegralExp = sympify(inputDintegralExp_)

        if (mathComAnswerDintegralExp - mathInputDintegralExp) == 0 :
            correctAnswer(2)
            break
        else:
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerDintegralExp)
                progress()


### 로그 함수 ###
def logarithmicFunction():

    ## 로그함수 1단계
    print()
    print("<1단계>")
    x = Symbol('x')  # x를 변수로 설정
    # 로그함수 랜덤 생성
    a = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    b = random.randint(1, 5)
    c = random.randint(-5, 5)
    global oriLogarithmicFunction
    oriLogarithmicFunction = a * log(b * x) + c
    exprd = sympify(oriLogarithmicFunction)  # 수식화
    global exprD
    exprD = diff(exprd, x)  # 도함수 추출
    global comAnswerfpLog
    comAnswerfpLog = str(exprD)
    print("-" * 40)
    print("f(x) =", oriLogarithmicFunction)
    print("함수 f(x)의 도함수 f'(x)를 구하시오.")
    print("-" * 40)

    while (1):
        global inputfpLog
        print("치팅코드:", comAnswerfpLog)  # 치팅코드
        print()
        inputfpLog = str(input("f'(x) = "))
        print()
        inputfpLog_ = inputfpLog.replace(" ", "")
        comAnswerfpLog_ = comAnswerfpLog.replace(" ", "")
        mathComAnswerfpLog = sympify(comAnswerfpLog_)
        mathInputfpLog = sympify(inputfpLog_)

        if (mathComAnswerfpLog - mathInputfpLog) == 0 :
            correctAnswer(0)
            break
        else :
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerfpLog)
                progress()
                
    
    ## 로그함수 2단계
    print()
    print("<2단계>")
    k = (random.randint(-10, -1) or random.randint(1, 10))  # 미분계수의 x 값 난수 생성
    DCV = exprD.subs(x, k)
    comAnswerfpxLog = str(DCV)
    print("-" * 40)
    print("함수 f'(x) =", exprD, "입니다.")
    print("x =", k, "에서의 미분계수를 구하시오.")
    print("-" * 40)

    while (1):
        print("치팅코드:", comAnswerfpxLog)  # 치팅코드
        global inputfpxLog
        print()
        inputfpxLog = str(input("답 >> "))
        print()
        inputfpxLog_ = inputfpxLog.replace(" ", "")
        comAnswerfpxLog_ = comAnswerfpxLog.replace(" ", "")
        mathComAnswerfpxLog = sympify(comAnswerfpxLog_)
        mathInputfpxLog = sympify(inputfpxLog_)
        
        if (mathComAnswerfpxLog - mathInputfpxLog) == 0:
            correctAnswer(1)
            break
        else :
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerfpxLog)
                progress()
                
    
    ## 로그함수 3단계
    print()
    print("<3단계>")
    x = Symbol('x')
    critical = solve(exprD)  # critical point를 만족하는 x값 계산
    print("f'(x) = 0 인 x값(극값이 되는 x값)\n"
          'x =', critical, "입니다")  # f'(x) = 0 을 만족하는 x값
    print()
    expri = sympify(oriLogarithmicFunction)
    exprI = integrate(expri, x) # f(x) 적분
    print("-" * 60)
    print("원시함수 F(x) =", exprI)
    bottom = random.randint(0, 5)  # 아래끝 난수 생성
    top = random.randint(0, 10)  # 위끝 난수 생성
    ITV = integrate(exprI, (x, bottom, top))
    global comAnswerDintegralLog
    comAnswerDintegralLog = str(ITV)
    print("***************주어진 구간***************")
    print()
    print(' ' * 15, "위 끝:", top)
    print(' ' * 14, "아래 끝:", bottom)
    print()
    print("*****************************************")
    print("제시된 구간에서의 정적분 값을 구하시오")
    print("-" * 60)

    while (1):
        print("치팅코드:", comAnswerDintegralLog)  # 치팅코드
        global inputDintegralLog
        print()
        inputDintegralLog = input("답 >> ")
        print()
        inputDintegralLog_ = inputDintegralLog.replace(" ", "")
        comAnswerDintegralLog_ = comAnswerDintegralLog.replace(" ", "")
        mathComAnswerDintegralLog = sympify(comAnswerDintegralLog_)
        mathInputDintegralLog = sympify(inputDintegralLog_)

        if (mathComAnswerDintegralLog - mathInputDintegralLog) == 0:
            correctAnswer(2)
            break
        else :
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerDintegralLog)
                progress()


### 삼각 함수 ###
def trigonometricFunction():
    
    ## 삼각함수 1단계
    print()
    print("<1단계>")
    x = Symbol('x')  # x를 변수로 설정
    # 지수함수 랜덤 생성
    a = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
    b = random.randint(1, 4)
    c = random.randint(-3, 3)
    global oriTrigonometricFunction
    # sin(x), cos(x) 랜덤으로 종류 선택
    TrigonometricChoice = random.randint(0, 1)

    if TrigonometricChoice == 0:
        oriTrigonometricFunction = a * sin(b * x) + c
    elif TrigonometricChoice == 1:
        oriTrigonometricFunction = a * cos(b * x) + c

    exprd = sympify(oriTrigonometricFunction)  # 수식화
    global exprD
    exprD = diff(exprd, x)
    global comAnswerfpTri
    comAnswerfpTri = str(exprD)
    print("-" * 40)
    print("f(x) =", oriTrigonometricFunction)
    print("함수 f(x)의 도함수 f'(x)를 구하시오.")
    print("-" * 40)

    while (1):
        print("치팅코드", comAnswerfpTri)  # 치팅코드
        global AfpTri
        print()
        AfpTri = str(input("f'(x) = "))
        print()
        AfpTri_ = AfpTri.replace(" ", "")
        comAnswerfpTri_ = comAnswerfpTri.replace(" ", "")
        mathComAnswerfpTri = sympify(comAnswerfpTri_)
        mathAfpTri = sympify(AfpTri_)
        
        if (mathComAnswerfpTri - mathAfpTri) == 0 :
            correctAnswer(0)
            break
        else :
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerfpTri)
                progress()

    
    ## 삼각함수 2단계
    print()
    print("<2단계>")
    k = random.choice([-4 * pi, -3 * pi, -2 * pi, -pi, 0, pi, 2 * pi, 3 * pi, 4 * pi])  # 미분계수의 x 값 난수 생성
    print(k)  # 치팅코드
    x = Symbol('x')
    DCV = exprD.subs(x, k)
    global comAnswerfpxTri
    comAnswerfpxTri = str(DCV)
    print("-" * 40)
    print("함수 f'(x) =", exprD, "입니다.")
    print("x =", k, "에서의 미분계수를 구하시오.")
    print("-" * 40)

    while (1):
        print("치팅코드:", comAnswerfpxTri)  # 치팅코드
        global AfpxTri
        print()
        AfpxTri = str(input("답 >> "))
        print()
        AfpxTri_ = AfpxTri.replace(" ", "")
        comAnswerfpxTri_ = comAnswerfpxTri.replace(" ", "")
        mathComAnswerfpxTri = sympify(comAnswerfpxTri_)
        mathAfpxTri = sympify(AfpxTri_)

        if (mathComAnswerfpxTri -  mathAfpxTri) == 0:
            correctAnswer(1)
            break
        else :
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))
            
            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerfpxTri)
                progress()

    
    ## 삼각함수 3단계
    print()
    print("<3단계>")
    x = Symbol('x')
    critical = solve(exprD)  # critical point를 만족하는 x값 계산
    print("f'(x) = 0 인 x값(극값이 되는 x값)\n"
          'x =', critical, "입니다")  # f'(x) = 0 을 만족하는 x값
    print()
    expri = sympify(oriTrigonometricFunction)
    exprI = integrate(expri, x)  # 리스트 자료형 수식화
    print("-" * 60)
    print("원시함수 F(x) = ", exprI)
    bottom = random.choice([0, pi, 2 * pi, 3 * pi, 4 * pi, 5 * pi])  # 아래끝 난수 생성
    top = random.choice([6 * pi, 7 * pi, 8 * pi, 9 * pi, 10 * pi])  # 위끝 난수 생성
    ITV = integrate(expri, (x, bottom, top))
    global comAnswerDintegralTri
    comAnswerDintegralTri = str(ITV)
    print("***************주어진 구간***************")
    print()
    print(' ' * 15, "위 끝:", top)
    print(' ' * 14, "아래 끝:", bottom)
    print()
    print("*****************************************")
    print("제시된 구간에서의 정적분 값을 구하시오")
    print("-" * 60)

    while (1):
        print("치팅코드:", comAnswerDintegralTri)  # 치팅코드
        global ADintegralTri
        print()
        ADintegralTri = input("답 >>  ")
        print()
        ADintegralTri_ = ADintegralTri.replace(" ", "")
        comAnswerDintegralTri_ = comAnswerDintegralTri.replace(" ", "")
        mathComAnswerDintegralTri = sympify(comAnswerDintegralTri_)
        mathADintegralTri = sympify(ADintegralTri_)

        if (mathComAnswerDintegralTri - mathADintegralTri) == 0 :
            correctAnswer(2)
            break
        else :
            print("오답입니다. 해당 단계를 다시 풀이하겠습니까?")
            print("1. 다시 도전하기\n2. 정답 확인하고 진행 여부 결정하기")
            C = int(input(">> "))

            if C == 1:
                continue
            elif C == 2:
                wrongAnswer(comAnswerDintegralTri)
                progress()
    



### 메인 함수 ###

score = [0, 0, 0, 0]    # score 초기화

while (1):
    print("============================= <<Calculus Quiz>> =============================")
    print("[1단계] f(x)가 제시되면 f'(x)를 입력하세요, 정답이면 다음 단계로 넘어갑니다.\n")
    print("[2단계] x=k가 제시되면 f'(k)를 입력하세요, 정답이면 다음 단계로 넘어갑니다.\n")
    print("[3단계] 위끝과 아래끝이 제시되면 도함수의 정적분 값을 구하세요.\n"
          "        정답이면 1점 획득입니다.\n")
    print("정답이면 계속되고 오답이면 연속 정답수가 제시되고 프로그램이 종료됩니다.\n")
    print("참고 : f'(x) 식은 a*x**2 + b*x + c 꼴로 입력하시면 됩니다.")
    print("=============================================================================\n")
    
    funcSort = int(input("<메뉴를 선택하세요.>\n\n1.다항함수\n\n2.지수함수\n\n3.로그함수\n\n4.삼각함수\n\n5.개발자 정보\n\n6.끝내기\n\n>> "))

    if funcSort == 1:
        polynomialFunction()

    elif funcSort == 2:
        exponentialFunction()

    elif funcSort == 3:
        logarithmicFunction()

    elif funcSort == 4:
        trigonometricFunction()

    elif funcSort == 5:
        print()
        print("Program Information")
        print("=" * 50)
        print("Calculus Quiz")
        print("-" * 50)
        print("Developer")
        print("2020313232    컴퓨터교육과    김동호")
        print("2020313623    컴퓨터교육과    김민중")
        print("2020313250    컴퓨터교육과    김태완")
        print("2020311252    컴퓨터교육과    최재석")
        print("-" * 50)
        print("Programed by team MathCom")
        print("-" * 50)
        print("Calculus Quiz Program version 5.8")
        print("-" * 50)
        print("Last Update")
        print("2020.11.28")
        print("=" * 50)
        print()
        continue

    elif funcSort == 6:
        print()
        print("======================================")
        print()
        print("      퀴즈를 마칩니다. Good Bye!")
        print()
        print("======================================")
        break

    else:
        print()
        print("잘못된 입력입니다.\n다시 입력하세요.")
        print()
        continue

