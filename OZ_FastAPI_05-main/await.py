import time
import asyncio

async def a():
    print ("A 작업 시작")           # [1] a() 실행 시작
    await asyncio.sleep(5)        # [2] 2초 대기 -> 양보
    print ("A 작업 종료")           # [5] a() 종료

async def b():
    print("B 작업 시작")             # [3] b() 실행 시작 
    await asyncio.sleep(2)         # [4] 2초 대기 -> 양보
    print("B 작업 종료")             # [6] b() 종료


async def main():
    coro1 = a()
    coro2 = b()
    await asyncio.gather(coro1, coro2)

start= time.time()
asyncio.run(main())
end = time.time()
print(f"총 소요 시간 : {end - start:.2f} 초")