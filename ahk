#!/usr/bin/env sh
echo $AHK_HOME
ahk_file=Hotkeys.ahk
if [ $# -le 1 ] || [ $# -gt 3 ]
then
    echo "Wrong number of arguments"
    exit
elif [ $# -eq 2 ]
then
    if [ $1 != "pop" ]
    then
        echo "Wrong number of arguments for pop"
        exit
    else
        echo "poping"
        #pop the last map
    fi
else
    if [ $1 != "push" ]
    then
        echo "Wrong number of arguments for push"
        exit
    else
        echo "pushing"
        echo -e ":C*:$2::\nSend, $3\nReturn\n" >> $AHK_HOME/$ahk_file
        
        #push a map
    fi
fi

