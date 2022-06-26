import hea
import easygui as eg

text="CSDN官网：https://www.csdn.net"
eg.msgbox(text,"加密前")
e=hea.en(text)
eg.msgbox(e,"加密后")
une=hea.unen(e)
eg.msgbox(une,"解密后")