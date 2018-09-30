#!/usr/local/bin/python3

import subprocess
import sys
import re
import math

def get_size(url):
    cmd = "curl -sI \"" + url + "\" | grep -i Content-Length: | grep -E -o \"[0-9]+\"" # About to execute this #
    # print("About to Execute:\n",cmd,"....")
    (status,output) = subprocess.getstatusoutput(cmd)
    if status:
        if status:
            sys.stderr.write(output)
            sys.exit(1)

    return output




def download_file(url,filename,part_size=300000000):
    max_part_size = part_size
    file_size = int(get_size(url))
    print("File Size: %d" % (file_size/1e6))
    num_parts = math.ceil(file_size/max_part_size)

    for x in range(0,num_parts):
        cmd = 'curl --range ' + str(x*max_part_size) + '-' + str( ( (x+1)*max_part_size - 1) )
        cmd += ' -o %s.part' % filename + str(x+1) + " " + url
        # args = [word for word in cmd.split()]
        print("About to execute:\n%s..." %(cmd))
        # continue
        completed_process = subprocess.run(cmd,shell=True)
        completed_process.check_returncode() 

    # Now I have all the parts I just have to join them now #
    for i in range(0,num_parts//10 + 1):
        if(i == 0):
            cmd = 'cat %s.part? > %s' % (filename,filename)
        else:
            cmd = 'cat %s.part%d? >> %s' % (filename,i,filename)

        args = [words for words in cmd.split()]
        print("About to execute:\n%s..." %(cmd))
        # continue
        completed_process = subprocess.run(cmd,shell=True)
        completed_process.check_returncode()


    print("Done :)")

def remove_parts(filename):
    cmd = 'rm %s.part*' % (filename)
    print("About to execute:\n%s..." %(cmd))
    completed_process = subprocess.run(cmd,shell=True)
    completed_process.check_returncode()
    return



def main():
    args = sys.argv[1:]

    if not args or args[0] != '-o':
        print("Usage: -o filename [--partsize (partsizeinMB) ] url [--rmparts]")
        return
    

    filename = args[1]
    del args[0:2]

    part_size = 300000000

    if args[0] == '--partsize':
        part_size = int(args[1]) * 1000000
        del args[0:2]

    url = args[0]

    download_file(url,filename,part_size)
    del args[0]

    if args:
        if(args[0] == '--rmparts'):
            remove_parts(filename)





if __name__ == '__main__':
    main()
