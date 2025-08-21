import random
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
import
    return password
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
def gen_emodji():
    emodji = ["🥷", "🐉", "👻", "🎃"]
    return random.choice(emodji)
