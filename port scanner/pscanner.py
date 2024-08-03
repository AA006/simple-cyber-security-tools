import socket

def port_scanner(target):
    ip = socket.gethostbyname(target)
    print(f"Tarama Yapılıyor\n"
          f"Hedef / IP\n"
          f"{target} / {ip}")
    for p in range(1, 65535):
        print(f"\nPort Scan {p}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        sonuc = s.connect_ex((ip, p))
        if sonuc == 0:
            print(f"{p}: Port {p} is open")
            open.append(p)
        else:
            print(f"{p}: Port {p} is closed")
        s.close()
    print(f"Port Scan Done\n"
          f"Open Ports --> {open}\n")

open = []
target = input("Hedef DOMAIN:")
port_scanner(target)
