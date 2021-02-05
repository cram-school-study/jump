import os

with os.scandir('/') as a:
    for b in a:
        print(b.name)