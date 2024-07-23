while True:
    try:
        n = input()
        m = len(n)//2
        # n에 0이 들어오면 stop 
        if n == '0':
            break
        # 한자리 수는 팰린드롬수로 판단 
        elif len(n) == 1:
            print('yes')
        # 두자리 이상이면 수를 반씩 나눠서 각각의 인덱스를 비교 
        else:
            for i in range(m):
                a = n[:m]
                b = n[:m-1:-1]  # 거꾸로 인덱스 출력
                if a[i] == b[i]:
                    i+=1  # 맞으면 다음 인덱스로
                    if i==m:  # 전체 길이와 마지막 인덱스가 같으면 팰린드롬수
                        print('yes')
                else:
                    print('no')
                    break
    except:
        break