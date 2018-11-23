import schedule, time
import requests

room_list = ['living', 'bed', 'seojin', 'seohun']
room_data = []
schedule_path = './schedule/'

base_ip = 'http://59.14.***.***'
control_url = base_ip + '/sm/control.php'
sess_id = {'PHPSESSID': '**************************'}

for i in range(4):
    tmp = []
    for j in range(3):
        tmp.append('') 
    room_data.append(tmp)

def ctrl_request():
    print ('function called')
    print (temp, io, i)
    room = room_list[i]
    p = '0' if io == 'o' else '1'
    
    room_no = {'living': 'L1', 'bed': 'R1', 'seojin': 'R2', 'seohun': 'R3'}
    room_no = room_no[room]
    if io == 'o':
        control_data = {'dn': '2', 'room': room_no, 'act': 'p0'}
        requests.get(control_url, cookies=sess_id, params=control_data)
    else:
        control_data = {'dn': '2', 'room': room_no, 'act': 'p1'}
        requests.get(control_url, cookies=sess_id, params=control_data)
        print (control_data)
        control_data = {'dn': '2', 'room': room_no, 'act': 's'+temp}
        requests.get(control_url, cookies=sess_id, params=control_data)
        print (control_data)

def schedule_parse():
    for i in range(4):
        f = open(schedule_path+room_list[i]+'.data')
        for j in range(3):
            room_data[i][j] = f.readline().replace('\n', '')
        f.close()
    print (room_data)

schedule_parse()
schedule.every().day.do(schedule_parse)

for i in range(4):
        io = room_data[i][0]
        temp = room_data[i][2]
        schedule.every().day.at(room_data[i][1]).do(ctrl_request)

while True:
    schedule.run_pending()
    time.sleep(1)