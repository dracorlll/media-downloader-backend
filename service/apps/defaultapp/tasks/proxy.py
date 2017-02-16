from apps.defaultapp.celery import app
from apps.defaultapp.services.proxy import new_proxy


@app.task(name=u'ProxyReceiver')
def proxy_receiver_task(*args, **kwargs):
    new_proxy()
