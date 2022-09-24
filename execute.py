from FRcode import result
import requests
import lock
if True in result:
    lock.runrun()
else:
    requests.post('https://maker.ifttt.com/trigger/stranger/json/with/key/buVVmrERe_Q1B_jiP3eNoj')