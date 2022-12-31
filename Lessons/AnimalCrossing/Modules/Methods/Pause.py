"""

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
                                    
                                    
                            █▀█ █▀█ █ █▄░█ ▀█▀ ▄▀ ▀▄   █▀▀ █░░ █▀█ █▄░█ █▀▀ █▀█
                            █▀▀ █▀▄ █ █░▀█ ░█░ ▀▄ ▄▀   █▄▄ █▄▄ █▄█ █░▀█ ██▄ █▀▄
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                A script that contain's various cloners using different methods of cloning the
                print() to emulate a faster and more efficient way of making the code ore readable!

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
"""

# import modules
import logging, logging.handlers
import time

# from import modules 
from dataclasses import dataclass, field

# Method module imports
from Modules.Methods.ELOC_Cloner import *

# classes
class Pause(): 

    # doc string
    """ program execution delay set by the parameter time """
    
    # class method
    def Execution_delay(sec: int): 
        
        # doc string
        """ defining a function to make freezing exeute easier """
        
        # freeze by the sec parameter
        time.sleep(sec)
        
        # log info
        logger.info(f"Program execution has been delayed by ({sec}) seconds!")
        
        Cloners.Eloc_for_loop(1)
        pass