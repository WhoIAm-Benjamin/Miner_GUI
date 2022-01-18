import psutil as ps
from time import sleep as sl
from PySide2.QtWidgets import (QApplication,
                               QMainWindow)
#from PySide2 import QtCore
import design
# noinspection PyPep8Naming
from pyautogui import (moveTo as mt,
                       locateOnScreen as los,
                       mouseDown as md,
                       mouseUp as mu)
from threading import Thread as Th
from os import (system as s,
                getcwd as gcwd,
                path as pth)
import logging
from sys import exit as ex
from keyboard import (add_hotkey as a_h,
                      wait,
                      is_pressed as isp)

logging.basicConfig(level = logging.DEBUG,
              filename = r'logs.log',
              format = '%(asctime)s : %(levelname)s : %(message)s',
              filemode = 'a')

def runner():
    global run
    run = True
    window.changer()

def pause():
    global run
    run = False
    window.changer()

def restart():
    if isp('3'):
        logging.debug('restart')
        path = gcwd()
        s(pth.join(path, 'rest.exe'))

# def locker():
#     window.setWindowTitle('CryptoTab Miner Lite [Locked]')
#     wait('ctrl+5')
#     window.setWindowTitle('CryptoTab Miner Lite')

def miner(self):
    with open(r'settings.txt', 'r', encoding='utf-8') as f:
        settings = f.read()
    global percent, run, t, r, set_t
    settings = settings.split('\n')
    sleep = float(settings[0])
    set_t = int(settings[1])
    percent = 0.0
    r = 0
    run = True
    while self.defmain.value() == 0:
        pass
    sl(3)
    c_path = gcwd()
    i = 0
    while i<2:
        try:
            cr_path = pth.join(c_path, "crypt_tab.png")
            x, y, w, h = los(cr_path)
            del w, h
            mt(x+30, y+24)
            md(); mu()
            sl(5)
            del x, y
            break
        except TypeError:
            i+=1
    del i
    while run:
        percent = ps.cpu_percent(interval=0.5)
        sl(sleep)
        t = 0
        s('cls')
        if r == 1:
            return
        if not run:
            logging.debug('not run')
            while 1:
                try:
                    x, y, w, h = los(pth.join(c_path, 'miningDown.png'))#, region=(150, 100, 700, 350))
                    del w, h
                    mt(x+15, y+9)
                    md()
                    mt(x-150, y, duration=0.7)
                    mu()
                    while t < set_t:
                        s('cls')
                        sl(1); t += 1
                        if run: break
                    logging.debug('t = {}'.format(t))
                    t = 0
                    logging.debug('t = {}'.format(t))
                except TypeError:
                    continue
                if run: break
                try:
                    x, y, w, h = los(pth.join(c_path, "mining.png"))#, region=(150, 100, 700, 350))
                    del w, h
                    mt(x+9, y+8)
                    md()
                    mt(x+150, y, duration=0.7)
                    mu()
                    sl(2)
                    run = True
                except TypeError:
                    continue
        else:
            logging.debug('run')
            if percent >= 75:
                s('cls')
                sl(5)
                if ps.cpu_percent(interval=0.5) > 75:
                    run = False
            elif percent >= 70.0:
                for i in range(0,3):
                    try:
                        x, y, w, h = los(pth.join(c_path, 'miningDown.png'))#, region=(150, 100, 700, 350))
                        del w, h
                        mt(x+15, y+9)
                        md()
                        mt(x-150, y, duration=0.7)
                        mu()
                        sl(2)
                    except TypeError:
                        if i == 3:
                            pass
                        else:
                            sl(2)
                            continue
            elif percent <= 30.0:
                try:
                    x, y, w, h = los(pth.join(c_path, "mining.png"))#, region=(150, 100, 700, 350))
                    del w, h
                except TypeError:
                    continue
                mt(x+9, y+8)
                md()
                mt(x+150, y, duration=0.7)
                mu()
                sl(2)


class MainWindow(QMainWindow, design.Ui_mw):
    def __init__(self):
        global th1
        # noinspection PyArgumentList
        super().__init__()
        self.setupUi(self)
        self.defmain.valueChanged.connect(self.changer)

    def closeEvent(self, event):
        # th1.terminate()
        ex()

    def changer(self):
        global run
        # if ((self.defmain.value() == 1) and (run == False)) or ((self.defmain.value() == 0) and (run == False)):
        if not run:
            self.miner_st.setText('Off')
            self.miner_st.setStyleSheet("color: rgb(186, 2, 2);")
            self.defmain.setValue(0)
            run = False
        # elif (self.defmain.value() == 1) or (run == True):
        else:
            self.miner_st.setText('On')
            self.miner_st.setStyleSheet("color: rgb(71, 231, 22)")
            self.defmain.setValue(1)
            run = True


if __name__ == '__main__':
    global window, run
    run = None
    app = QApplication()
    window = MainWindow()
    window.show()
    a_h('1', runner)
    a_h('2', pause)
    a_h('3', restart)
    # a_h('4', exiting)
    a_h('4', lambda: s('taskkill /f /im Miner.exe'))
    # a_h('4', lambda: s('taskkill /f /im python.exe'))
    # a_h('5', locker)
    th1 = Th(target = miner, args = (window, ))
    th1.start()
    ex(app.exec_())
