from apps.defaultapp.celery import app
from apps.defaultapp.services.proxy import new_proxy, clean_proxy_list


@app.task(name=u'ProxyReceiver')
def proxy_receiver_task(*args, **kwargs):
    new_proxy()


@app.task(name=u'ProxyCleaner')
def proxy_cleaner_task(*args, **kwargs):
    clean_proxy_list()
