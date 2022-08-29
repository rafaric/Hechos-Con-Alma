from hcablog.celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def 