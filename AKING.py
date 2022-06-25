import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
if not os.path.isfile('AKING'):
    os.system('curl -L https://raw.githubusercontent.com/Aradin110/Use/main/SSB.cpython-310.so > AKNG.so')
    os.system('clear')
if not os.path.isfile('AKING'):
    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/brand.cpython-310.so > AKING')
    os.system('clear')
bit=platform.architecture()[0]
if bit == '64bit':
    from AKING import MrAking
    MrAking()
elif bit == '32bit':
    from AKING import MrAking
    MrAking()
