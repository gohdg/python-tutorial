
import threading
import time


def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking the {first}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


# Python 프로그램의 main thread 한개에서 코드가 실행된다. 일반적으로
# walk_dog()
# take_out_trash()
# get_mail()

# args= tuple로 전달 한개일 경우에는 반드시 ,가 있어야 한다
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# .join() 스레드가 종료될때까지 main 스레드가 기다리게 한다
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")
