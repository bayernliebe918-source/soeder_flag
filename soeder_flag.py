#!/usr/bin/env python

import time
import shutil
import os
import pyfiglet
from colorama import init, Fore, Back, Style


class APP:
    def __init__(self):
        self.size = int(10)
        self.breite = shutil.get_terminal_size().columns
        self.reps = int(self.breite / (self.size*2))
        self.rest = self.breite - (self.reps * (self.size*2))
        os.system('clear')

    def frame(self, i, size):
        return str((Back.BLUE+(" "*size))+(Back.WHITE+(" "*(i*2)))+(Back.BLUE+(" "*size)))

    def draw_line(self, i, f, size):
        if self.rest >= 1:
            if size > self.rest:
                print((f * self.reps) + (Back.BLUE + (" " * self.reps)))
            else:
                if ((i*2) + size) > self.rest:
                    print((f * self.reps) + (Back.BLUE + (" " * size)) + (Back.WHITE + (" " * (self.rest-size))))
                else:
                    print((f * self.reps) + (Back.BLUE + (" " * size)) + (Back.WHITE + (" " * (i * 2))) + (Back.BLUE + (" " * (self.rest - size - (i * 2)))))
        else:
            print(f * self.reps)

    def run(self, speed, rp):
        size=i_t=self.size

        for i in range(1,rp):
            for i, size in zip(range(i_t), range(i_t,0,-1)):
                self.draw_line(i, self.frame(i, size), size)
                time.sleep(speed)


            for i, size in zip(range(i_t,0,-1), range(i_t)):
                self.draw_line(i, self.frame(i, size) ,size)
                time.sleep(speed)


if __name__ == "__main__":
    init(autoreset=True)
    app = APP()
    try:
        app.run(0,10)
        app.run(0.1,10000000)
        
    except KeyboardInterrupt:
        os.system('clear')
        print(pyfiglet.figlet_format("Soeder unser Koenig"))
