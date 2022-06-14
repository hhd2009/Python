print("main.py is runing.")
from Libs import repetition,turn,settings
import easygui as eg
import sys

title="消息轰炸机"

if __name__=="__main__":
	while True:
		choice=eg.choicebox("请您选择：",title,("重复轰炸","顺序轰炸","设置","退出"))
		if choice=="重复轰炸":
			repetition.run()
		elif choice=="顺序轰炸":
			turn.run()
		elif choice=="设置":
			settings.run()
		elif choice=="退出" or choice==None:
			sys.exit()
		else:
			pass