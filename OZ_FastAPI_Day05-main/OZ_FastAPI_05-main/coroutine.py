# 동기식
# 1) 함수의 정의 : def 함수명()
# 2) 함수의 호출 : 함수명() => 함수 실행


# 비동기식
# 1) 코루틴 함수((coroutine function)) 정의 : async def 함수명()
# 2) 코루틴 함수 호출 : coro = 함수명() => 함수 실행 X, 코루틴 객체(coro) 생성
# 3) 코루틴 함수 실행 : await coro 또는 asyncio.run(함수명())

import asyncio

async def hello():
    print("Hello")

coro1 = hello()  # 코루틴 객체(coro1) 생성
coro2 = hello()  # 코루틴 객체(coro2) 생성

async def main():
    await asyncio.gather(coro1, coro2)  # 코루틴 객체(coro1, coro2) 실행

main_coro = main()  # main() 코루틴 객체(main_coro) 생성
asyncio.run(main_coro)  # 코루틴 함수 실행
