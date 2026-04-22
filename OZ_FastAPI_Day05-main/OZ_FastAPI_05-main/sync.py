# 동기(synchronous)
# 프로그래밍에서 동기란 A 작업 -> B 작업 순서대로 진행되는 것 의미

import time

def hello():
    time.sleep(3)
    print("Hello")

hello()