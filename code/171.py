# one of the simplest programs
# using "async" (python 3.5+)

import asyncio
# methods for working with async
# code

async def f():
    # "async" function
    print("Hello there!")

asyncio.run(f()) # you need () here

# Output:
# Hello there!
