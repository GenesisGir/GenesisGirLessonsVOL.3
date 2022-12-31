"""

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
                                    
                                    
                █▀▀ █░█ █▄░█ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀   ▀▄▀   █▀▄▀█ █▀▀ ▀█▀ █░█ █▀█ █▀▄ █▀
                █▀░ █▄█ █░▀█ █▄▄ ░█░ █ █▄█ █░▀█ ▄█   █░█   █░▀░█ ██▄ ░█░ █▀█ █▄█ █▄▀ ▄█
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                A script that contain's various functions that all have different behaviors that are
                required by the program for tasks for the user to implement actions etc.
                Add, Remove, Edit them here.

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
"""


# import modules
import os
import sys
import logging, logging.handlers
import time, random, pygame


# from import modules 
from dataclasses import dataclass, field
from Modules.Entities import *
from Modules.PlayerElements import *
from Modules.PlayerElements import Player

# Method module imports
from Modules.Methods.ELOC_Cloner import *
from Modules.Methods.Pause import *
from pygame import mixer
from playsound import playsound

# classes
Player

# functions/methods

# Music/FX
def bkround_song(filepath: str, loop: int = -1 , vol: float = 0.2 ): # menu music theme to program
    
    # menu.wav using pygame and mixer method to render!
    pygame.mixer.init() # boot up mixer
    pygame.mixer.music.load(filepath) # load .wav
    pygame.mixer.music.play(loop) # play .wav
    pygame.mixer.music.set_volume(vol)
    
    # log info
    logger.info("menu.wav rendered!")
    pass

def equip_fx(): # clothing equip sound FX
    
    # file path
    file_path = r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Audio\quip.wav" # wav file path
    
    # initalize mixer
    pygame.mixer.init()
    
    # create sound
    sound = pygame.mixer.Sound(file_path) # Create a new Sound object from a file or buffer object
    
    # set volume for .wav
    sound.set_volume(0.2) # set the playback volume for this Sound
    
    # playback
    pygame.mixer.Sound.play(sound, loops=0, maxtime=0, fade_ms=0) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel
    
    # log info
    logger.info("quip.wav rendered!")
    pass

def prompt_sound(): # enter prompt wav
    
    # file path
    file_path = r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Audio\enter.wav" # wav file path
    
    # initalize mixer
    pygame.mixer.init()
    
    # create sound
    sound = pygame.mixer.Sound(file_path) # Create a new Sound object from a file or buffer object
    
    # set volume for .wav
    sound.set_volume(0.3) # set the playback volume for this Sound
    
    # playback
    pygame.mixer.Sound.play(sound, loops=0, maxtime=0, fade_ms=0) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel
    
    # log info
    logger.info("quip.wav rendered!")
    pass

def error_wav(): # error wav
    
    # file path
    file_path = r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Audio\error.wav" # wav file path
    
    # initalize mixer
    pygame.mixer.init()
    
    # create sound
    sound = pygame.mixer.Sound(file_path) # Create a new Sound object from a file or buffer object
    
    # set volume for .wav
    sound.set_volume(0.3) # set the playback volume for this Sound
    
    # playback
    pygame.mixer.Sound.play(sound, loops=0, maxtime=0, fade_ms=0) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel
    
    # log info
    logger.info("error.wav rendered!")
    pass

def gameboy_boot(): # clothing equip sound FX
    # docstring
    """The sound of the gameboy booting up, uses pygame and it's mixer for sound generation and implementation."""
    
    # file path
    file_path = r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Audio\Gameboy.wav" # wav file path
    
    # initalize mixer
    pygame.mixer.init()
    
    # create sound
    sound = pygame.mixer.Sound(file_path) # Create a new Sound object from a file or buffer object
    
    # set volume for .wav
    sound.set_volume(0.3) # set the playback volume for this Sound
    
    # playback
    pygame.mixer.Sound.play(sound, loops=0, maxtime=0, fade_ms=0) # begin sound playback play(loops=0, maxtime=0, fade_ms=0) -> Channel
    
    # log info
    logger.info("quip.wav rendered!")
    pass

def credits():
    
    # doc string
    """ Displays credits to user than returns back to the main menu with the main_menu() function. """
    
    # import module
    import webbrowser
    
    # backround music
    bkround_song(r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Audio\Night.wav")
    
    Cloners.Eloc_for_loop(20)
    
    print("""
            
            ░█████╗░███╗░░██╗██╗███╗░░░███╗░█████╗░██╗░░░░░  ░█████╗░██████╗░░█████╗░░██████╗░██████╗██╗███╗░░██╗░██████╗░
            ██╔══██╗████╗░██║██║████╗░████║██╔══██╗██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██║████╗░██║██╔════╝░
            ███████║██╔██╗██║██║██╔████╔██║███████║██║░░░░░  ██║░░╚═╝██████╔╝██║░░██║╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░
            ██╔══██║██║╚████║██║██║╚██╔╝██║██╔══██║██║░░░░░  ██║░░██╗██╔══██╗██║░░██║░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗
            ██║░░██║██║░╚███║██║██║░╚═╝░██║██║░░██║███████╗  ╚█████╔╝██║░░██║╚█████╔╝██████╔╝██████╔╝██║██║░╚███║╚██████╔╝
            ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░
                        
                        
                        
                                ▀█▀ █░█ ▄▀█ █▄░█ █▄▀ █▀   █▀▀ █▀█ █▀█   █▀█ █░░ ▄▀█ █▄█ █ █▄░█ █▀▀
                                ░█░ █▀█ █▀█ █░▀█ █░█ ▄█   █▀░ █▄█ █▀▄   █▀▀ █▄▄ █▀█ ░█░ █ █░▀█ █▄█
    """)
    
    Cloners.Eloc_for_loop(2)
    
    Pause.Execution_delay(3)
    
    print("                                                 Source code by Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺                                         ")
    
    Cloners.Eloc_for_loop(2)
    
    Pause.Execution_delay(3)
    
    print("                                                       Hideki Konno Producer                                             ")
    
    Cloners.Eloc_for_loop(2)
    
    Pause.Execution_delay(3)
    
    print("                                          Data and credits for this game contributed by \n ")
    
    Cloners.Eloc_for_loop(1)
    
    Pause.Execution_delay(3)
    
    print("                                  mistymermaid, shinjiman, Blk_Mage_Ctype, oliist, Super_Archer, \n ") 
    
    Cloners.Eloc_for_loop(1)
    
    Pause.Execution_delay(3)
    
    print("                                                twadepsvita, ironyisntdead, 1258lkj. \n ")
    
    # visit animal crossing website w/webbrowser module prompt
    while True: # iterate until condition is met
        
        resp = input("Visit The Animal Crossing website and support Nintendo [y/n]? >>> ")
        # flow control
        if resp == "y":  # user did not want to open webpage
            
            prompt_sound() # enter.wav playback
            
            # open webpage
            webbrowser.open("https://animal-crossing.com/")
            break
            pass
        
        elif resp == "n": # user did not want to open webpage
            
            prompt_sound() # enter.wav playback
            break
            pass
        
        else: # user input invalid value, re-iterate while loop
            continue

def main_menu():
    
    # flow control for menu prompts
    while True: # iterate infinite until functions are used or break statements are presented
        
        # init Animal Crossing: Pocket Camp - sound effect with download link  music OST
        bkround_song(r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Audio\menu.wav")

        # doc string
        """
        The main menu function for the animal crossing project this will contain the functionalities that will make user
        control where to start in the program to starting a brand new game, or terminating the app, as well as viewing
        credits from the programmer himself and developer stats.    
        """

        Cloners.Eloc_for_loop(2)

        print("░█████╗░███╗░░██╗██╗███╗░░░███╗░█████╗░██╗░░░░░  ░█████╗░██████╗░░█████╗░░██████╗░██████╗██╗███╗░░██╗░██████╗░")
        print("██╔══██╗████╗░██║██║████╗░████║██╔══██╗██║░░░░░  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██║████╗░██║██╔════╝░")
        print("███████║██╔██╗██║██║██╔████╔██║███████║██║░░░░░  ██║░░╚═╝██████╔╝██║░░██║╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░")
        print("██╔══██║██║╚████║██║██║╚██╔╝██║██╔══██║██║░░░░░  ██║░░██╗██╔══██╗██║░░██║░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗")
        print("██║░░██║██║░╚███║██║██║░╚═╝░██║██║░░██║███████╗  ╚█████╔╝██║░░██║╚█████╔╝██████╔╝██████╔╝██║██║░╚███║╚██████╔╝")
        print("╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░ \n \n")


        # prompts for main_menu()
        print("new game [n]") # start new story mode event
        print("close animal crossing [x]") # terminate
        print("credits [c]") 
        Cloners.Eloc_for_loop(1)
        
        resp = input(">>> ") # retrieve users input data ⌨

        Cloners.Eloc_for_loop(1)

        # flow statements
        if resp == "n": # user decides start a new game
            
            # init Animal Crossing: Pocket Camp - sunny morning music OST
            bkround_song(r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Audio\SunnyM.wav")
        
            #load() # initialize loading screen

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , "Hey!")
            


            controller_prompt() 

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , "You seem new here!!") 

            controller_prompt() 

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , """Welcome to animal crossing: pocket camp! a place were you can chill
            be yourself and explore the world trying out different clothing sets or various challenges 
            and so much way more! You are currently in the beta version of this game and its a lesson/demo 
            and was intended for the learning process for novice programmers such as myself, GenesisGir
            and yes even you!""") 

            controller_prompt() 

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , "Oh your not a novice?") 

            Pause.Execution_delay(1)

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , ". . .") 

            Pause.Execution_delay(1)

            controller_prompt() 

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , "Even an experienced programmer/software dev could learn a trick or two!") 

            controller_prompt() 

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , """This program comes with chalk full of tips and tricks that you could implement
            inside your on programs to progress in your craft!""")

            controller_prompt() 

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , "But anywho!") 

            controller_prompt() 

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , """Welcome and we have to get you set up with your own personal room and items 
            clothing, accessories, little trinkets and much more!""") 

            Pause.Execution_delay(3)

            # KK Slider game dialog
            npc_dialog(f"{KK_SLIDER}" , "Lets get started!") 

            controller_prompt()
            
            break
            pass
        
        elif resp == "x": # user decides close program
        
            print("Animal Crossing: Pocket Camp is now shutting down!")

            # time.sleep() to delay executions
            Pause.Execution_delay(random.randint(3,5))

            sys.exit() # shut down the program
            pass
        
        elif resp == "c": # user decides to view credits of game
            credits()
            
        elif resp == " ": # user pressed enter without any values
            pass
        
        else: 
            pass # null , nill, pass

def create_username(): 
    
    # doc string
    """ Username creation function, Takes user's input and assigns it to the 'username' variable."""
    
    # flow conditions
    while True: # while loop being used as infinite loop until username is created correctly!
        
        # execption handler 🕷
        try: # check for errors in data collection of users input
            
            rsp = input("enter your nintendo username > ") # capture input
            
            Cloners.Eloc_for_loop(1)
            
            # username special charater checker flow control
            if not rsp.isalnum():
                
                # nintendo game dialog
                print("Nintendo: Username's can not contain special characters '!@#$%'! \n")
                
                error_wav()
                
                Cloners.Eloc_for_loop(1)
                
                # log info
                logger.info("user input invalid special characters! and username was denied!")
                
                continue # re-iterate
                pass
            
            # username int length checker flow control
            elif len(rsp) in range(3,8) and rsp.isalnum(): # create username                 
                
                # username comfirmation
                resp = input(f"Nintendo: Your username will be {rsp} are you sure? y/n >>> ")
                
                if resp == "y": # comfirmed username
                    
                    # overwrite username variable with user created username
                    Player.username = rsp
                    
                    # log info
                    logger.info(f"The username {Player.username} was created for user!")

                    Cloners.Eloc_for_loop(1)
                    
                    break
                
                elif resp == "n": # re-create username
                    
                    # log info
                    logger.info("The user decided to try a diffrent username")
                    
                    Cloners.Eloc_for_loop(1)
                    
                    continue # re-iterate
                    
                    pass
                    
            elif len(rsp) >= 8 or len(rsp) <= 3: # player input too many values
            
                # nintendo game dialog
                print("Nintendo: Username's can only be the 3-8 characters long and can only contain numbers and letters!")
                
                error_wav()
                
                Cloners.Eloc_for_loop(1)
                
                # log info
                logger.info("user input too many characters in username creation. MAX chars is 8, The value given was" + str(len(rsp)) + "⚠")
                
                continue # re-iterate
                pass
            
            elif resp == '': # user did not enter a value
                
                # log debug
                logger.debug("User tried to continue username creation without values.")
                
                error_wav()
                
                kk_slider_exception_speech_randomizer(random.randint(0,2))
                
                continue
                pass
        


        # excecption
        except ValueError: 
            
            # log info
            logger.info(f"ValueError str only, The value {Player.username} was given")
            
            Cloners.Eloc_for_loop(1)
            
            continue

def leaf_token(start_int: int, stop_int: int): 
    
    # doc string
    """ The leaf_token() generates a random integer used for randomness within other functions. To create a sense of
    more possiblities!"""
    
    # global
    global leaf_token
    
    # random integer variable
    leaf_token = int(random.randint(start_int, stop_int))
    
    """ leaf token info

        ╭╮╱╱╱╱╱╱╱╭━╮╱╭╮╱╱╱╭╮
        ┃┃╱╱╱╱╱╱╱┃╭╯╭╯╰╮╱╱┃┃
        ┃┃╭━━┳━━┳╯╰╮╰╮╭╋━━┫┃╭┳━━┳━╮
        ┃┃┃┃━┫╭╮┣╮╭╯╱┃┃┃╭╮┃╰╯┫┃━┫╭╮╮
        ┃╰┫┃━┫╭╮┃┃┃╱╱┃╰┫╰╯┃╭╮┫┃━┫┃┃┃
        ╰━┻━━┻╯╰╯╰╯╱╱╰━┻━━┻╯╰┻━━┻╯╰╯

        The leaf token is a random token that generates random integers from 0 to 5 and can be used to add randomizations
        to speech or other elements within the game.

        """
    
    pass

def kk_slider_exception_speech_randomizer(): 
    
    # doc string
    """ A speech randomizer for KK Slider . Uses the leaf_token() to aid random outcomes."""
    
    # globals
    global leaf_token
    
    leaf_token
    
    # conditions
    if leaf_token == 0:
        
        # KK Slider NPC Dialog
        npc_dialog(KK_SLIDER, "You need a user name pal! try again")
    
    elif leaf_token == 1:
        
        # KK Slider NPC Dialog
        npc_dialog(KK_SLIDER, "You have a name don't ya?")
    
    elif leaf_token == 2:
        
        # KK Slider NPC Dialog
        npc_dialog(KK_SLIDER, "Type your username than hit enter please!")

def bed_prompt(): 
    
    # doc string
    """ asks user to leave bed """
    
    while True: # looping condition!

        # grab users input
        resp = input("Get out of bed? y/n? >>> ") # create variable from users input

        Cloners.Eloc_for_loop(1) # (ELOC)
        
        prompt_sound()

        if resp == "y": # user gets out of bed

            # player dialog
            print(f"- {Player.username} plops out of bed -")
            
            Cloners.Eloc_for_loop(1) # (ELOC)

            Pause.Execution_delay(random.randint(1,2))

            break # break away from while loop w/break statement

            pass
        
        elif resp == "n": # user wants to stay in bed

            # player dialog
            print(f"{Player.username}: I should really get up and get dressed.")

            controller_prompt()

            Cloners.Eloc_for_loop(1) # (ELOC)

            continue
            pass
        
        elif resp == " ": # user gave no input
            
            error_wav()
            pass # null, nill, pass
        
        else:
            pass

def wardrobe():
    
    # init Animal Crossing: Pocket Camp - sunny noon music OST
    bkround_song(r"GenesisGirLessonsVOL.3\Lessons\AnimalCrossing\Audio\Noon.wav")
    
    # doc string
    """ Equips various types of clothing to the player or unequips them"""
    
    # methods
    def notifcation(): 
        # docstring
        """Controls for the wardrobe menu."""
        
        # wardrobe control notifcations
        print("""Equip clothing by typing the item catalog number and pressing enter! 
press [d] to display the wardrobe interface again or [x] to exit wardobe!
            """)
        pass
    
    # clothing globals
    # equipped clothes globals
    global pajama_top 
    global kuromi_tee 
    global academic_hha_jacket
    global aqua_polka_tee
    global usahana_tee

    # bottoms
    global pajama_pants 
    global black_formal_pants
    global bone_pants
    global dry_denim_skirt
    global lavender_chiffon_skirt 
    global isabelles_skirt 

    # Dresses
    global black_sailor_pinafore 
    global black_sakura_hakama 
    global black_yukata_dress
    global blue_mail_room_dress 
    global blue_tuxedo_set 

    # Handheld Accessories
    global berry_ice_cream_cone
    global black_purrfect_plushie
    global green_watering_can 
    global gudetama_fan 
    global handheld_can_of_soda 

    # Hats
    global angelic_wig
    global apple_stem	
    global black_ram_horn_wig 
    global blue_ombre_antler_wig
    global bunny_hood 

    # Face
    global black_jewel_thief_mask 
    global doctors_mask
    global halloween_face_paint 
    global post_op_patch 
    global snowy_crystal_earrings 

    # Backpiece
    global angelic_wings 
    global bat_friends
    global black_kitty_backpack 
    global blue_hydrangea_obi 
    global dark_angel_wings

    # Shoes
    global blue_spring_moccasins 
    global brown_santa_boots 
    global lavender_pumps
    global pastel_purple_pumps
    global pink_rubber_rain_boots

    # Socks
    global black_stockings
    global pajama_slippers
    global bobby_socks
    global crimson_striped_socks
    global purple_star_socks
    global white_stockings

    # Outfits
    global starry_pajama_suit 
    global animal_crossing_ski_suit 
    global mario_outfit 
    global eevee_costume 
    global foxtail_dress 
    global zipper_costume 
    
    # equipped globals
    # equipped clothes globals
    global equipped_top
    global equipped_bottom
    global equipped_dress
    global equipped_handheld
    global equipped_hat
    global equipped_face
    global equipped_backpiece
    global equipped_shoes
    global equipped_socks
    global equipped_outfit
    
    
    # equipped item type globals
    global equipped_top_type
    global equipped_bottom_type
    global equipped_dress_type
    global equipped_handheld_type
    global equipped_hat_type
    global equipped_face_type
    global equipped_backpiece_type
    global equipped_shoes_type
    global equipped_socks_type
    global equipped_outfit_type
    
    
    # equipped item theme globals
    global equipped_top_theme
    global equipped_bottom_theme
    global equipped_dress_theme
    global equipped_handheld_theme
    global equipped_hat_theme
    global equipped_face_theme
    global equipped_backpiece_theme
    global equipped_shoes_theme
    global equipped_socks_theme
    global equipped_outfit_theme
    
    
    
    # U/I
    print(" . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . \n ")

    print(f"                        {Player.username}'s \n ") 

    print("""                   
    █▀▀ ▄▀█ █▄░█ █▀▀ █▄█   █░█░█ ▄▀█ █▀█ █▀▄ █▀█ █▀█ █▄▄ █▀▀
    █▀░ █▀█ █░▀█ █▄▄ ░█░   ▀▄▀▄▀ █▀█ █▀▄ █▄▀ █▀▄ █▄█ █▄█ ██▄  \n """)

    print(" . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ .\n \n ")


    print("""                                  
                    ▀▀▀▄▄▄▄▄▄▄▀▀▀▄───                                
                ───█▒▒░░░░░░░░░▒▒█───                                
                ────█░░█░░░░░█░░█────                                
                ─▄▄──█░░░▀█▀░░░█──▄▄─                                
                █░░█─▀▄░░░░░░░▄▀─█░░█ - Time for a stylish change!  \n \n """)


    print("""
Welcome to your wardrobe you can try out different types of clothing that you have collected here!
fancy dresses, tee's, shoes, faces, pants you name it can be found here and if you wish to expand your
collection make sure to visit the clothing shops and purchase items you may like with bells! \n \n""")
    
    
    print("""

█▀▀ ▄▀█ █▀ █░█ █ █▀█ █▄░█
█▀░ █▀█ ▄█ █▀█ █ █▄█ █░▀█


Collect, Be snazzy, Be You!

    𝙩𝙤𝙥𝙨 \n """)
    
    print(f" [01] {pajama_top.name} \n ") 
    
    print(f" [02] {kuromi_tee.name} \n \n ")
    
    
    print("""
    
    𝙗𝙤𝙩𝙩𝙤𝙢𝙨 \n """)
    
    print(f" [03] {pajama_pants.name} \n ")

    print(f" [04] {dry_denim_skirt.name} \n ")
    
    
    print("""                                       

    𝘿𝙧𝙚𝙨𝙨𝙚𝙨                                               

You have not collected any dresses yet!



    𝙃𝙖𝙣𝙙𝙝𝙚𝙡𝙙 𝘼𝙘𝙘𝙚𝙨𝙨𝙤𝙧𝙞𝙚𝙨

You have not collected any Faces yet!



    𝙁𝙖𝙘𝙚

You have not collected any Faces yet!



    𝘽𝙖𝙘𝙠𝙥𝙞𝙚𝙘𝙚

You have not collected any backpieces yet!



    𝙎𝙝𝙤𝙚𝙨 \n """)
    
    print(f" [05] {blue_spring_moccasins.name} \n \n")                                  
    
    
    print("""
    
    𝙎𝙤𝙘𝙠𝙨 \n""")
    
    print(f" [06] {pajama_slippers.name}")
    print(f" [07] {bobby_socks.name} \n ")
    
    print("""                                         
    
    𝙊𝙪𝙩𝙛𝙞𝙩𝙨 \n """)
    
    print(f" [08] {starry_pajama_suit.name} \n ")
        
    notifcation() # wardrobe menu controls
    
    Cloners.Eloc_for_loop(2) # create spacial area with 2 print() functions!
    
    # exception handler 🕷
    try: # check code for execptions   
        
        # flow control statement for item catalog system
        while True: # while loop
            
            # user input
            response = str(input(">>> "))
            
            Cloners.Eloc_for_loop(1)
            
            
            # flow controls for item catalogs
            """ 𝐭𝐨𝐩𝐬 """
            if response == "01": # equip pajama top for player 
                
                # equipped clothing .wav w/pygame/mixer
                equip_fx(0.2)
                # check variable for values
                equipped_top
                
                # check item ownership
                if equipped_top == pajama_top.name: # in case if on already
                    
                    # in game dialog
                    print("You can't equip something you already have equipped!")
                    
                    # log info
                    logger.info(f"{Player.username} tried to equip {pajama_top.name} and has it on already!")
                    
                    Cloners.Eloc_for_loop(1)
                    
                    notifcation() # wardrobe menu controls
                    
                    continue
                    
                    pass # do nothing
                
                elif equipped_top != pajama_top.name: # equip it
                    
                    # equip pajama top
                    equipped_top = pajama_top.name
                    equip_fx()
                    
                    print(f"- {Player.username} puts on {pajama_top.name} -")
                    
                    notifcation() # wardrobe menu controls
                    
                    # exception handling
                    try:# check for value exceptions!
                        
                        # reaction speech to clothing change!
                        leaf_token(0, 5)
                        
                        # flow controls
                        if type(leaf_token) != int:
                            raise ValueError # raise exception if the token is not an integer.
                            pass

                        if leaf_token == 0: # leaf token landed on the (int) 0!
                            print(f"{Player.username}: Looks pretty snazzy! \n")
                            pass
                        
                        elif leaf_token == 1: # leaf token landed on the (int) 1!
                            print(f"{Player.username}: Why do I do this to myself..maybe I should try something else. \n")
                            pass
                        
                        elif leaf_token == 2: # leaf token landed on the (int) 2!
                            print(f"{Player.username}: Wow I'm a natrual at fashion! \n")
                            pass
                        
                        elif leaf_token == 3: # leaf token landed on the (int) 3!
                            print(f"{Player.username}: This is so me! \n")
                            pass
                        
                        elif leaf_token == 4: # leaf token landed on the (int)  4!
                            print(f"{Player.username}: Fabulous! \n")
                            pass
                        
                        elif leaf_token == 5: # leaf token landed on the (int) 5!
                            print(f"{Player.username}: Your looking good! \n")
                            pass
                        
                        else: 
                            
                            # [ERROR] [40]
                            logger.error(f"ERROR: The leaf_token gave the Value {leaf_token} and none of the flow control clauses were excecuted .")
                            pass
                        
                    except ValueError: # resolve ValueErrors
                        
                        # [ERROR] [40]
                        logger.error(f"ERROR: The leaf_token expects an int not str. Value given {leaf_token}.")
                        pass
                    
                    
                    Cloners.Eloc_for_loop(1) # (ELOC)

                    # log info
                    logger.info(f"{Player.username} equipped {pajama_top.name} ")
                    
                    continue 
                    
                else: # invalid values         
                    pass
            
            elif response == "02": # equip kuromi tee for player 
                
                # check variable for values
                equipped_top
                
                # flow controls for item catalogs
                if response == "02": # put on the pajama top for character
                    
                    # check variable for values
                    equipped_top
                    
                    # check item ownership
                    if equipped_top == kuromi_tee.name: # in case if on already
                        
                        # in game dialog
                        print("You can't equip something you already have equipped!")
                        
                        # log info
                        logger.info(f"{Player.username} tried to equip {kuromi_tee.name} and has it on already!")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                        
                        pass # do nothing
                    
                    elif equipped_top != kuromi_tee.name: # equip it 
                        
                        # equip kuromi tee
                        equipped_top = kuromi_tee.name
                        equip_fx()
                        
                        
                        print(f"- {Player.username} puts on {kuromi_tee.name} -")
                        
                        # log info
                        logger.info(f"{Player.username} equipped {kuromi_tee.name} ")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                        
                        break # escape while loop
                    
                    else: # invalid values
                        pass



            # bottoms
            elif response == "03": # equip pajama pants for player
                
                # check variable for values
                equipped_bottom
                
                # flow controls for item catalogs
                if response == "03": # put on the pajama top for character
                    
                    # check variable for values
                    equipped_bottom
                    
                    # check item ownership
                    if equipped_bottom == pajama_pants.name: # in case if on already
                        
                        # in game dialog
                        print("You can't equip something you already have equipped!")
                        
                        # log info
                        logger.info(f"{Player.username} tried to equip {pajama_pants.name} and has it on already!")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                        
                        pass # do nothing
                    
                    elif equipped_bottom != pajama_pants.name: # equip it 
                        
                        # equip kuromi tee
                        equipped_bottom = pajama_pants.name
                        # equipped clothing .wav w/pygame/mixer
                        equip_fx()
                        
                        print(f"- {Player.username} puts on {pajama_pants.name} -")
                        
                        # log info
                        logger.info(f"{Player.username} equipped {pajama_pants.name} ")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                    
                    else: # invalid values
                        pass


            elif response == "04": # equip dry denim skirt for player
                
                # check variable for values
                equipped_bottom
                
                # flow controls for item catalogs
                if response == "04": # put on the dry denim skirt for player
                    
                    # check variable for values
                    equipped_bottom
                    
                    # check item ownership
                    if equipped_bottom == dry_denim_skirt.name: # in case if on already
                        
                        # in game dialog
                        print("You can't equip something you already have equipped!")
                        
                        # log info
                        logger.info(f"{Player.username} tried to equip {dry_denim_skirt.name} and has it on already!")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                        
                        pass # do nothing
                    
                    elif equipped_bottom != dry_denim_skirt.name: # equip it 
                        
                        # equip kuromi tee
                        equipped_bottom = dry_denim_skirt.name
                        equip_fx()
                        
                        # equipped clothing .wav w/pygame/mixer
                        equip_fx()
                        
                        print(f"- {Player.username} puts on {dry_denim_skirt.name} -")
                        
                        # log info
                        logger.info(f"{Player.username} equipped {dry_denim_skirt.name} ")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue # (RI)
                    
                    else: # invalid values
                        pass


            
            # shoes
            elif response == "05": # equip blue spring moccasins for player
                
                # check variable for values
                equipped_shoes
                
                # flow controls for item catalogs
                if response == "05": # put on the blue spring moccasins for player
                    
                    # check variable for values
                    equipped_shoes
                    
                    # check item ownership
                    if equipped_shoes == blue_spring_moccasins.name: # in case if on already
                        
                        # in game dialog
                        print("You can't equip something you already have equipped!")
                        
                        # log info
                        logger.info(f"{Player.username} tried to equip {blue_spring_moccasins.name} and has it on already!")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                        
                        pass # do nothing
                    
                    elif equipped_shoes != blue_spring_moccasins.name: # equip it 
                        
                        # equip blue spring moccasins shoe
                        equipped_shoes = blue_spring_moccasins.name
                        equip_fx()
                        
                        print(f"- {Player.username} puts on {blue_spring_moccasins.name} -")
                        
                        # log info
                        logger.info(f"{Player.username} equipped {blue_spring_moccasins.name} ")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                    
                    else: # invalid values
                        pass

            
            
            # socks 
            elif response == "06": # equip pajama slippers for player
                
                # check variable for values
                equipped_socks
                
                # flow controls for item catalogs
                if response == "06": # put on the blue spring moccasins for player
                    
                    # check variable for values
                    equipped_socks
                    
                    # check item ownership
                    if equipped_socks == pajama_slippers.name: # in case if on already
                        
                        # in game dialog
                        print("You can't equip something you already have equipped!")
                        
                        # log info
                        logger.info(f"{Player.username} tried to equip {pajama_slippers.name} and has it on already!")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                        
                        pass # do nothing
                    
                    elif equipped_socks != pajama_slippers.name: # equip it 
                        
                        # equip pajama slippers
                        equipped_socks = pajama_slippers.name
                        equip_fx()
                        
                        print(f"- {Player.username} puts on {pajama_slippers.name} -")
                        
                        # log info
                        logger.info(f"{Player.username} equipped {pajama_slippers.name} ")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                    
                    else: # invalid values
                        pass

            elif response == "07": # equip bobby socks for player
                
                # check variable for values
                equipped_socks
                
                # flow controls for item catalogs
                if response == "07": # put on the bobby socks for player
                    
                    # check variable for values
                    equipped_socks
                    
                    # check item ownership
                    if equipped_socks == bobby_socks.name: # in case if on already
                        
                        # in game dialog
                        print("You can't equip something you already have equipped!")
                        
                        # log info
                        logger.info(f"{Player.username} tried to equip {bobby_socks.name} and has it on already!")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                        
                        pass # do nothing
                    
                    elif equipped_socks != bobby_socks.name: # equip it 
                        
                        # equip bobby socks
                        equipped_socks = bobby_socks.name
                        equip_fx()
                        
                        print(f"- {Player.username} puts on {bobby_socks.name} -")
                        
                        # log info
                        logger.info(f"{Player.username} equipped {bobby_socks.name} ")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                    
                    else: # invalid values
                        pass


            # outfits
            elif response == "08": # equip starry pajama suit for character
                
                # check variable for values
                equipped_socks
                
                # flow controls for item catalogs
                if response == "08": # put on the starry pajama suit for player
                    
                    # check variable for values
                    equipped_outfit
                    
                    # check item ownership
                    if equipped_outfit == starry_pajama_suit.name: # in case if on already
                        
                        # in game dialog
                        print("You can't equip something you already have equipped!")
                        
                        # log info
                        logger.info(f"{Player.username} tried to equip {starry_pajama_suit.name} and has it on already!")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                        
                        pass # do nothing
                    
                    elif equipped_outfit != starry_pajama_suit.name: # equip it 
                        
                        # equip starry pajama suit
                        equipped_outfit = starry_pajama_suit.name
                        equip_fx()
                        
                        print(f"- {Player.username} puts on {starry_pajama_suit.name} -")
                        
                        # log info
                        logger.info(f"{Player.username} equipped {starry_pajama_suit.name} ")
                        
                        Cloners.Eloc_for_loop(1)
                        
                        notifcation() # wardrobe menu controls
                        
                        continue
                    
                    else: # invalid values
                        error_wav()
                        pass

            
            elif response == "d": # re-display wardrobe menu!
                
                # U/I
                print("               . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ .      \n ")

                print(f"                                     {Player.username}'s                     \n ") 

                print("""                   
                                        █▀▀ ▄▀█ █▄░█ █▀▀ █▄█   █░█░█ ▄▀█ █▀█ █▀▄ █▀█ █▀█ █▄▄ █▀▀
                                        █▀░ █▀█ █░▀█ █▄▄ ░█░   ▀▄▀▄▀ █▀█ █▀▄ █▄▀ █▀▄ █▄█ █▄█ ██▄  
                    \n """)

                print("               . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ .\n \n ")


                print("""                                   ▀▀▀▄▄▄▄▄▄▄▀▀▀▄───                                
                                                        ───█▒▒░░░░░░░░░▒▒█───                                
                                                        ────█░░█░░░░░█░░█────                                
                                                        ─▄▄──█░░░▀█▀░░░█──▄▄─                                
                                                        █░░█─▀▄░░░░░░░▄▀─█░░█ - Time for a stylish change!  \n \n """)


                print("""Welcome to your wardrobe you can try out different types of clothing that you have collected here!
                fancy dresses, tee's, shoes, faces, pants you name it can be found here and if you wish to expand your
                collection make sure to visit the clothing shops and purchase items you may like with bells!
                """)


                print("""                                       
                                                        █▀▀ ▄▀█ █▀ █░█ █ █▀█ █▄░█
                                                        █▀░ █▀█ ▄█ █▀█ █ █▄█ █░▀█


                                                        Collect, Be snazzy, Be You!

                                                                𝙩𝙤𝙥𝙨                                            \n """)

                print(f"                                [01] {pajama_top.name}                                    \n ") 

                print(f"                                [02] {kuromi_tee.name}                                 \n \n ")


                print("                                         𝙗𝙤𝙩𝙩𝙤𝙢𝙨                                           \n ")

                print(f"                                [03] {pajama_pants.name}                                  \n ")

                print(f"                                [04] {dry_denim_skirt.name}                               \n ")


                print("""                                       𝘿𝙧𝙚𝙨𝙨𝙚𝙨                                               

                                                    You have not collected any dresses yet!



                                                                𝙃𝙖𝙣𝙙𝙝𝙚𝙡𝙙 𝘼𝙘𝙘𝙚𝙨𝙨𝙤𝙧𝙞𝙚𝙨

                                                    You have not collected any Faces yet!



                                                                𝙁𝙖𝙘𝙚

                                                    You have not collected any Faces yet!



                                                                𝘽𝙖𝙘𝙠𝙥𝙞𝙚𝙘𝙚

                                                    You have not collected any backpieces yet!



                                                                𝙎𝙝𝙤𝙚𝙨
                                                    \n """)

                print(f"                                [05] {blue_spring_moccasins.name}                       \n \n ")                                  


                print("                                                𝙎𝙤𝙘𝙠𝙨                                        \n")

                print(f"                                [06] {pajama_slippers.name}                                   ")
                print(f"                                [07] {bobby_socks.name}                                    \n ")

                print("                                                𝙊𝙪𝙩𝙛𝙞𝙩𝙨                                      \n ")

                print(f"                                 [08] {starry_pajama_suit.name}                            \n ")

                notifcation() # wardrobe menu controls
                Cloners.Eloc_for_loop(4) # create spacial area with 4 print() functions!
                pass
            
            elif response == "x": # user exits wardrobe
                
                # log info
                logger.info(f"{Player.username} exited wardrobe!")
                Cloners.Eloc_for_loop(1)
                break # escape loop w/break statement
                pass
            
            elif response == " ": # user gave no input
                pass # null, nill, pass
        
            else:
                pass
            
                print(f"notification alert!: The catalog {input} does not exist")

                Cloners.Eloc_for_loop(1)
                Pause.Execution_delay(3)
                continue # (RI) re-iterate

    except ValueError: # log exception 
        
        # log debug
        logger.debug(f"{Player.username} has input an invalid datatype 'integer'")
        pass

def character_menu(): 
    
    # doc string
    """ A graphical user interface that allows the player to view their name, equipped items, levels, experience points,
    next level ,location."""
    
    # character U/I intergration
    print("""   

            𝔞𝔫𝔦𝔪𝔞𝔩 𝔠𝔯𝔬𝔰𝔰𝔦𝔫𝔤 𝔭𝔬𝔠𝔨𝔢𝔱 𝔠𝔞𝔪𝔭 
        
        █▀▀ █░█ ▄▀█ █▀█ ▄▀█ █▀▀ ▀█▀ █▀▀ █▀█
        █▄▄ █▀█ █▀█ █▀▄ █▀█ █▄▄ ░█░ ██▄ █▀▄
        
        . - - - - - - - - - - - - - - - - - .
        Name: {Player.username} 
        LVL: {current_level}
        Nxt LVL: {next_level}
        Friendship LVL: {current_friendship_level}
        Nxt Friendship LVL: {next_friendship_level}
        Exp: {current_xp_level}
        Friendship LVL Exp: {friendship_xp_level} 
        
        Location: {player_location} 
        
        
        Items
        Top: {equipped_top} Theme: {equipped_top_theme} 
        Bottoms: {equipped_bottom} Theme: {equipped_bottom_theme}
        Dress: {equipped_dress} Theme: {equipped_dress_theme}
        Hand: {equipped_handheld} Theme: {equipped_handheld_theme}
        Hat: {equipped_hat} Theme: {equipped_hat_theme}
        Face: {equipped_face} Theme: {equipped_face_theme}
        Back: {equipped_backpiece} Theme: {equipped_backpiece_theme}
        Shoes: {equipped_shoes} Theme: {equipped_shoes_theme}
        Socks: {equipped_socks} Theme: {equipped_socks_theme}
        Outfit: {equipped_outfit} Theme: {equipped_outfit_theme}
        
        
        . - - - - - - - - - - - - - - - - - .
        """)
    
    Cloners.Eloc_for_loop(2) # Prints print() and clones to create 2 blank lines in the program
    pass


# NPC dialog functions
def npc_dialog(character: str = "", speech: str = ""): 
    
    # doc string
    """ NPC dialog generator that uses the optional parameters 'character' for assigning the NPC name and the 'speech' parameter
    or implementing the text the NPC will say to user!"""
    
    # character speech dialog
    print(f"{character}: {speech}")
    
    Cloners.Eloc_for_loop(1) # (ELOC)
    
    pass

def kk_slider_dialog_randomizer(): 
    
    # doc string
    """ A dialog randomizer for KK slider that uses the leaf_token() function and outputs different strings with phrases!"""
    
    # random integer variable
    leaf_token = int(random.randint(0, 2))
    
    """ leaf token info

        ╭╮╱╱╱╱╱╱╱╭━╮╱╭╮╱╱╱╭╮
        ┃┃╱╱╱╱╱╱╱┃╭╯╭╯╰╮╱╱┃┃
        ┃┃╭━━┳━━┳╯╰╮╰╮╭╋━━┫┃╭┳━━┳━╮
        ┃┃┃┃━┫╭╮┣╮╭╯╱┃┃┃╭╮┃╰╯┫┃━┫╭╮╮
        ┃╰┫┃━┫╭╮┃┃┃╱╱┃╰┫╰╯┃╭╮┫┃━┫┃┃┃
        ╰━┻━━┻╯╰╯╰╯╱╱╰━┻━━┻╯╰┻━━┻╯╰╯

        The leaf token is a random token that generates random integers from 0 to 5 and can be used to add randomizations
        to speech or other elements within the game.

        """
    
    # flow conditions
    if leaf_token == 0:
        
        # KK Slider game dialog
        npc_dialog(KK_SLIDER , f" {Player.username}? thats a cool name")
        
        prompt_sound()
        
        Cloners.Eloc_for_loop(1)
    
    if leaf_token == 1:
        
        # KK Slider game dialog
        npc_dialog(KK_SLIDER, f"{Player.username}? meh.")
        
        prompt_sound()
    
    if leaf_token == 2:
        
        # KK Slider game dialog
        npc_dialog(KK_SLIDER, f"That name is really rad! nice to meet ya {Player.username}")
        
        prompt_sound()
    
    else: 
        pass # null, nill, do nothing just pass through!

def load_number_token_generator(): 
    
    # doc string
    """ generates random integers and random loading messages! """
    
    
    # random integer variable
    leaf_token = int(random.randint(0, 10))
    
    """ leaf token info

        ╭╮╱╱╱╱╱╱╱╭━╮╱╭╮╱╱╱╭╮
        ┃┃╱╱╱╱╱╱╱┃╭╯╭╯╰╮╱╱┃┃
        ┃┃╭━━┳━━┳╯╰╮╰╮╭╋━━┫┃╭┳━━┳━╮
        ┃┃┃┃━┫╭╮┣╮╭╯╱┃┃┃╭╮┃╰╯┫┃━┫╭╮╮
        ┃╰┫┃━┫╭╮┃┃┃╱╱┃╰┫╰╯┃╭╮┫┃━┫┃┃┃
        ╰━┻━━┻╯╰╯╰╯╱╱╰━┻━━┻╯╰┻━━┻╯╰╯

        The leaf token is a random token that generates random integers from 0 to 5 and can be used to add randomizations
        to speech or other elements within the game.

        """
    
    # flow controls/conditions for token
    if leaf_token == 0: # if token is equal to 0 execute the clause
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("have a great day!")
        pass
    
    elif leaf_token == 1: # if token is equal to 1 execute the clause
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("to be the best believe your the best!")
        pass
    
    elif leaf_token == 2: # if token is equal to 2 execute the clause
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("you can purchase new items and clothes with bells!")
        pass
    
    elif leaf_token == 3: # if token is equal to 3 execute the clause
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("make sure to drink plenty of water while coding!")
        pass
    
    elif leaf_token == 4: 
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("help planet earth by not litering and conserving energy!")
        pass
    
    elif leaf_token == 5: 
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("get stylish with bells!")
        pass
    
    elif leaf_token == 6: 
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("open your mind and access your potential!")
        pass
    
    elif leaf_token == 7: 
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("mario is a cross over in animal crossing did you know?")
        pass
    
    elif leaf_token == 8: 
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("get plenty of rest, studying is important but the brain needs rest!")
        pass
    
    elif leaf_token == 9: 
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("make sure to visit my github by searching for GenesisGir on the platform!")
        pass
    
    elif leaf_token == 10: 
        
        Cloners.Eloc_for_loop(1)
        
        # display message
        print("perfectionism can ruin or make your creations never finish, have fun.")
        pass

def load(): 
    
    # doc string
    """ A basic loading screen emulating loading screens with the time.sleep() function imported from the time() module
    that displays arbitrary messages."""
    
    # loading U/I
    print("""
        
        ⓐ ⓝ ⓘ ⓜ ⓐ ⓛ  ⓒ ⓡ ⓞ ⓢ ⓢ ⓘ ⓝ ⓖ   ⓐ ⓝ ⓘ ⓜ ⓐ ⓛ  ⓒ ⓡ ⓞ ⓢ ⓢ ⓘ ⓝ ⓖ   ⓐ ⓝ ⓘ ⓜ ⓐ ⓛ  ⓒ ⓡ ⓞ ⓢ ⓢ ⓘ ⓝ ⓖ   ⓐ ⓝ ⓘ ⓜ ⓐ ⓛ  ⓒ ⓡ ⓞ ⓢ ⓢ ⓘ ⓝ ⓖ
        
                                ▄▀█ █▄░█ █ █▀▄▀█ ▄▀█ █░░   █▀▀ █▀█ █▀█ █▀ █▀ █ █▄░█ █▀▀
                                █▀█ █░▀█ █ █░▀░█ █▀█ █▄▄   █▄▄ █▀▄ █▄█ ▄█ ▄█ █ █░▀█ █▄█
    
                                . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . ✿ x ✿ . 
    
                                                █░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀
                                                █▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█
                                                
                                                🝗𝓝丿ㄖ丫 丫ㄖㄩ尺 丂七闩丫
                                                
                                                
                                                
        ⓐ ⓝ ⓘ ⓜ ⓐ ⓛ  ⓒ ⓡ ⓞ ⓢ ⓢ ⓘ ⓝ ⓖ   ⓐ ⓝ ⓘ ⓜ ⓐ ⓛ  ⓒ ⓡ ⓞ ⓢ ⓢ ⓘ ⓝ ⓖ   ⓐ ⓝ ⓘ ⓜ ⓐ ⓛ  ⓒ ⓡ ⓞ ⓢ ⓢ ⓘ ⓝ ⓖ   ⓐ ⓝ ⓘ ⓜ ⓐ ⓛ  ⓒ ⓡ ⓞ ⓢ ⓢ ⓘ ⓝ ⓖ
        \n """)
    
    """ # buffer info
    🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
    
    
    
    █▄▄ █░█ █▀▀ █▀▀ █▀▀ █▀█   █▀ █▄█ █▀ ▀█▀ █▀▀ █▀▄▀█
    █▄█ █▄█ █▀░ █▀░ ██▄ █▀▄   ▄█ ░█░ ▄█ ░█░ ██▄ █░▀░█

    The buffer system allows you to pull up a loading screen at ease by no means
    is this an actual loading screen! Its being used as an illusion with the use of
    for loops, the buffer variable keeps tracks of the iterations inside the function.
    
    ⣿⣯⣿⣟⣟⡼⣿⡼⡿⣷⣿⣿⣿⠽⡟⢋⣿⣿⠘⣼⣷⡟⠻⡿⣷⡼⣝⡿⡾⣿
    ⣿⣿⣿⣿⢁⣵⡇⡟⠀⣿⣿⣿⠇⠀⡇⣴⣿⣿⣧⣿⣿⡇⠀⢣⣿⣷⣀⡏⢻⣿
    ⣿⣿⠿⣿⣿⣿⠷⠁⠀⠛⠛⠋⠀⠂⠹⠿⠿⠿⠿⠿⠉⠁⠀⠘⠛⠛⠛⠃⢸⣯
    ⣿⡇⠀⣄⣀⣀⣈⣁⠈⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠠⠎⠈⠀⣀⣁⣀⣀⡠⠈⠉
    ⣿⣯⣽⡿⢟⡿⠿⠛⠛⠿⣶⣄⠀⠀⠀⠀⠀⠀⠈⢠⣴⣾⠛⠛⠿⠻⠛⠿⣷⣶
    ⣿⣿⣿⠀⠀⠀⣿⡿⣶⣿⣫⠉⠀⠀⠀⠀⠀⠀⠀⠈⠰⣿⠿⠾⣿⡇⠀⠀⢺⣿
    ⣿⣿⠻⡀⠀⠀⠙⠏⠒⡻⠃⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠐⡓⢚⠟⠁⠀⠀⡾⢫
    ⣿⣿⠀⠀⡀⠀⠀⡈⣉⡀⡠⣐⣅⣽⣺⣿⣯⡡⣴⣴⣔⣠⣀⣀⡀⢀⡀⡀⠀⣸
    ⣿⣿⣷⣿⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⢾⣷⣿
    ⣿⣿⣟⠫⡾⠟⠫⢾⠯⡻⢟⡽⢶⢿⣿⣿⡛⠕⠎⠻⠝⠪⢖⠝⠟⢫⠾⠜⢿⣿
    ⣿⣿⣿⠉⠀⠀⠀⠀⠈⠀⠀⠀⠀⣰⣋⣀⣈⣢⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⢸⣿
    ⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿
    ⣿⣿⣿⣿⣦⡔⠀⠀⠀⠀⠀⠀⢻⣿⡿⣿⣿⢽⣿⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿
    ⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠘⠛⢅⣙⣙⠿⠉⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣅⠀⠓⠀⠀⣀⣠⣴⣺⣿⣿⣿⣿⣿⣿⣿⣿
    
    
    🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂
    """

    # hint flow control statements
    for buff in range(0, 101, 10): # for loop buffer 
        
        # loading time
        Pause.Execution_delay(random.randint(1, 2)) # delay execution by a random int!
        
        
        # U/I for progress
        print(f"Animal crossing {buff}%") # percentage of the U/I
        
        
        # flows & condition
        if buff == 0: # percentage has reached 0%
            
            load_number_token_generator()
        
        elif buff == 20: # percentage has reached 20%
            
            load_number_token_generator()
            
        elif  buff == 30: # percentage has reached 30%
            
            load_number_token_generator()
        
        elif  buff == 50: # percentage has reached 50%
            
            load_number_token_generator()
        
        elif  buff == 80: # percentage has reached 80%
            
            load_number_token_generator()

        elif  buff == 100: # percentage has reached finished loading!
            
            Cloners.Eloc_for_loop(2)
            
            break 

def controller_prompt():
# doc string
    """ A prompt that prompts user to press enter using the input() function. And only retrieves '' as a value to continue any other
    values are dismissed and re-iterates the while loop to prompt user to press the enter key only to progress.
    """
    
    # loop
    while True:

        response = input("[press enter]") # retrieve user input data
        
        if response ==  '': # condition for correct input value for prompt
            Cloners.Eloc_for_loop(1)
            prompt_sound() # prompt sound
            break
            pass
        
        elif response == response.isalpha: # re-iterate if Alpha's are entered
            continue
            pass
        
        elif response == response.isascii: # re-iterate if ASCII are entered
            continue
            pass
        
        elif response == response.isalnum: # re-iterate if Alphabetical or numerical values are entered
            continue
            pass
        
        elif response == response.isdigit: # re-iterate if numerical values are entered
            continue
            pass
        
        else:
            continue


# more functionalites will be added in this section ^

# leveling up player level
def level_up(desired_xp):
    
    # doc string
    """ Levels up the player with an experinece point system! """
    
    # variables 📦
    current_level = current_level
    next_level = next_level
    xp_level = xp_level
    user = Player.username
    
    # log info
    logger.info("variables defined for the level_up() function successfully")
    
    # constants
    default_xp = 0
    
    # flow controls
    
    # level up mechanism
    while xp_level != desired_xp:
        
        # flow
        if xp_level == desired_xp:

            # Camp Manager Level inceased!
            current_level += 1
            
            print(user + " has leveled up!")

            # experience level reset
            xp_level = 0
            
            break
        
        elif xp_level == default_xp:
            break
        
    else: # do nothing!
        
        pass # null statement essentially
    
    # log info
    logger.info("level_up() function iterated/ran successfully")

# experience point gain
def exp_gain(xp: int = 0): 
    
    # doc string
    """ user gains experience points set by the exp parameter """
    
    # variables 📦
    current_level = current_level
    next_level = next_level
    xp_level = xp_level
    
    # gained exp set by the arguement of function!
    xp_level + xp
    
    print("+" + str(xp) + " experience gained!")
    
    # log info
    logger.info("exp_gain() function iterated/ran successfully")
    
    pass


# leveling up friendship level
def friendship_level_up(desired_xp: int = 0):
    
    # doc string
    """ friendship level increases set by the desired_xp parameter """
    
    # variables 📦
    current_friendship_level = current_friendship_level
    next_level = next_friendship_level
    friendship_xp_level = friendship_xp_level
    user = Player.username
    
    # constants
    default_xp = 0
    
    # flow controls
    
    # friendship level up mechanism
    while friendship_xp_level != desired_xp:
        
        # flow
        if friendship_xp_level == desired_xp:

            # friendship Level increased!
            next_level +=  1 # using an augmented operator to add an additional point
            
            print(user + "'s friendships level has increased!")

            # experience level reset
            xp_level = 0
            
            break
        
        elif xp_level == default_xp:
            break

    else: # do nothing!
        pass # null statement essentially
    
    # log info
    logger.info("friendship_level_up() function iterated/ran successfully")

# friendship experience point gain
def friendship_exp_gain(xp: int = 0): # user has gained friendship exp
    
    # doc string
    """ friendship experience increases set by the desired_xp parameter """
    
    # variables 📦
    current_friendship_level = current_friendship_level
    next_level = next_friendship_level
    friendship_xp_level = friendship_xp_level
    
    
    # gained  friendship exp set by the arguement of function!
    friendship_xp_level + xp
    
    print("+" + str(xp) + " friendship experience gained!")
    
    # log info
    logger.info("friendship_exp_gain() function iterated/ran successfully")
    
    pass