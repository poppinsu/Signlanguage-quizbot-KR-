import random as rd
import time
suhyung = ["남자/여자", "아들/딸", "아버지/어머니", "할아버지/할머니", "닭/경찰", "나비/잠자리"]
suwi = ["닭/바보", "병/맞다", "수고/만들다", "심심하다/궁금하다", "추억/멋", "배우다/해보다"]
sudong = ["기쁘다/항상", "거짓말/예쁘다", "믿다/위하다", "자유/동물", "아니다/여러가지", "행동/활동"]
suhyang = ["멀다/가깝다", "도와주다/도움받다", "어제/내일", "등산/하산", "빌리다/빌려주다"]
bisuji = ["기분좋다/기분나쁘다", "귀엽다/아깝다"]
try:
    with open("score.txt", "r") as highscore:
        highscore1 = highscore.read()
        print(f"최고점수 : {highscore1}")
    with open("time.txt", "r") as spendtime:
        spenttime = spendtime.read()
        print(f"최소 시간: {spenttime}")
except:
    with open("score.txt", "w+") as highscore:
        highscore.write("0")
        highscore.seek(0)
        highscore1 = highscore.read()
        print(f"최고점수 : {highscore1}")
    with open("time.txt", "w") as spendtime:
        spendtime.write("-")
score = 0
total = list(suwi+sudong+suhyang+suhyung+bisuji)
go = True
start_time = time.time()
while go:
    rd.shuffle(total)
    a = total.pop()
    print(f"현재 점수 : {score}")
    print(a)
    answer = input("수화소 차이 : ")
    if answer == "q":
        with open("score.txt", "r") as qhandle:
            scoreq = qhandle.read()
            if int(scoreq) < score:
                with open("score.txt", "w") as handle:
                    handle.write(str(score))
        break
    if total == []:
        print("종료")
        finish_time = time.time()
        spend_time = int(start_time - finish_time)
        print(f"{spend_time}소요")
        with open("time.txt", "r") as oldtime:
            otime = int(oldtime.read())
            if otime == "-" or otime > spend_time:
                with open("time.txt", "w+") as spendtimel:
                    spendtimel.write(str(spend_time))
                print("최소 시간 경신!")
        break
    while True:
        if answer == "수형" and a in suhyung:
            print("정답")
            score += 1
            print()
            break
        elif answer == "수위" and a in suwi:
            print("정답")
            score += 1
            print()
            break
        elif answer == "수동" and a in sudong:
            print("정답")
            score += 1
            print()
            break
        elif answer == "수향" and a in suhyang:
            print("정답")
            score += 1
            print()
            break
        elif answer == "비수지" and a in bisuji:
            print("정답")
            score += 1
            print()
            break
        else:
            print("오답")
            with open("score.txt", "r") as whandle:
                scorew = whandle.read()
                if int(scorew) < score:
                    with open("score.txt", "w") as handle:
                        handle.write(str(score))
            print(f"최종 점수 : {score}")
            go = False
            break
