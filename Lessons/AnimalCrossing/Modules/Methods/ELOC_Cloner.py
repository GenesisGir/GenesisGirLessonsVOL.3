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

# from import modules 
from dataclasses import dataclass, field

# define logger
def logger(): # GenesisGir's typical logger preset! 
    
    # importing modules
    import logging, logging.handlers
    from logging.handlers import SMTPHandler
    
    # create the logger and set severity
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # set logger lvl

    # create handles and set their severity
    
    #File Handlers
    file_handler = logging.FileHandler( 
    filename = r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Logs\AnimalCrossingPocketCamp.log",
    mode = 'w', # filemode 
    encoding = 'utf-8', 
    delay = False, 
    errors = None)
    file_handler.setLevel(logging.DEBUG)
    
    #Stream Handlers
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.CRITICAL)

    
    # create formatter
    formatter = logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s] [Lvl:%(levelno)s] [%(funcName)s] [%(lineno)d] %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p')

    # add formatter to handles
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    
    
    # adding the handler
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger
    pass

# logger variable
logger = logger()


# classes
@dataclass
class Cloners(): # group Eloc functions

        # doc string
        """ A print() function cloner that outputs the desired function set by the number of integer's passed to the parameter
        (line). A great tool from not having to clutter up the script with 'print()'.
        """

        """🖨  㠪㇄ㄖ⼕ ⼕㇄ㄖ𝓝🝗尺 🖨"""
        @staticmethod
        def Eloc_for_loop(line: int): # (ELOC) Empty line of code functionality

            for iteration in range(line): # for every iteration create blank line 

                print() # create a blank line of code

                # log info
                logger.info(f"Eloc() function has looped ({iteration}) times!")
