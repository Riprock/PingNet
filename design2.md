# Design 2 of communcaitons AKA REFACTOR communcaitons

## Type Range 44- 252
69 Types per range, and gonna have some funky stuff
## Code Range 0 -255
Using this for the commands Possibly.
### Commands
44- 94
    - Codes
        Split up the codes into a range of 3  
        To make it for the interpretation of cmd processors
For testing right now cmd is going to be type 44
Powershell 1
CMD 2
Linux 3
    Will make this based on OS detection later so that its not accidentally doing bash things on a windows machine
Code 255 is mayday mode - In case blueteams get smart and get fine grained with the firewall rules, this will activate mayday mode
and route everything over type 8 
### File sending
95 - 145
### Heart Beats
146 - 196




