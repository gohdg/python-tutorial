import time

# my_time = int(input("Enter the time in seconds: "))

my_time = 3671  # 예: 3671초는 1시간 1분 11초

for x in range(my_time, 0, -1):
    seconds = x % 60  # 초 단위는 60으로 나눈 나머지
    minutes = (x // 60) % 60  # 분 단위는 초 단위를 제외한 나머지에서 60으로 나눈 나머지
    hours = x // 3600  # 시간 단위는 전체 시간을 3600으로 나눈 몫
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")

# minutes = int(x / 60) % 60 정수 변환을 한다.
# minutes = (x // 60) % 60 에서 // 연산자는 소수점을 버린 정수 반환
