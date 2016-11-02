# relaytcp
python3 module for SainSmart iMatic TCP 8 Channel Relay

- import relaytcp ### socket connection to 192.168.1.4 port 30000
- import _thread ### does not interupt the ongoing process

# examples:
- turn all relays on:
 _thread.start_new_thread(relaytcp.networkrelay, ("all","on"))
- turn all relays off:
 _thread.start_new_thread(relaytcp.networkrelay, ("all","off"))
- turn relay 3 on:
 _thread.start_new_thread(relaytcp.networkrelay, ("3","on"))
- turn relay 3 off:
 _thread.start_new_thread(relaytcp.networkrelay, ("3","off"))

# in terminal:
- python3 relaytcp.py
- then follow prompts...

