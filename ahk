#!/usr/bin/env python

import os
import sys
import re
import subprocess
ahk_path = os.environ.get("AHK_HOME")
ahk_file = 'Hotkeys.ahk'

def push(params):
#push
    if len(params)!= 4:
        print 'Wrong number of arguments for push'
        return -1
    else:
        print 'pushing'
        subprocess.Popen('echo -e ":C*:' + params[2] + '::' + params[3]
                + '" >> ' + ahk_path + '/' + ahk_file, shell = True)
        return 0

def pop(params):
#pop the last map
    print 'poping'
    if len(params) == 2:
        subprocess.Popen('sed -i \'$d\' ' +  ahk_path + '/' + ahk_file, shell = True)
        return 0
    
    file = open(ahk_path + '/' + ahk_file, 'r')
    lines = file.readlines()
    
    if len(params) == 3:
        if not params[2].isdigit():
            print 'Usage of pop: ahk pop [int] [int]'
            return -1
        else:
            subprocess.Popen('sed -i \'' + str(len(lines) - int(params[2])) + 'd\' ' + ahk_path + '/' + ahk_file, shell = True)
            return 0
    elif len(params) == 4:
        if not params[2].isdigit() or not params[3].isdigit():
            print 'Usage of pop: ahk pop [int] [int]'
            return -1
        else:
            subprocess.Popen('sed -i \'' + str(len(lines) - int(params[3])) + ', ' 
                    + str(len(lines) - int(params[2])) + 'd\' ' +  ahk_path + '/' + ahk_file, shell = True)
            return 0

def list():
#list all map in the stack
    file = open(ahk_path + '/' + ahk_file, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        pattern = re.search(';;;;;;stack;;;;;;.*', lines[i])
        if pattern != None:
            count = 0
            for j in range(len(lines) - 1, i, -1):
                list = re.findall(':[a-z]+', lines[j])
                if len(list) != 0:
                    print '[' + str(count) + '] ' + list[0][1 : ] + '\t-->\t' + list[1][1 : ]
                    count = count + 1
            break

def restart_ahk():
    subprocess.Popen('pkill AutoHotkey', shell = True)
    print 'Restarting AutoHotkey'
    subprocess.Popen('AutoHotkey /r ' + ahk_path + '/' + ahk_file + '&', shell = True)
    
if __name__ == '__main__':
    if len(ahk_path) == 0:
        print "Please set Environment AHK_HOME first"
        os._exit(0)
    
    if len(sys.argv) <= 1:
        print 'Usage: ahk [command] [param1, param2,...]'
        os._exit(0)

    if not cmp(sys.argv[1], 'push'):
        push(sys.argv)
        restart_ahk()
    elif not cmp(sys.argv[1], 'pop'):
        pop(sys.argv)
        restart_ahk()
    elif not cmp(sys.argv[1], 'list'):
        list()

