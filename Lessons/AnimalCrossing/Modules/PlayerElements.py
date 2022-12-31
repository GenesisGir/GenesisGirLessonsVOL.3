"""

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂


                    █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█   █▀▀ █░░ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀
                    █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄   ██▄ █▄▄ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ▄█
                    
                    Player username variable, Player levels, Experinece levels
                    
                    This script contains the classes, functions and data that is in charge of the level
                    system within the Animal Crossing: Pocket Camp.py

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
"""

# from import modules 
from dataclasses import dataclass, field
from Modules.Fashion import *

""" 𝗽𝗹𝗮𝘆𝗲𝗿 𝘁𝗿𝗮𝗶𝘁𝘀 """
class Player(): # player username
    
    # doc string
    """ tracks user username & equipped items and cosmetics! """
    
    # player username
    username = ""
    
    # equipped clothes globals
    
    # item names
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
    
    
    # item type globals
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
    
    
    # item theme globals
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
    
    
    # equipped clothes variables
    equipped_top = pajama_top.name # current top 
    equipped_bottom = pajama_pants.name # current bottoms 
    equipped_dress = None # current dress 
    equipped_handheld = None # current handheld 
    equipped_hat = None # current hat 
    equipped_face = None # current face 
    equipped_backpiece = None # current backpiece 
    equipped_shoes = None # current shoes 
    equipped_socks = pajama_slippers # current socks 
    equipped_outfit = starry_pajama_suit.name # current outfit 
    
    # equipped clothes type variables
    equipped_top_type = pajama_top.clothing_type # current top type
    equipped_bottom_type = pajama_pants.clothing_type # current bottoms type 
    equipped_dress_type = None # current dress type 
    equipped_handheld_type = None # current handheld type 
    equipped_hat_type = None # current hat type 
    equipped_face_type = None # current face type 
    equipped_backpiece_type = None # current backpiece type 
    equipped_shoes_type = None # current shoes type 
    equipped_socks_type = pajama_slippers.clothing_type # current sock theme 
    equipped_outfit_type = starry_pajama_suit.theme # current outfit type 
    
    # equipped clothes theme variables
    equipped_top_theme = pajama_top.theme # current top theme
    equipped_bottom_theme = pajama_pants.theme # current bottoms theme
    equipped_dress_theme = None # current dress theme
    equipped_handheld_theme = None # current handheld theme
    equipped_hat_theme = None # current hat theme
    equipped_face_theme = None # current face theme
    equipped_backpiece_theme = None # current backpiece theme
    equipped_shoes_theme = None # current shoes theme
    equipped_socks_theme = pajama_slippers.theme # current socks theme
    equipped_outfit_theme = starry_pajama_suit.theme # current outfit theme
    
    # log info
    logger.info("Player() class defined successfully")

class Player_level(): # player level
    
    # doc string
    """keeps track of levels available in the project"""
    
    # globals
    # player level globals
    global user_camp_level
    global user_next_camp_level
    global current_level
    global next_level
    global current_xp_level
    
    #friendship level globals
    global current_friendship_level
    global next_friendship_level
    global friendship_xp_level
    
    #  variables
    
    #friendship levels
    current_friendship_level = 0
    next_friendship_level = current_friendship_level + 1
    
    #friendship xp
    friendship_xp_level = 0
    
    
    
    # player level
    current_level = 0
    next_level = current_level + 1
    
    # player xp level 
    current_xp_level = 0
    
    # log info
    logger.info("Player_level() class defined successfully")

class Player_location(): # keeps track of where player is located on map
    
    # doc string
    """keeps track of where player is located on map!"""
    
    # player location globals
    global player_location
    
    # player location variables
    player_location = None
    pass



""" 𝗡𝗣𝗖𝗦 """
class entities: # NPC's

    # NPC Dataclass 📦
    @dataclass(frozen = True)
    class Npc(): # NPC class of special characters in Animal Crossing: Pocket Camp

        # NPC attributes 
        name: str = field(repr = True)

        located: str = field(repr = True) # location where NPC is found

        role: str = "NPC", field(repr = False) # role within the software
        
        pass
    
    # npc globals
    global isabelle
    global timmy
    global reese
    global lottie
    global lloid
    global katie
    global kk_slider
    global blathers
    global beppe
    global cj
    global cyrus
    global digby
    global kicks
    global labelle
    global niko
    global pascal
    global pave
    global pelly
    global pete
    global redd
    global sable
    global tom_nook
    global tortimer
    global wardell
    global wisp
    global zipper
    global jingle
    global jack
    global harvey
    global harriet
    global gulliver
    global flick
    global gracie
    global franklin
    global daisy_mae
    global chip
    global celeste
    global carlo
    global brewster
    global giovanni
    global kappn
    global katrina
    global leif
    global tommy
    global rover
    global lyle
    
    
    # instants of the Npc() class
    isabelle = Npc("Isabelle", "Market Place")
    timmy = Npc("Timmy", "Market Place")
    reese = Npc("Reese", "Market Place")
    lottie = Npc("Lottie", "Happy Homeroom")
    lloid = Npc("Lloid", "garden")
    katie = Npc("Katie", None)
    kk_slider = Npc("K.K Slider", None)
    blathers = Npc("Blathers", "Blathers's Treasure Trek")
    beppe = Npc("Beppe", "OK Motors")
    cj = Npc("CJ", None)
    cyrus = Npc("Cyrus", "Market Place ")
    digby = Npc("Digby", "Happy Homeroom")
    kicks = Npc("Kicks", "Market Place")
    labelle = Npc("Labelle", "Market Place")
    niko = Npc("Niko", "Happy Homeroom")
    pascal = Npc("Pascal", None)
    pave = Npc("Pave", None)
    pelly = Npc("Pelly", None)
    pete = Npc("Pete", "Pete's Parcel Service")
    redd = Npc("Redd", None)
    sable = Npc("Sable", "Market Place ")
    tom_nook = Npc("Tom Nook", None)
    tortimer = Npc("Torttimer", None)
    wardell = Npc("Wardell", "Happy Homeroom")
    wisp = Npc("Wisp", None)
    zipper = Npc("Zipper", None)
    jingle = Npc("Jingle", None)
    jack = Npc("Jack", None)
    harvey = Npc("Harvey", None)
    harriet = Npc("Harriet", None)
    gulliver = Npc("Gulliver", "Gulliver's Ship")
    flick = Npc("Flick", None)
    gracie = Npc("Gracie", None)
    franklin = Npc("Franklin", None)
    daisy_mae = Npc("Daisy Mae", None)
    chip = Npc("Chip", None)
    celeste = Npc("Celeste", None)
    carlo = Npc("Carlo", "OK Motors")
    brewster = Npc("Brewster", None)
    giovanni = Npc("Giovanni", "OK Motors")
    kappn = Npc("Kappn", None)
    katrina = Npc("Katrina", None)
    leif = Npc("Leif", None)
    tommy = Npc("Tommy", "Market Place ")
    rover = Npc("Rover", None)
    lyle = Npc("Lyle", None)

    # NPC name globals
    global ISABELLE
    global TIMMY
    global REESE
    global LOTTIE
    global LLOID
    global KATIE
    global KK_SLIDER
    global BLATHERS
    global BEPPE
    global CJ
    global CYRUS
    global DIGBY
    global KICKS
    global LABELLE
    global NIKO
    global PASCAL
    global PAVE
    global PELLY
    global PETE
    global REDD
    global SABLE
    global TOM_NOOK
    global TORTIMER
    global WARDELL
    global WISP
    global ZIPPER
    global JINGLE
    global JACK
    global HARVEY
    global HARRIET
    global GULLIVER
    global FLICK
    global GRACIE
    global FRANKLIN
    global DAISY_MAE
    global CHIP
    global CELESTE
    global CARLO
    global BREWSTER
    global GIOVANNI
    global KAPPN
    global KATRINA
    global LEIF
    global TOMMY
    global ROVER
    global LYLE
    
    
    # NPC name constants
    ISABELLE = isabelle.name
    TIMMY = timmy.name
    REESE = reese.name
    LOTTIE = lottie.name
    LLOID = lloid.name
    KATIE = katie.name
    KK_SLIDER = kk_slider.name
    BLATHERS = blathers.name
    BEPPE = beppe.name
    CJ = cj.name
    CYRUS = cyrus.name
    DIGBY = digby.name
    KICKS = kicks.name
    LABELLE = labelle.name
    NIKO = niko.name
    PASCAL = pascal.name
    PAVE = pave.name
    PELLY = pelly.name
    PETE = pete.name
    REDD = redd.name
    SABLE = sable.name
    TOM_NOOK = tom_nook.name
    TORTIMER = tortimer.name
    WARDELL = wardell.name
    WISP = wisp.name
    ZIPPER = zipper.name
    JINGLE = jingle.name
    JACK = jack.name
    HARVEY = harvey.name
    HARRIET = harriet.name
    GULLIVER = gulliver.name
    FLICK = flick.name
    GRACIE = gracie.name
    FRANKLIN = franklin.name
    DAISY_MAE = daisy_mae.name
    CHIP = chip.name
    CELESTE = celeste.name
    CARLO = carlo.name
    BREWSTER = brewster.name
    GIOVANNI = giovanni.name
    KAPPN = kappn.name
    KATRINA = katrina.name
    LEIF = leif.name
    TOMMY = tommy.name
    ROVER = rover.name
    LYLE = lyle.name

class Furniture_cls: # furniture assets 📦
    
    class Type: # catagory types
        
        # globals
        global TABLE
        global BED
        global SEAT
        global STORAGE
        global LAMP
        global KITCHENWARE
        global GYM_EQUIPMENT
        global ELECTRONICS
        global STORE_DECOR
        global PROMINENT_FURNITURE
        global FOOD_DECORATION
        global TOY
        global ART
        global INSTRUMENT
        global PLANT
        global GYROID
        global OUTDOOR_FURNITURE
        global WALLPAPER
        
        # catagory types
        TABLE = "Table"
        BED = "Bed"
        SEAT = "Chair"
        STORAGE = "Storage"
        LAMP = "Lamp"
        KITCHENWARE = "Kitchenware/Appliance"
        GYM_EQUIPMENT = "Gym Equipment"
        ELECTRONICS = "Electronics"
        STORE_DECOR = "Store Decoration"
        PROMINENT_FURNITURE = "Prominent Furniture"
        FOOD_DECORATION = "Food Decoration"
        TOY = "Toy"
        ART = "Art"
        INSTRUMENT = "Instruments"
        PLANT = "Plant"
        GYROID = "Gyroid"
        OUTDOOR_FURNITURE = "Outdoor Furniture"
        WALLPAPER = "Wallpaper"
    
    class theme(): # themes for items
        
        # globals
        global CUTE
        global HIP
        global COOL
        global ELEGANT
        global SPORTY
        global HARMONIOUS
        global DRAIN
        global NATURAL
        global MODERN
        global RUSTIC
        global HISTORIC
        global CIVIC
        global HISTORICAL
        
        # funiture catagory themes
        CUTE = "Cute"
        HIP = "Hip"
        COOL = "Cool"
        ELEGANT = "Elegant"
        SPORTY = "Sporty"
        HARMONIOUS = "Harmonious"
        DRAIN = "Draingang"
        NATURAL = "Natural"
        MODERN = "Modern"
        RUSTIC = "Rustic"
        HISTORIC = "Historic"
        CIVIC = "Civic"
        HISTORICAL = "Historical"
    
    @dataclass(frozen = True)
    class Furniture:
        
        # attributes
        name: str
        furniture_type: str
        theme: str
        bells: int
        pass
    
    # globals
    global aquarium_table
    global autumn_apple_bistro_set
    global barrel_table
    global basic_teachers_desk
    global bbq_camp_table
    global birthday_table
    global blue_egg_painting_table
    global cafeteria_table
    global coconut_table
    global classic_buffet_table
    global alpine_bed
    global balloon_bed
    global bookish_loft_bed
    global cardboard_bed
    global crystal_bed
    global cozy_camp_hammock
    global classic_bed
    global chrysanthemum_bed
    global choco_mint_bed
    global grandiose_canopy_bed
    global alpine_sofa
    global azalea_stool
    global balloon_chair
    global blue_bbq_camp_chair
    global basket_chair
    global classic_chair
    global cozy_lodge_knit_sofa
    global cupid_bench
    global deep_sea_mermaid_sofa
    global denim_sofa
    global cd_shelf
    global double_bookshelf
    global full_moon_vanity
    global gardening_tool_shelf
    global hello_kitty_drawers
    global kiddie_bookcase
    global ice_cream_truck_shelf
    global ice_shelf
    global ice_dresser
    global mermaid_dresser
    global angelic_chandelier
    global aquatic_lamp
    global balloon_lamp
    global balloon_dog_lamp
    global bbq_camp_lantern
    global blooming_chapel_lantern
    global bright_glowing_gifts
    global candlelit_house_set
    global clear_cafe_bubble_light
    global crystal_lamp
    global computer
    global decade_diner_jukebox
    global dice_stereo
    global desktop_tv
    global laptop
    global juicy_apple_tv
    global humidifier
    global hologram_machine
    global high_end_stereo
    global haunted_tv
    global server
    global automatic_washer
    global bathroom_sink
    global bathtub
    global bread_making_set
    global breezy_clothes_line
    global donut_shop_kitchen
    global dishwasher
    global gold_toilet
    global freezer
    global far_out_refrigerator
    global barbell
    global blue_floral_inner_tube
    global golf_bag
    global exercise_bike
    global exercise_ball_blue	
    global earth_tone_yoga_mats
    global hurdle
    global skateboard_rack
    global sandbag
    global pink_whale_pool_float
    global baked_goods_display
    global bakery_counter
    global basic_display_stand
    global bathroom_stall
    global beauty_salon_cart
    global big_top_treats_wagon
    global billiard_table
    global bistro_table
    global blue_ice_cream_cart
    global capsule_toy_machine
    global aluminum_briefcase
    global anchor
    global angelfish_tank
    global angelic_fireplace
    global aroma_pot
    global aries_scepter
    global aquarium_pillar
    global antique_library_books
    global bakery_sign
    global bakery_seating
    global afternoon_tea_set
    global apple_spooky_treat_set
    global bananas
    global basket_of_tangerines
    global bbq_veggie_skewers
    global bbq_camp_meals
    global berry_cake_set
    global cinnamoroll_tray
    global chocolate_waffles_meal
    global confectionery_case	
    global blooper_balloon
    global dreamy_unicorn_plushie
    global dollhouse
    global cute_as_a_button_bear
    global crayons
    global first_anniv_music_box
    global executive_toy
    global giant_zipper_plushie
    global giant_stuffed_eevee
    global giant_game_boy
    global ethereal_pegasus_statue
    global aquarius_urn
    global gallant_statue
    global statue_fountain	
    global ancient_statue
    global amp
    global angelic_harp
    global dj_turntable
    global drum_set
    global effects_rack
    global electropop_synth
    global electropop_standing_mic
    global electropop_speaker_set
    global electropop_guitar
    global lil_devil_bass_stage
    global aloe
    global bamboo_tree	
    global barrel_planter
    global azalea_bonsai
    global birch_tree
    global blossoming_sakura_tree
    global cacao_tree
    global cactus
    global cherry_blossom_tree	
    global garden_flower_wagon
    global denim_gyroidite_figure
    global kingly_gyroidite_statue
    global jellied_gyroidite_figure
    global gyroidite_statue
    global darling_gyroidite_figure
    global air_pump
    global autumn_cookie_tin
    global autumn_fairy_jar
    global balance_training_pond
    global backpack
    global bbq_camp_tent
    global big_lit_up_sleigh
    global big_leaf_umbrella
    global blue_sparklers
    global broken_deep_sea_pillar
    global alpine_wall
    global antique_bookshelf_wall
    global backyard_fence
    global balloon_wall
    global ballroom_wall
    global boba_shop_floral_wall
    global blue_sky_wall
    global blue_seashell_wall
    global celestial_wall
    global cityscape_wall
    global cottage_wood_paneling
    
    # furniture object instances
    
    # tables
    aquarium_table = Furniture("Aquarium Table", TABLE , MODERN, 100)
    autumn_apple_bistro_set = Furniture("Autumn Apple Bistro Set", TABLE, RUSTIC, 120)
    barrel_table = Furniture("Barrel Table", TABLE, HISTORIC, 90)
    basic_teachers_desk = Furniture("Basic Teacher's Desk", TABLE, CIVIC, 100)
    bbq_camp_table = Furniture("BBQ-Camp Table", TABLE, NATURAL, 100)
    birthday_table = Furniture("Birthday Table", TABLE, ELEGANT, 600)
    blue_egg_painting_table = Furniture("Blue Egg-Painting Table", TABLE, CUTE, 100)
    cafeteria_table = Furniture("Cafeteria Table", TABLE, NATURAL, 150)
    coconut_table = Furniture("Coconut Table", TABLE, HARMONIOUS, 260)
    classic_buffet_table = Furniture("Classic Buffet", TABLE, NATURAL, 300)

    # beds
    alpine_bed = Furniture("Alpine Bed", BED , NATURAL , 100)
    balloon_bed = Furniture("Balloon Bed", BED , HIP , 500)
    bookish_loft_bed = Furniture("Bookish Loft Bed", BED , MODERN , 400)
    cardboard_bed = Furniture("Cardboard Bed", BED , NATURAL , 50)
    crystal_bed = Furniture("Crystal Bed", BED , CUTE , 500)
    cozy_camp_hammock = Furniture("Cozy Camp Hammock", BED , NATURAL, 2640)
    classic_bed = Furniture("Classic Bed", BED , NATURAL, 2300)
    chrysanthemum_bed = Furniture("Chrysanthemum Bed", BED , MODERN, 0)
    choco_mint_bed = Furniture("Choco-Mint Bed", BED , CUTE, 1200)
    grandiose_canopy_bed = Furniture("Grandiose Canopy Bed", BED , ELEGANT, 0)
    
    # seats
    alpine_sofa = Furniture("Alpine Sofa", SEAT , NATURAL, 1470)
    azalea_stool = Furniture("Azalea Stool", SEAT, CUTE, 560)
    balloon_chair = Furniture("Balloon Chair", SEAT , HIP, 810)
    blue_bbq_camp_chair = Furniture("Blue BBQ-Camp Chair", SEAT, NATURAL, 200)
    basket_chair = Furniture("Basket Chair", SEAT, MODERN, 540)
    classic_chair = Furniture("Classic Chair", SEAT, NATURAL, 1160)
    cozy_lodge_knit_sofa = Furniture("Cozy-Lodge Knit Sofa", SEAT, RUSTIC, 1000)
    cupid_bench = Furniture("Cupid Bench", SEAT, CUTE, 10440)
    deep_sea_mermaid_sofa = Furniture("Deep-Sea Mermaid Sofa", SEAT, CUTE, 500)
    denim_sofa = Furniture("Denim Sofa", SEAT, COOL, 1500)
    
    # storage
    cd_shelf = Furniture("CD Shelf", STORAGE , COOL, 2410)
    double_bookshelf = Furniture("Double Bookshelf", STORAGE , NATURAL, 4320)
    full_moon_vanity = Furniture("Full-Moon Vanity", STORAGE , CUTE, 10240)
    gardening_tool_shelf = Furniture("Gardening Tool Shelf", STORAGE , NATURAL, 10000)
    hello_kitty_drawers = Furniture("Hello Kitty Drawers", STORAGE , CUTE, 600)
    kiddie_bookcase = Furniture("Kiddie Bookcase", STORAGE , HIP, 1120)
    ice_cream_truck_shelf = Furniture("Ice-Cream-Truck Shelf", STORAGE , CUTE, 1000)
    ice_shelf = Furniture("Ice Shelf", STORAGE , CUTE, 0)
    ice_dresser = Furniture("Ice Dresser", STORAGE , CUTE, 0)
    mermaid_dresser = Furniture("Mermaid Dresser", STORAGE , CUTE, 9720)
    
    # lamps
    angelic_chandelier = Furniture("Angelic Chandelier", LAMP , ELEGANT , 1700)
    aquatic_lamp = Furniture("Aquatic Lamp", LAMP , MODERN, 1780)
    balloon_lamp = Furniture("Balloon Lamp", LAMP , HIP, 950)
    balloon_dog_lamp = Furniture("Balloon-Dog Lamp", LAMP , HIP, 760)
    bbq_camp_lantern = Furniture("BBQ-Camp Lantern", LAMP , NATURAL, 660)
    blooming_chapel_lantern = Furniture("Blooming Chapel Lantern", LAMP , NATURAL, 600)
    bright_glowing_gifts = Furniture("Bright Glowing Gifts", LAMP , HIP, 1200)
    candlelit_house_set = Furniture("Candlelit House Set", LAMP , NATURAL, 200)
    clear_cafe_bubble_light = Furniture("Clear-Café Bubble Light", LAMP , MODERN, 1200)
    crystal_lamp = Furniture("Crystal Lamp", LAMP , CUTE, 300)
    
    # electronics
    computer = Furniture("Computer", ELECTRONICS, COOL, 10340)
    decade_diner_jukebox = Furniture("Decade-Diner Jukebox", ELECTRONICS, COOL, None)
    dice_stereo	= Furniture("Dice Stereo", ELECTRONICS, HIP, 9540)
    desktop_tv = Furniture("Desktop TV", ELECTRONICS, MODERN, 2250)
    laptop = Furniture("Laptop", ELECTRONICS, COOL, 10340)
    juicy_apple_tv = Furniture("Juicy-Apple TV", ELECTRONICS, COOL, 10250)
    humidifier = Furniture("Humidifier", ELECTRONICS, MODERN, 9670)
    hologram_machine = Furniture("Hologram Machine", ELECTRONICS, COOL, 10350)
    high_end_stereo = Furniture("High-End Stereo", ELECTRONICS, COOL, 9850)
    haunted_tv = Furniture("Haunted TV", ELECTRONICS, HARMONIOUS, 960)
    server = Furniture("Server", ELECTRONICS, CIVIC, 9670)
    
    # kitchenware/appliances
    automatic_washer = Furniture("Automatic Washer", KITCHENWARE , MODERN, 10470)
    bathroom_sink = Furniture("Bathroom Sink", KITCHENWARE , MODERN, 10020)
    bathtub = Furniture("Bathtub", KITCHENWARE , HARMONIOUS, 200)
    bread_making_set = Furniture("Bread-Making Set", KITCHENWARE , NATURAL, 9720)
    breezy_clothes_line = Furniture("Breezy Clothes line", KITCHENWARE , NATURAL, 2160)
    donut_shop_kitchen = Furniture("Donut-Shop Kitchen", KITCHENWARE , CUTE, None)
    dishwasher = Furniture("Dishwasher", KITCHENWARE , NATURAL, 9580)
    gold_toilet = Furniture("Gold Toilet", KITCHENWARE , ELEGANT, 200)
    freezer = Furniture("Freezer", KITCHENWARE , MODERN, 580)
    far_out_refrigerator = Furniture("Far-Out Refrigerator", KITCHENWARE , HIP, 1920)
    
    # gym and sports equipment
    barbell = Furniture("Barbell", GYM_EQUIPMENT , SPORTY, 890)
    blue_floral_inner_tube = Furniture("Blue Floral Inner Tube", GYM_EQUIPMENT , SPORTY, 200)
    golf_bag = Furniture("Golf Bag", GYM_EQUIPMENT , SPORTY, 10230)
    exercise_bike = Furniture("Exercise Bike", GYM_EQUIPMENT , SPORTY, 1610)
    exercise_ball_blue	 = Furniture("Exercise Ball (Blue)", GYM_EQUIPMENT , SPORTY, 10230)
    earth_tone_yoga_mats = Furniture("Earth-Tone Yoga Mats", GYM_EQUIPMENT , SPORTY, 3600)
    hurdle = Furniture("Hurdle", GYM_EQUIPMENT , SPORTY, 730)
    skateboard_rack = Furniture("Skateboard Rack", GYM_EQUIPMENT , SPORTY, 9810)
    sandbag = Furniture("Sandbag", GYM_EQUIPMENT , SPORTY, 9979)
    pink_whale_pool_float = Furniture("Pink Whale Pool Float", GYM_EQUIPMENT , SPORTY, None)
    
    # Store Decor
    baked_goods_display	= Furniture("Baked-Goods Display", STORE_DECOR , RUSTIC, None)
    bakery_counter = Furniture("Bakery Counter", STORE_DECOR , RUSTIC, None)
    basic_display_stand = Furniture("Basic Display Stand", STORE_DECOR , CIVIC, 1600)
    bathroom_stall = Furniture("Bathroom Stall", STORE_DECOR , CIVIC, None)
    beauty_salon_cart = Furniture("Beauty Salon Cart", STORE_DECOR , CIVIC, 9870)
    big_top_treats_wagon = Furniture("Big-Top Treats Wagon", STORE_DECOR , HIP, None)
    billiard_table = Furniture("Billiard Table", STORE_DECOR , COOL, 10480)
    bistro_table = Furniture("Bistro Table", STORE_DECOR , NATURAL, 710)
    blue_ice_cream_cart = Furniture("Blue Ice-Cream Cart", STORE_DECOR , CUTE, 3360)
    capsule_toy_machine = Furniture("Capsule-Toy Machine", STORE_DECOR , COOL, 1870)

    # Prominent Furniture
    aluminum_briefcase = Furniture("Aluminum Briefcase", PROMINENT_FURNITURE, CIVIC, 9940)
    anchor = Furniture("Anchor", PROMINENT_FURNITURE, HISTORICAL, 1840)
    angelfish_tank = Furniture("Angelfish Tank", PROMINENT_FURNITURE, SPORTY, None)
    angelic_fireplace = Furniture("Angelic Fireplace", PROMINENT_FURNITURE, ELEGANT, None)
    aroma_pot = Furniture("Aroma Pot", PROMINENT_FURNITURE, CUTE, 10060)
    aries_scepter = Furniture("Aries Scepter", PROMINENT_FURNITURE, ELEGANT, None)
    aquarium_pillar	= Furniture("Aquarium Pillar", PROMINENT_FURNITURE, MODERN, None)
    antique_library_books = Furniture("Antique Library Books", PROMINENT_FURNITURE, HISTORICAL, None)
    bakery_sign = Furniture("Bakery Sign", PROMINENT_FURNITURE, RUSTIC, None)
    bakery_seating = Furniture("Bakery Seating", PROMINENT_FURNITURE, CIVIC, None)
    
    # Food Decor
    afternoon_tea_set = Furniture("Afternoon-Tea Set", PROMINENT_FURNITURE, ELEGANT, 10130)	
    apple_spooky_treat_set = Furniture("Apple Spooky-Treat Set", PROMINENT_FURNITURE, HIP, 1440)	
    bananas = Furniture("Bananas", PROMINENT_FURNITURE, NATURAL, 10220)	
    basket_of_tangerines = Furniture("Basket of Tangerines", PROMINENT_FURNITURE, NATURAL, 100)	
    bbq_veggie_skewers = Furniture("BBQ Veggie Skewers", PROMINENT_FURNITURE, SPORTY, None)	
    bbq_camp_meals = Furniture("BBQ-Camp Meals", PROMINENT_FURNITURE, SPORTY, None)	
    berry_cake_set = Furniture("Berry Cake Set", PROMINENT_FURNITURE, MODERN, None)	
    cinnamoroll_tray = Furniture("Cinnamoroll Tray", PROMINENT_FURNITURE, CUTE, None)	
    chocolate_waffles_meal = Furniture("Chocolate Waffles Meal", PROMINENT_FURNITURE, NATURAL, None)	
    confectionery_case	 = Furniture("Confectionery Case", PROMINENT_FURNITURE, HIP, None)	
    
    # toys
    blooper_balloon = Furniture("Blooper Balloon", TOY, HIP, None)
    dreamy_unicorn_plushie = Furniture("Dreamy Unicorn Plushie", TOY, CUTE, None)
    dollhouse = Furniture("Dollhouse", TOY, CUTE, 9510)
    cute_as_a_button_bear = Furniture("Cute-as-a-Button Bear", TOY, NATURAL, 6000)
    crayons = Furniture("Crayons", TOY, CUTE, 1280)
    first_anniv_music_box = Furniture("First-Anniv. Music Box", TOY, ELEGANT, None)
    executive_toy = Furniture("Executive Toy", TOY, HIP, None)
    giant_zipper_plushie = Furniture("Giant Zipper Plushie", TOY, HIP, 14400)
    giant_stuffed_eevee = Furniture("Giant Stuffed Eevee", TOY, CUTE, 2400)
    giant_game_boy = Furniture("Giant Game Boy", TOY, COOL, 10370)
    
    # art
    ethereal_pegasus_statue	= Furniture("Ethereal Pegasus Statue", ART, ELEGANT, None)
    aquarius_urn = Furniture("Aquarius Urn", ART, ELEGANT, 1670)
    gallant_statue = Furniture("Gallant Statue", ART, HISTORICAL, 9610)
    statue_fountain	 = Furniture("Statue Fountain", ART, ELEGANT, 9770)
    ancient_statue = Furniture("Ancient Statue", ART, HARMONIOUS, 9500)
    
    # Instruments and Music Equipment
    amp = Furniture("Amp", INSTRUMENT, COOL, 290)
    angelic_harp = Furniture("Angelic Harp", INSTRUMENT, ELEGANT, None)
    dj_turntable = Furniture("DJ's Turntable", INSTRUMENT, COOL, 10030)
    drum_set = Furniture("Drum Set", INSTRUMENT, COOL, 730)
    effects_rack = Furniture("Effects Rack", INSTRUMENT, COOL, 520)
    electropop_synth = Furniture("Electropop Synth", INSTRUMENT, COOL, 2160)
    electropop_standing_mic = Furniture("Electropop Standing Mic", INSTRUMENT, COOL, 1440)
    electropop_speaker_set = Furniture("Electropop Speaker Set", INSTRUMENT, COOL, 6000)
    electropop_guitar = Furniture("Electropop Guitar", INSTRUMENT, COOL, 960)
    lil_devil_bass_stage = Furniture("Li'l-Devil Bass Stage", INSTRUMENT, COOL, None)
    
    # Plants
    aloe = Furniture("Aloe", PLANT, NATURAL, 430)
    bamboo_tree	 = Furniture("Bamboo Tree", PLANT,  HARMONIOUS, 750)
    barrel_planter = Furniture("Barrel_Planter", PLANT,  NATURAL, 1800)
    azalea_bonsai = Furniture("Azalea Bonsai", PLANT,  HARMONIOUS, 9800)
    birch_tree = Furniture("Birch Tree", PLANT,  MODERN, None)
    blossoming_sakura_tree = Furniture("Blossoming Sakura Tree", PLANT,  HARMONIOUS, None)
    cacao_tree = Furniture("Cacao Tree", PLANT,  NATURAL, 1410)
    cactus = Furniture("Cactus", PLANT,  NATURAL, 330)
    cherry_blossom_tree	 = Furniture("Cherry-Blossom Tree", PLANT,  HARMONIOUS, None)
    garden_flower_wagon = Furniture("Garden Flower Wagon", PLANT,  NATURAL, None)
    
    # Gyroids
    denim_gyroidite_figure = Furniture("Denim-Gyroidite Figure", GYROID, COOL, 828)
    kingly_gyroidite_statue = Furniture("Kingly-Gyroidite Statue", GYROID, ELEGANT, 8280)
    jellied_gyroidite_figure = Furniture("Jellied-Gyroidite Figure", GYROID, HIP, 828)
    gyroidite_statue = Furniture("Gyroidite Statue", GYROID, NATURAL, None)
    darling_gyroidite_figure = Furniture("Darling-Gyroidite Figure", GYROID, ELEGANT, 828)
    
    # Outdoor Furniture
    air_pump = Furniture("Air Pump", OUTDOOR_FURNITURE, SPORTY, None)
    autumn_cookie_tin = Furniture("Autumn Cookie Tin", OUTDOOR_FURNITURE, NATURAL, None)
    autumn_fairy_jar = Furniture("Autumn Fairy Jar", OUTDOOR_FURNITURE, NATURAL, None)
    balance_training_pond = Furniture("Balance-Training Pond", OUTDOOR_FURNITURE, HARMONIOUS, None)
    backpack = Furniture("Backpack", OUTDOOR_FURNITURE, SPORTY, 970)
    bbq_camp_tent = Furniture("BBQ-Camp Tent", OUTDOOR_FURNITURE, RUSTIC, None)
    big_lit_up_sleigh = Furniture("Big Lit-Up Sleigh", OUTDOOR_FURNITURE, RUSTIC, None)
    big_leaf_umbrella = Furniture("Big Leaf Umbrella", OUTDOOR_FURNITURE, NATURAL, None)
    blue_sparklers = Furniture("Blue Sparklers", OUTDOOR_FURNITURE, HARMONIOUS, None)
    broken_deep_sea_pillar = Furniture("Broken Deep-Sea Pillar", OUTDOOR_FURNITURE, HISTORICAL, None)
    
    # Wallpaper
    alpine_wall = Furniture("Alpine Wall", WALLPAPER, NATURAL, None)
    antique_bookshelf_wall = Furniture("Antique Bookshelf Wall", WALLPAPER, HISTORICAL, None)
    backyard_fence = Furniture("Backyard Fence", WALLPAPER, NATURAL, None)
    balloon_wall = Furniture("Balloon Wall	", WALLPAPER, HIP, 2230)
    ballroom_wall = Furniture("Ballroom Wall", WALLPAPER, ELEGANT, None)
    boba_shop_floral_wall = Furniture("Boba-Shop Floral Wall", WALLPAPER, HARMONIOUS, None)
    blue_sky_wall = Furniture("Blue-Sky Wall", WALLPAPER, NATURAL, None)
    blue_seashell_wall = Furniture("Blue Seashell Wall", WALLPAPER, NATURAL, None)
    celestial_wall	= Furniture("Celestial Wall	", WALLPAPER, ELEGANT, None)
    cityscape_wall = Furniture("Cityscape Wall", WALLPAPER, MODERN, None)
    cottage_wood_paneling = Furniture("Cottage Wood Paneling", WALLPAPER, NATURAL, None)

class Items: # item assets 📦
    
    @dataclass(order=True,frozen=True)
    class Item:
        
        # attributes
        name: str = field(repr = True)
        bug: bool = field(repr = False)
        fish: bool = field(repr = False)
        fruit: bool = field(repr = False)
        shell: bool = field(repr = False)
        bell_price: int = field(repr = True)
        
        pass
    
    # item globals
    global tiger_butterfly
    global giant_cicada
    global darner_dragonfly
    global horned_dynastid
    global white_tailed_skimmer
    global saw_stag
    global emperor_butterfly
    global banded_dragonfly
    global horned_atlas
    global golden_stag
    global crucian_carp
    global pale_chub
    global bluegill
    global black_bass
    global eel
    global frog
    global pop_eyed_goldfish
    global sweetfish
    global gar
    global koi
    global cherry
    global pear
    global peach
    global orange
    global coconut
    global apple
    global lemon
    global lychee
    global grapes
    global perfect_apple
    global coral
    global sea_star
    global scallop_shell
    global pearl_oyster_shell
    global grand_oyster
    global angel_wing_clam
    global pink_heart_cockle
    global conch_shell
    global violet_sea_snail
    global razor_clam
    
    
    # Item objects
    # bug instants
    tiger_butterfly = Item("Tiger Butterfly", True, False, False, False ,10)
    giant_cicada = Item("Giant Cicada", True, False, False, False, 10)
    darner_dragonfly = Item("Darner Dragonfly", True, False, False, False, 10)
    horned_dynastid = Item("Horned Dynastid", True, False, False, False, 100)
    white_tailed_skimmer = Item("White-Tailed Skimmer", True, False, False, False, 300)
    saw_stag = Item("Saw Stag", True, False, False, False, 1200)
    emperor_butterfly = Item("Emperor Butterfly", True, False, False, False, 3000)
    banded_dragonfly = Item("Banded Dragonfly", True, False, False, False, 3000)
    horned_atlas = Item("Horned Atlas", True, False, False, False, 4000)
    golden_stag = Item("Golden Stag", True, False, False, False, 5500)
    
    # fish instants
    crucian_carp = Item("Crucian Carp", False, True, False, False, 10)
    pale_chub = Item("Pale Chub", False, True, False, False, 10)
    bluegill = Item("Bluegill", False, True, False, False, 10)
    black_bass = Item("Black Bass", False, True, False, False, 100)
    eel = Item("Eel", False, True, False, False, 1200)
    frog = Item("Frog", False, True, False, False, 200)
    pop_eyed_goldfish = Item("Pop-Eyed Goldfish", False, True, False, False, 200)
    sweetfish = Item("Sweetfish", False, True, False, False, 800)
    gar = Item("gar", False, True, False, False, 2000)
    koi = Item("koi", False, True, False, False, 4000)
    
    # fruit instants
    cherry = Item("Cherry", False, False, True, False, 10)
    pear = Item("Pear", False, False, True, False, 10)
    peach = Item("Peach", False, False, True, False, 10)
    orange = Item("Orange", False, False, True, False, 10)
    coconut = Item("Coconut", False, False, True, False, 10)
    apple = Item("Apple", False, False, True, False, 10)
    lemon = Item("Lemon", False, False, True, False, 10)
    lychee = Item("Lychee", False, False, True, False, 600)
    grapes = Item("Grapes", False, False, True, False, 600)
    perfect_apple = Item("Perfect Apple", False, False, True, False, 600)
    
    # shell instants
    coral = Item("Coral", False, False, False, True, 10)
    sea_star = Item("Sea Star", False, False, False, True, 10)
    scallop_shell = Item("Scallop Shell", False, False, False, True, 10)
    pearl_oyster_shell = Item("Pearl-Oyster Shell", False, False, False, True, 2000)
    grand_oyster = Item("Grand Oyster", False, False, False, True, 1000)
    angel_wing_clam = Item("Angel Wing Clam", False, False, False, True, 1200)
    pink_heart_cockle = Item("Pink Heart Cockle", False, False, False, True, 10)
    conch_shell = Item("Conch Shell", False, False, False, True, 10)
    violet_sea_snail = Item("Violet Sea Snail", False, False, False, True, 10)
    razor_clam = Item("Razor Clam", False, False, False, True, 10)