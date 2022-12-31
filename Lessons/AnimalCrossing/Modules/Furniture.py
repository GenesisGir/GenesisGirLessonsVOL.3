"""

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂


                                    
                                    █▀▀ █░█ █▀█ █▄░█ █ ▀█▀ █░█ █▀█ █▀▀
                                    █▀░ █▄█ █▀▄ █░▀█ █ ░█░ █▄█ █▀▄ ██▄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                Furniture Classes, Functions and all the common furniture items can be found here

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
"""

# from import modules 
from dataclasses import dataclass, field

# classes
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