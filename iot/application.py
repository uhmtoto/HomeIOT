from flask import Flask, render_template
from iot import app
import requests, os

device_list = ['light', 'gas', 'heating', 'ventilation']
room_list = ['living', 'living1', 'living2', 'hallway', 'kitchen', 'bed', 'seohun', 'seojin', 'all']

base_ip = 'http://59.14.175.46'
control_url = base_ip + '/sm/control.php'
sess_id = {'PHPSESSID': 'a82fe3pbuqgchva1ujv3m5b2q4'}
schedule_path = './schedule/'

@app.route('/')
def main():
    return render_template('main.html', main=True)

@app.route('/<dn>/<room>')
def status_parse(dn=None, room=None):
    return requests.get(base_ip + '/sm/room.php', cookies=sess_id, params={'dn': dn, 'room': room}).text

@app.route('/<device>/<room>/')
def dev_main(device=None, room=None):
    return render_template('main.html', device=device, device_list=device_list, room=room, room_list=room_list)

@app.route('/<device>/<room>/<act>')
def control(device=None, room=None, act=None):
    if (device == 'light'):
        if (act != 'on' and act != 'off'):
            return 'err'
        light_no = {'living1': '1', 'living2': '2', 'hallway': '3'}
        light_no = light_no[room]
        act = '1' if act == 'on' else '0'
        control_data = {'dn': '0', 'room': 'L1', 'act': light_no + act}
    if (device == 'gas'):
        if (act != 'off'):
            return 'err'
        control_data = {'dn': '1', 'room': 'R1', 'act': '10'}
    if (device == 'heating'):
        room_no = {'living': 'L1', 'bed': 'R1', 'seojin': 'R2', 'seohun': 'R3'}
        room_no = room_no[room]
        try:
            int(act)
            control_data = {'dn': '2', 'room': room_no, 'act': 's' + act}
        except:
            if (act != 'on' and act != 'off'):
                return 'err'
            control_data = {'dn': '2', 'room': room_no, 'act': 'p0' if act == 'off' else 'p1'}
    if (device == 'ventilation'):
        try:
            if (int(act) < 1 or int(act) > 3):
                return 'err'
            control_data = {'dn': '5', 'room': 'L1', 'act': 's'+act}
        except:
            if (act != 'on' and act != 'off'):
                return 'err'
            control_data = {'dn': '5', 'room': 'L1', 'act': 'p0' if act == 'off' else 'p1'}
    try:
        requests.get(control_url, cookies=sess_id, params=control_data)
        return 'ok'
    except:
        return 'err'

@app.route('/schedule/<room>/')
def schedule_form(room=None):
    return render_template('schedule.html', room=room, room_list=room_list)

@app.route('/schedule/<room>/<time>/<io>/<temp>')
def schedule_set(time=None, room=None, io=None, temp=None):
    i_time = int(time)
    i_temp = int(temp)
    if (i_time / 100 < 0 or i_time / 100 > 24 or i_time % 100 < 0 or i_time % 100 > 60):
        return 'check time'
    if (io != 'i' and io != 'o'):
        return 'check on/off'
    if (i_temp < 5 or i_temp > 40):
        return 'check temperature'
    time = time[:2] + ':' + time[2:]
    f = open(schedule_path+room+'.data', 'w')
    f.write(io+'\n'+time+'\n'+temp+'\n')
    f.close()
    return 'ok'

@app.route('/schedule/<room>/del')
def schdeule_del(room=None):
    f = open(schedule_path+room+'.data', 'w')
    f.close()
    return 'ok'
