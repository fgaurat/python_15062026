from celery import Celery
import requests

app = Celery('tasks', broker='sqla+sqlite:///celery_broker.db',backend="db+sqlite:///celery_results.db")

@app.task
def add(x, y):
    return x + y

@app.task
def download(url,file_name):
    response = requests.get(url+file_name)
    return file_name,response.text


@app.task
def save(param):
    file_name,text = param
    with open(file_name,'w') as f:
        f.write(text)