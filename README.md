# PingNet
This is creating a beacon network through the use of the ICMP protocol 
The use case is a competition environment where some machines have ping check for scoring thus ping has to be allowed through the firewall.
Since ping is a check, it makes for a good lateral movement point.

## Usage
Server
```bash
pyhton3 server.py
```
Client
```bash
pyhton3 beacon.py
```
There is the argument of -v to allow for a verbose output for whenever a cmd is run on both the client and the server
