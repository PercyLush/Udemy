import time
import asyncio

async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCoffee()")
    return "Coffee ready"

async def toastBagel():
    print("Start toastBagel()")
    await asyncio.sleep(2)
    print("End toastBagel()")
    return "Bagel toasted"


async def main():
    start_time = time.time()

    batch = asyncio.gather(brewCoffee(), toastBagel())
    result_coffee, result_bagel = await batch

    end_time = time.time()
    elasped_time = end_time - start_time
    
    print(f"Result One: {result_coffee}")
    print(f"Result Two: {result_bagel}")
    print(f"Total Time: {elasped_time:.2f} Seconds")

if __name__ == "__main__":
    asyncio.run(main())