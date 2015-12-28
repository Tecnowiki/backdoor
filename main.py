from urllib import urlopen
from sys import exit
from os import system

class Core():
    command = ""
    old_command = ""
    myserver = "http://wikitecno.altervista.org/command.txt"
    def __init__(self):
        link = urlopen(self.myserver)
        self.command = link.read().decode('utf8').strip()
        self.old_command = self.command

    def controll(self):
        while True:
            link = urlopen(self.myserver)
            self.command = link.read().decode('utf8').strip()
            if self.command != self.old_command:
                self.old_command = self.command
                print("Comando cambiato, nuovo comando: " + self.command)
                self.comando()

    def comando(self):
        #sintassi = "spegni + num.di.sec."
        if self.command[:6] == "spegni":
            var = "shutdown -f -s -t" + self.command[6:]
            print(var)
            #system(var)

        if self.command == "esci":
            exit(0)

a = Core()
a.controll()
