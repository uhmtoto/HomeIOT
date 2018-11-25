import requests as rq
base_ip = 'your_apt_ip'

# Get SessID
login_url = base_ip + '/house/member/login_check.php'
uid = raw_input('id? ')
upw = raw_input('pw? ')
login_d = {'user_id':uid, 'user_pass':upw}
res = rq.post(login_url, data=login_d)
res_cookie = res.headers['Set-Cookie'][10:][:26]
sess_id = {'PHPSESSID':res_cookie}

# Print Info
print ("Evolved KOCOM Homemanger")

# Control
con_url = base_ip + '/sm/control.php'
while (True):
    print ("Which device do you want to control?")
    cmd = int(input("1. Light\n2. Gas\n3. Boiler\n4. Ventilation\n5. Exit\n"))
    if (cmd < 1 or cmd > 5):
        print ("Please Input Again")
        continue
    if (cmd == 5):
        print ("Bye")
        break
    if (cmd == 1):
        print ("Which light do you want to control?")
        light_no = raw_input("1. Living Room 1\n2. Living Room 2\n3. Hallway\n")
        light_act = '0' if int(raw_input("1. On\n2. Off\n")) == 2 else '1'
        con_dat = {'dn':'0', 'room':'L1', 'act':light_no + light_act}
    if (cmd == 2):
        print("You can only turn it off")
        gas_act = int(raw_input("1. Turn it off\n2. Keep now status\n"))
        if (gas_act != 1):
            continue
        con_dat = {'dn':'1', 'room':'R1', 'act':'10'}
    if (cmd == 3):
        print ("Which boiler do you want to control?")
        boil_no = int(raw_input("1. Living Room\n2. Room 1\n3. Room 2\n4. Room 3\n"))
        boil_no = boil_no - 1 if boil_no > 1 else boil_no
        room_k = 'L' if boil_no == 1 else 'R'
        boil_cmd = int(raw_input("1. Power Control\n2. Temperature Control\n"))
        if (boil_cmd == 1):
            boil_act = 'p1' if  int(raw_input("1. On\n2. Off\n")) == 1 else 'p0';
            con_dat = {'dn':'2', 'room':room_k + str(boil_no), 'act':boil_act}
        else:
            boil_act = raw_input("What temperature do you want to set? (5 ~ 40)\n")
            boil_act = 's' + boil_act
            con_dat = {'dn':'2', 'room':room_k + str(boil_no), 'act':boil_act}
    if (cmd == 4):
        vent_act = int(raw_input("1. Power Control\n2. Wind Power Control\n"))
        if (vent_act == 1):
            vent_act = 'p' + ('1' if int(raw_input("1. On\n2. Off\n")) == 1 else '0')
        else:
            vent_act = raw_input("1. 33%\n2. 66%\n3. 100%\n")
            vent_act = 's' + vent_act
        con_dat = {'dn':'5', 'room':'L1', 'act':vent_act}
    res = rq.get(con_url, cookies=sess_id, params=con_dat)
    print ("Successfully Controled!!")
