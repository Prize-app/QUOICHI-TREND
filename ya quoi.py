from pystyle import *
from pyfade import *

quoi = input()
if quoi =='Ya quoi ?':
    print("CHI")


kalash = '''
     ___________________________________________,
   ___/  ////////  \____/                         |----------------------
  <__ |_////////__________________________________|----------------------
    \)                 *                |________|
     /        __________________________|
    /        /  ||   //
   /        /____\__//
  /        /~~~~~~~~~
 /        /
/        /
\-------/
'''

if quoi =='Ya quoi ?':
  print(Colorate.Horizontal(Colors.yellow_to_red, kalash, 1))

raw = input()