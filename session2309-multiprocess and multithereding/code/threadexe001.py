# Basic Async Function

# 1. Import the module
import asyncio
# 2. Define the async function
async def say_hello():
    print("Hello")
    await asyncio.sleep(4) # 3. Wait for 1 second
    print("World")
async def say_whatnow():
    print("What now")
    await asyncio.sleep(3) # 3. Wait for 1 second
    print("...")
# 4. Run the async function
asyncio.run(say_hello()) 
asyncio.run(say_whatnow())
