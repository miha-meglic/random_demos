import requests
import threading
import time


def tfunc(i):
    requests.get('https://rls-led.loca.lt/led',
                 json={
                     'led_id': i,
                     'red': 255,
                     'blue': 0
                 })

    # print(f'Done: {i}')


# for i in range(30):
#     x = threading.Thread(target=tfunc, args=(i,))
#     x.start()

# threading._shutdown()

requests.get('https://rls-led.loca.lt/led',
             json={
                 'led_id': 6,
                 'red': 255,
                 'blue': 128
             })
