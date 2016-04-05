#!/usr/bin/env python
import ConfigParser
import argparse
import os
import subprocess
import json
import sys

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

    subprocess.Popen("date", shell = True)
    #parse configurations from file
    cp = ConfigParser.ConfigParser()
    cp.read(config)
    secs = cp.sections()
    key = ""
    try:
        key = cp.get("key", "key")
    except ConfigParser.NoSectionError:
        print "no key section"
        sys.exit()
    except ConfigParser.NoOptionError:
        print "no key option in key section"
        sys.exit()

    path = ""
    path_json = ""
    try:
        path_json = cp.get("project", "path")
    except ConfigParser.NoSectionError:
        print "no project section"
        sys.exit()
    except ConfigParser.NoOptionError:
        print "no path option in project section"
        sys.exit()
    
    pathes = json.loads(path_json)

    for path in pathes:
        child = subprocess.Popen("cd " + path + " && eval `ssh-agent -s` && ssh-add " 
                + key + " && git pull", shell = True)
        child.wait()
        child = subprocess.Popen("cd " + path + " && eval `ssh-agent -s` && ssh-add " 
                + key + " && git push", shell = True)
        child.wait()

if __name__ == "__main__":
    main()
