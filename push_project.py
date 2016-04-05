#!/usr/bin/env python
import ConfigParser
import argparse
import os
import subprocess

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--config", help = "config file",
            action = "store", default = 'conf/push_project.conf')
    return parser
def main():
    #parse command line arguments
    ap = argparser() 
    args = ap.parse_args()
    config = args.config

    #parse configurations from file
    cp = ConfigParser.ConfigParser()
    cp.read(config)
    secs = cp.sections()
    for sec in secs:
        try:
            path = cp.get(sec, "path")
        except ConfigParser.NoOptionError:
            continue
        
        os.chdir(path)
        child = subprocess.Popen("git pull", shell = True)
        child.wait()
        child = subprocess.Popen("echo " + path 
                + "pull >> /home/liangjiang/code/scripts/out", shell = True)
        child.wait()
        child = subprocess.Popen("git push", shell = True)
        child.wait()
        child = subprocess.Popen("echo " + path 
                + "push >> /home/liangjiang/code/scripts/out", shell = True)
        child.wait()

if __name__ == "__main__":
    main()
