## TODO 
   - Make the command system argument based instead of "menu" based
   - Setup multiple ways to send the comands. So either all in one ping or across multple pings
   - Maybe add file transfer capabilites.
   - Encode the values so that they cant be read by just looking at a packet capture
   - For the storage table, add hostnames into it instaead of the dumb names i put 
   - Need to change from sleep(60) becuase of syncronizing callback times
   - Need to save the information from whatever the current state of the program is in case of crash or accidential exit
   - Add time of last call back. 
   - Figure out how to run this in the background
  

## Testing Notes
   - Need to do sanitization becuase spaces will break it
   - Sending a ping cmd to the client is a bad idea It just will not work. Have to investigate(This might just be irrelevant because thats just not something that should be done)
   

IF I go with heartbeat from server
    Im relying on the return packet that gets sent back
    for that I need to do a loop and iterate through all the ips sending 1 ping to each one every minute

If coming from client
just need to make sure that each packet gets processed quickly enough to update
  
Need to make sure an ack ping packet(not reply) gets sent from this machine as confirmation

Far off idea but maybe some kind of visual board to show callbacks

For sending files first packet will be a setup packet that is identified by f1
f2 will be the data
f1 will contain file name(with extension)