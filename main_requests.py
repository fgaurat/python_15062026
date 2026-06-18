import requests
from bs4 import BeautifulSoup
from pprint import pprint
import os
from pathlib import Path
import time
# from glob import glob
import re

def main():
    output_dir = Path('output')
    log_files = output_dir.glob('*.log')
    
    pattern_ip = r"^(.+?)\s"
    pattern_http_status = r"\"\s(404)\s"
    # pattern_ip = r"^((\d{1,3}\.?){4})"
    # pattern_ip = r"^((\d{1,3}\.){3}\d{1,3})"
    # pattern_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    
    cpt = 0
    for log_file in log_files:
        with open(log_file) as f:
            for line in f:
                # ip = re.findall(pattern_ip,line)
                # print(ip,line)
                status = re.findall(pattern_http_status,line)
                if status:
                    cpt+=1
                    print(status)

    print(cpt)

def main_requests():
    start = time.perf_counter()
    output_dir = Path('output')
    os.makedirs(output_dir,exist_ok=True)
    
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # body > pre > a:nth-child(10)
    all_a = soup.find_all('a')

    log_files = [str(a['href']) for a in all_a if str(a['href']).endswith('.log')]

    # for a in all_a:
    #     href= str(a['href'])
    #     if href.endswith('.log'):
    #         log_files.append(href)
    pprint(log_files)

    for log_file in log_files:
        response = requests.get(url+log_file)
        with open(output_dir / log_file,'w') as f:
            f.write(response.text)

    end = time.perf_counter()

    print(f"{end-start:.3}s")


if __name__=='__main__':
    main()
    main_requests()
