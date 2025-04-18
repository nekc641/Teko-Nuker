from colorama import init
from pystyle import Colorate, Colors, Center, Col, Add, Anime

from Plugins.logger import Logger
from Plugins.colors import Palette



palette = Palette()



class Funcs:
    
    @staticmethod
    def get_input(text: str, checker = True):
        
        
        
        text = f"{palette.red}{text}{palette.better_grassy_green}"

        v = input(text)
        if not checker(v):
            while not checker(v):
                Logger.Error.error("Try Again")
                v = input(text)
        
        return v
    
    @staticmethod
    def print_logo():
        logo = """
                      
  __            __    __                         ___                
 /\ \          /\ \__/\ \                      /'___\ __            
 \_\ \     __  \ \ ,_\ \ \____    ___   __  __/\ \__//\_\    ___    
 /'_` \  /'__`\ \ \ \/\ \ '__`\  / __`\/\ \/\ \ \ ,__\/\ \ /' _ `\  
/\ \L\ \/\ \L\.\_\ \ \_\ \ \L\ \/\ \L\ \ \ \_\ \ \ \_/\ \ \/\ \/\ \ 
\ \___,_\ \__/.\_\\ \__\\ \_,__/\ \____/\/`____ \ \_\  \ \_\ \_\ \_\
 \/__,_ /\/__/\/_/ \/__/ \/___/  \/___/  `/___/> \/_/   \/_/\/_/\/_/
                                            /\___/                  
                                            \/__/                   

"""


        print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.dark_red)), logo))
