import asyncio

def async_decorator(func):
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, func, *args, **kwargs)
    return wrapper

@async_decorator
def create_writer(file):
    def writer(value):
        with open(file, 'a') as f:
            f.write(str(value) + '\n')

    return writer

async def main():
    writer = await create_writer('output.txt')
    writer(1)
    writer(2)
    writer(3)
    f = open('output.txt','r')
    print(f.read())

asyncio.run(main())