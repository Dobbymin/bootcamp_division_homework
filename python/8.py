"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    n = int(input())
    number = 1
    num_sum = [i for i in range(1, n+1)]

    for i in range(1, n + 1):
        number *= i
    print(sum(num_sum))
    print(number)

    return


if __name__ == '__main__':
    main()
