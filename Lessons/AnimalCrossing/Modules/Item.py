"""

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
                                    
                                    
                                        █ ▀█▀ █▀▀ █▀▄▀█ █▀
                                        █ ░█░ ██▄ █░▀░█ ▄█⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                Item's from within the game and item resources and their classes are on this script
                edit them, Add, Remove them here.

🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂
"""

# from import modules 
from dataclasses import dataclass, field


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