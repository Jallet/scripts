#!/usr/bin/env python
import subprocess
import argparse

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--days", 
            help = "how many days before the \
                    data trashed will be parmenantly deleted",
            action = "store", type = int, default = 7)
    return parser
def main():
    trash_empty_cmd = "/usr/local/bin/trash-empty"
    parser = argparser()
    args = parser.parse_args()
    days = args.days
    output = subprocess.check_output("ls /home", shell = True)
    users = output.split("\n")
    subprocess.Popen("date", shell = True)
    cmd = trash_empty_cmd + " " + str(days)
    print cmd
    child = subprocess.Popen(cmd, shell = True)
    child.wait()
    for i in range(len(users) - 1):
        user = users[i]
        if user == "lost+found":
            continue
        else:
            cmd = "su -c \"" + trash_empty_cmd + " " + str(days) + "\" " + user
	    print cmd
            child = subprocess.Popen(cmd, shell = True)
            child.wait()


if __name__ == "__main__":
    main()
