""" 𝘁𝗼𝗸𝗲𝗻𝘀 """
class Tokens: # tokens that randomize integers
    
    """ # Tokens
    
    ╭╮╱╱╱╱╱╱╱╭━╮╱╭╮╱╱╱╭╮
    ┃┃╱╱╱╱╱╱╱┃╭╯╭╯╰╮╱╱┃┃
    ┃┃╭━━┳━━┳╯╰╮╰╮╭╋━━┫┃╭┳━━┳━╮
    ┃┃┃┃━┫╭╮┣╮╭╯╱┃┃┃╭╮┃╰╯┫┃━┫╭╮╮
    ┃╰┫┃━┫╭╮┃┃┃╱╱┃╰┫╰╯┃╭╮┫┃━┫┃┃┃
    ╰━┻━━┻╯╰╯╰╯╱╱╰━┻━━┻╯╰┻━━┻╯╰╯
The leaf token is a random token that generates random integers from 0 to 5 and can be used to add randomizations
to speech or other elements within the game."""

    # define method
    def Leaf_Token(start_int: int, end_int: int):
        
        # import dependant modules
        import random
        
        # global
        global leaf_token
        # random integer variable
        leaf_token = int(random.randint(start_int, end_int))
        pass
    
    # generate rand int
    Leaf_Token(0, 2)