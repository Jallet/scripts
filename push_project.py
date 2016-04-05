#!/usr/bin/env python
import ConfigParser
import argparse

def argparser():
    parser = argparse.ArgumentParser()
    parser.add("-f", "--config", help = "config file",
            action = "store", default = 'conf/push_projects.conf')
    return parser
def main():
    #parse command line arguments
    ap = argparser() 
    args = ap.parse_args()
    config = args.config

    #parse configurations from file
    cp = ConfigParser.ConfigParser()
    cp.read(config)
    sections = cp.sections()
    print "sections: ", sections, type(secs)
    
if __name__ == "__main__":
    main()
