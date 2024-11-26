import random
import os
class ceritaku:
    def __init__(self):
        orang = ["aku","konsen","andi","budi","cobra"]
        randomorang = random.choice(orang)
        oranglain = ["rudi", "yanto", "lisa"]
        randomoranglain = random.choice(oranglain)
        oranglainlagi = ["budi", "aris", "santo"]
        randomoranglainlagi = random.choice(oranglainlagi)
        tujuanawal = ["mrt", "lrt", "bus"]
        randomtujuanawal = random.choice(tujuanawal)
        tujuanakhir = ["kfc", "mcd", "burger king"]
        randomtujuanakhir = random.choice(tujuanakhir)
        game = ["ml", "hok", "dota"]
        randomgame = random.choice(game)
        status = ["menang", "kalah"]
        randomstatus = random.choice(status)
        seluruhorang = ["aku","konsen","andi","budi","cobra", "rudi", "yanto", "lisa", "budi", "aris", "santo"]
        randomseluruhorang = random.choice(seluruhorang)
        os.system("cls")
        print(f"{randomorang} pergi ke {randomtujuanawal} untuk berjumpa dengan {randomoranglain} mereka berdua selanjutnbya pergi bersama ke {randomtujuanawal} untuk pergi menemui teman mereka yang lain bernama {randomoranglainlagi} setelah itu mereka pergi ke {randomtujuanakhir} untuk makan bersama dan sambil bermain {randomgame} dengan hasil {randomstatus} dan player terbaik adalah {randomseluruhorang}.")
def main():
    run = ceritaku()
if __name__ == "__main__":
    main()