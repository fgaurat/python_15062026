import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os
from pathlib import Path
import time
import asyncio
import httpx


# async def download_and_save(url,log_file):
#     response = requests.get(url)
#     with open(log_file,'w') as f:
#         f.write(response.text)

# async def download_and_save(url,log_file):
#     async with httpx.AsyncClient() as client:
#          response = await client.get(url)
#     with open(log_file,'w') as f:
#         f.write(response.text)



async def download(queue_download:asyncio.Queue,queue_save:asyncio.Queue):
    while True:
        url,log_file=  await queue_download.get()
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            param = log_file,response.text
            queue_save.put_nowait(param)
        
        queue_download.task_done()


async def save(queue_save:asyncio.Queue):
    while True:
        log_file,content=  await queue_save.get()
        with open(log_file,'w') as f:
            f.write(content)
        queue_save.task_done()



async def main():
    start = time.perf_counter()

    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()

    nb_download_workers = 10
    nb_save_workers = 5


    output_dir = Path('output')
    os.makedirs(output_dir,exist_ok=True)
    
    url = "https://logs.eolem.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    # body > pre > a:nth-child(10)
    all_a = soup.find_all('a')
    log_files = [str(a['href']) for a in all_a if str(a['href']).endswith('.log')]

    tasks=[]
    for i in range(nb_download_workers):
        t = asyncio.create_task(download(queue_download,queue_save))
        tasks.append(t)

    for i in range(nb_save_workers):
        t = asyncio.create_task(save(queue_save))
        tasks.append(t)


    for log_file in log_files:
        param = url+log_file,str(output_dir  / log_file)
        queue_download.put_nowait(param)

    
    await queue_download.join()
    await queue_save.join()

    [t.cancel() for t in tasks]


    # all_coroutines = []
    # for log_file in log_files:
    #     all_coroutines.append(download_and_save(url+log_file,str(output_dir  / log_file)))
        
    # await asyncio.gather(*all_coroutines)
    end = time.perf_counter()

    print(f"{end-start:.3}s")


if __name__=='__main__':
    asyncio.run(main())
