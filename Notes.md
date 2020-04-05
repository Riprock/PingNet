##TODO
   - Make the command system argument based instead of "menu" based
   - Setup multiple ways to send the comands. So either all in one ping or across multple pings
   - Maybe add file transfer capabilites.
   - Encode the values so that they cant be read by just looking at a packet capture
   - For the storage table, add hostnames into it instaead of the dumb names i put 
   - Need to change from sleep(60) becuase of syncronizing callback times
   - Need to save the information from whatever the current state of the program is in case of crash or accidential exit
   - Add time of last call back. 
   - Figure out how to run this in the background
  
Need to make sure an ack ping packet(not reply) gets sent from this machine as confirmation

Far off idea but maybe some kind of visual board to show callbacks

# Testing Notes
   - Need to add IP to filter beucase random pings will break it
   - Need to do sanitization becuase spaces will break it
