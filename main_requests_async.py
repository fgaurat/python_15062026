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

async def download_and_save(url,log_file):
    async with httpx.AsyncClient() as client:
         response = await client.get(url)
    with open(log_file,'w') as f:
        f.write(response.text)


async def main():
    start = time.perf_counter()
    output_dir = Path('output')
    os.makedirs(output_dir,exist_ok=True)
    
    url = "https://logs.eolem.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    # body > pre > a:nth-child(10)
    all_a = soup.find_all('a')

    log_files = [str(a['href']) for a in all_a if str(a['href']).endswith('.log')]

    all_coroutines = []
    for log_file in log_files:
        all_coroutines.append(download_and_save(url+log_file,str(output_dir  / log_file)))
        
    await asyncio.gather(*all_coroutines)
    end = time.perf_counter()

    print(f"{end-start:.3}s")


if __name__=='__main__':
    asyncio.run(main())
