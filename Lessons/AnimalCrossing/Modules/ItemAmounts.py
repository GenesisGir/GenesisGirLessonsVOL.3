"""

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
                                    
                                    
                            █ ▀█▀ █▀▀ █▀▄▀█   ▄▀█ █▀▄▀█ █▀█ █░█ █▄░█ ▀█▀ █▀
                            █ ░█░ ██▄ █░▀░█   █▀█ █░▀░█ █▄█ █▄█ █░▀█ ░█░ ▄█
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                Item amounts from within the game and item amount resources and their classes are on this script
                edit them, Add, Remove them here.

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

""" 𝗶𝘁𝗲𝗺 𝗮𝗺𝗼𝘂𝗻𝘁𝘀 """
class Clothing_amounts():
    
    # doc string
    """Track clothing (int) amounts!"""
    
    #constants
    global DEFAULT_AMOUNT
    DEFAULT_AMOUNT = 0
    
    class Top_amounts():
        
        # globals
        global kuromi_tee_amount
        global academic_hha_jacket_amount
        global aqua_polka_tee_amount
        global aqua_spring_outerwear_amount
        global usahana_tee_amount
        
        # log info
        logger.info("Top_amounts global statements were defined successfully")
        
        # top amounts variables
        kuromi_tee_amount = DEFAULT_AMOUNT
        academic_hha_jacket_amount = DEFAULT_AMOUNT
        aqua_polka_tee_amount = DEFAULT_AMOUNT
        aqua_spring_outerwear_amount = DEFAULT_AMOUNT
        usahana_tee_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Top_amounts variables were defined successfully")

    class Bottom_amounts():
        
        # globals
        global black_formal_pants_amount
        global bone_pants_amount
        global dry_denim_skirt_amount
        global lavender_chiffon_skirt_amount
        global isabelles_skirt_amount
        
        # log info
        logger.info("Bottom_amounts global statements were defined successfully")
        
        # bottom amounts
        black_formal_pants_amount = DEFAULT_AMOUNT 
        bone_pants_amount = DEFAULT_AMOUNT 
        dry_denim_skirt_amount = DEFAULT_AMOUNT 
        lavender_chiffon_skirt_amount = DEFAULT_AMOUNT 
        isabelles_skirt_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Bottom_amounts variables were defined successfully")

    class Dress_amounts():
        
        # globals
        global black_sailor_pinafore_amount
        global black_sakura_hakama_amount
        global black_yukata_dress_amount
        global blue_mail_room_dress_amount
        global blue_tuxedo_set_amount
        
        # log info
        logger.info("Dress_amounts global statements were defined successfully")

        # dress amounts
        black_sailor_pinafore_amount = DEFAULT_AMOUNT
        black_sakura_hakama_amount = DEFAULT_AMOUNT
        black_yukata_dress_amount = DEFAULT_AMOUNT
        blue_mail_room_dress_amount = DEFAULT_AMOUNT
        blue_tuxedo_set_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Dress_amounts variables were defined successfully")

    class Handheld_accessory_amounts():
        
        # globals
        global berry_ice_cream_cone
        global black_purrfect_plushie
        global green_watering_can
        global gudetama_fan
        global handheld_can_of_soda
        
        # log info
        logger.info("Handheld_accessory_amounts global statements were defined successfully")
        
        # handheld accessory amounts
        berry_ice_cream_cone_amount = DEFAULT_AMOUNT
        black_purrfect_plushie_amount = DEFAULT_AMOUNT
        green_watering_can_amount = DEFAULT_AMOUNT
        gudetama_fan_amount = DEFAULT_AMOUNT
        handheld_can_of_soda_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Handheld_accessory_amounts variables were defined successfully")

    class Hat_amounts():
        
        # globals
        global angelic_wig_amount
        global apple_stem_amount
        global black_ram_horn_wig_amount
        global blue_ombre_antler_wig_amount
        global bunny_hood_amount
        
        # log info
        logger.info("Hat_amounts global statements were defined successfully")
        
        # hat amounts
        angelic_wig_amount = DEFAULT_AMOUNT
        apple_stem_amount = DEFAULT_AMOUNT
        black_ram_horn_wig_amount = DEFAULT_AMOUNT
        blue_ombre_antler_wig_amount = DEFAULT_AMOUNT
        bunny_hood_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Hat_amounts variables were defined successfully")

    class Face_amounts():
        
        # globals
        global black_jewel_thief_mask_amount
        global doctors_mask_amount
        global halloween_face_paint_amount
        global post_op_patch_amount
        global snowy_crystal_earrings_amount
        
        # log info
        logger.info("Face_amounts global statements were defined successfully")
        
        # face amounts
        black_jewel_thief_mask_amount = DEFAULT_AMOUNT
        doctors_mask_amount = DEFAULT_AMOUNT
        halloween_face_paint_amount = DEFAULT_AMOUNT
        post_op_patch_amount = DEFAULT_AMOUNT
        snowy_crystal_earrings_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Face_amounts variables were defined successfully")

    class Backpiece_amounts():
        
        # globals
        global angelic_wings_amount
        global bat_friends_amount
        global black_kitty_backpack_amount
        global blue_hydrangea_obi_amount
        global dark_angel_wings_amount
        
        # log info
        logger.info("Backpiece_amounts global statements were defined successfully")
        
        # backpiece amounts
        angelic_wings_amount = DEFAULT_AMOUNT
        bat_friends_amount = DEFAULT_AMOUNT
        black_kitty_backpack_amount = DEFAULT_AMOUNT
        blue_hydrangea_obi_amount = DEFAULT_AMOUNT
        dark_angel_wings_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Backpiece_amounts variables were defined successfully")

    class Shoe_amounts():
        
        # globals
        global blue_spring_moccasins_amount
        global brown_santa_boots_amount
        global lavender_pumps_amount
        global pastel_purple_pumps_amount
        global pink_rubber_rain_boots_amount
        
        # log info
        logger.info("Shoe_amounts global statements were defined successfully")
        
        # shoe amounts
        blue_spring_moccasins_amount = DEFAULT_AMOUNT
        brown_santa_boots_amount = DEFAULT_AMOUNT
        lavender_pumps_amount = DEFAULT_AMOUNT
        pastel_purple_pumps_amount = DEFAULT_AMOUNT
        pink_rubber_rain_boots_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Shoe_amounts variables were defined successfully")

    class Sock_amounts():
        
        # globals
        global black_stockings_amount
        global bobby_socks_amount
        global crimson_striped_socks_amount
        global purple_star_socks_amount
        global white_stockings_amount
        
        # log info
        logger.info("Sock_amounts global statements were defined successfully")
        
        # sock amounts
        black_stockings_amount = DEFAULT_AMOUNT
        bobby_socks_amount = DEFAULT_AMOUNT
        crimson_striped_socks_amount = DEFAULT_AMOUNT
        purple_star_socks_amount = DEFAULT_AMOUNT
        white_stockings_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Sock_amounts variables were defined successfully")
        
        pass
    
    class Outfit_amounts():
        
        # globals
        global animal_crossing_ski_suit
        global mario_outfit
        global eevee_costume
        global foxtail_dress
        global zipper_costume
        
        # log info
        logger.info("Outfit_amounts global statements were defined successfully")
        
        # outfit amounts
        animal_crossing_ski_suit = DEFAULT_AMOUNT
        mario_outfit = DEFAULT_AMOUNT
        eevee_costume = DEFAULT_AMOUNT
        foxtail_dress = DEFAULT_AMOUNT
        zipper_costume = DEFAULT_AMOUNT
        
        # log info
        logger.info("Outfit_amounts variables were defined successfully")
        
        pass

class Item_amounts():
    
    # doc string
    """ Item amounts for the item integers within the game."""
    
    class Bug_amounts():
        
        # doc string
        """ Bug amounts within the game."""
        
        # globals
        global tiger_butterfly_amount
        global giant_cicada_amount
        global darner_dragonfly_amount
        global horned_dynastid_amount
        global white_tailed_skimmer_amount
        global saw_stag_amount
        global emperor_butterfly_amount
        global banded_dragonfly_amount
        global horned_atlas_amount
        global golden_stag_amount

        # log info
        logger.info("Bug_amounts global statements were defined successfully")

        # bug amounts (DEAFULT AMOUNT Constants = 0)
        tiger_butterfly_amount = DEFAULT_AMOUNT
        giant_cicada_amount = DEFAULT_AMOUNT
        darner_dragonfly_amount = DEFAULT_AMOUNT
        horned_dynastid_amount = DEFAULT_AMOUNT
        white_tailed_skimmer_amount = DEFAULT_AMOUNT
        saw_stag_amount = DEFAULT_AMOUNT
        emperor_butterfly_amount = DEFAULT_AMOUNT
        banded_dragonfly_amount = DEFAULT_AMOUNT
        horned_atlas_amount = DEFAULT_AMOUNT
        golden_stag_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Bug_amounts variables were defined successfully")

    class Fish_amounts():
        
        # doc string
        """ Fish amounts within the game."""
        
        # globals
        global CRUCIAN_CARP_AMOUNT
        global PALE_CHUB_AMOUNT
        global BLUEGILL_AMOUNT
        global BLACK_BASS_AMOUNT
        global EEL_AMOUNT
        global FROG_AMOUNT
        global POP_EYED_GOLDFISH_AMOUNT
        global SWEETFISH_AMOUNT
        global GAR_AMOUNT
        global KOI_AMOUNT
        
        # log info
        logger.info("Fish_amounts global statements were defined successfully")
        
        
        # fish amounts
        crucian_carp_amount = DEFAULT_AMOUNT
        pale_chub_amount = DEFAULT_AMOUNT
        bluegill_amount = DEFAULT_AMOUNT
        black_bass_amount = DEFAULT_AMOUNT
        eel_amount = DEFAULT_AMOUNT
        frog_amount = DEFAULT_AMOUNT
        pop_eyed_goldfish_amount = DEFAULT_AMOUNT
        sweetfish_amount = DEFAULT_AMOUNT
        gar_amount = DEFAULT_AMOUNT
        koi_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Fish_amounts variables were defined successfully")

    class Fruit_amounts():
        
        # doc string
        """ Fruit amounts within the game."""
        
        # globals
        global cherry_amount
        global pear_amount
        global peach_amount
        global orange_amount
        global coconut_amount
        global apple_amount
        global lemon_amount
        global lychee_amount
        global grapes_amount
        global perfect_apple_amount
        
        # log info
        logger.info("Fruit_amounts global statements were defined successfully")
        
        
        # fruit amounts
        cherry_amount = DEFAULT_AMOUNT
        pear_amount = DEFAULT_AMOUNT
        peach_amount = DEFAULT_AMOUNT
        orange_amount = DEFAULT_AMOUNT
        coconut_amount = DEFAULT_AMOUNT
        apple_amount = DEFAULT_AMOUNT
        lemon_amount = DEFAULT_AMOUNT
        lychee_amount = DEFAULT_AMOUNT
        grapes_amount = DEFAULT_AMOUNT
        perfect_apple_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Fruit_amounts variables were defined successfully")

    class Shell_amounts():
        
        # doc string
        """ Shell amounts within the game."""
        
        # globals
        global coral_amount
        global sea_star_amount
        global scallop_shell_amount
        global pearl_oyster_shell_amount
        global grand_oyster_amount
        global angel_wing_clam_amount
        global pink_heart_cockle_amount
        global conch_shell_amount
        global violet_sea_snail_amount
        global razor_clam_amount
        
        # log info
        logger.info("Shell_amounts global statements were defined successfully")
        
        # shell amounts
        coral_amount = DEFAULT_AMOUNT
        sea_star_amount = DEFAULT_AMOUNT
        scallop_shell_amount = DEFAULT_AMOUNT
        pearl_oyster_shell_amount = DEFAULT_AMOUNT
        grand_oyster_amount = DEFAULT_AMOUNT
        angel_wing_clam_amount = DEFAULT_AMOUNT
        pink_heart_cockle_amount = DEFAULT_AMOUNT
        conch_shell_amount = DEFAULT_AMOUNT
        violet_sea_snail_amount = DEFAULT_AMOUNT
        razor_clam_amount = DEFAULT_AMOUNT
        
        # log info
        logger.info("Shell_amounts variables were defined successfully")