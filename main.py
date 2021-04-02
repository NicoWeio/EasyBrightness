#!/usr/bin/env python3

import re, sys, subprocess, time

SCREENS = ['dev:/dev/i2c-3', 'dev:/dev/i2c-4', 'dev:/dev/i2c-5']
# links, Mitte, rechts

commands = {int(x.split(':')[0]) : int(x.split(':')[1]) for x in sys.argv[1].split(',')}

print(commands)

def check_success(out):

    # Writing 0x10, 0x19(25)...
    # Control 0x10: +/25/100 C [Brightness]
    
    written = re.search('Writing (.*)...', out).group(1)
    print(f"{written=}")
    written_num = int(re.search(r'\((.*)\)', written).group(1))
    print(f"{written_num=}")
    read = re.search('Control (.*)$', out).group(1)
    print(f"{read=}")
    read_num = int(re.search(r'\+\/(.*)\/100', read).group(1))
    print(f"{read_num=}")
    return written_num == read_num

for screen_id, brightness in commands.items():
    assert brightness >= 0 and brightness <= 100
    addr = SCREENS[int(screen_id)-1]

    cmd = ['ddccontrol', '-r', '0x10', '-w', f'{brightness}', f'{addr}']
    print('$ ' + ' '.join(cmd))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = p.communicate()
    # print(out.decode())
    success = check_success(out.decode())
    if not success:
        print('FAILED')
        time.sleep(1)
    print('---')
