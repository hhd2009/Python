def run():
	print(r"Libs\settings.py is running.")
	import os
	import easygui as eg

	title=name="消息轰炸机"

	try:
	    import winshell
	except ImportError as err:
	    print("Well, do nothing as 'winshell' lib may not available on current os")
	    print("error detail %s" % str(err))

	#当前工作目录
	work_path=os.path.abspath(".")
	print(work_path)

	#桌面文件夹的完整路径
	desktop=winshell.desktop()
	print(desktop)

	#程序路径
	p_path=work_path+r"\main.exe"
	print(p_path)

	def create_shortcut(bin_path:str,lnk_path:str,lnk_name:str,desc:str):
		shortcut = os.path.join(lnk_path,lnk_name + ".lnk")
		winshell.CreateShortcut(
			Path=shortcut,
			Target=bin_path,
			Icon=(bin_path, 0),
			Description=desc
		)

	choice=eg.choicebox("请您选择：",title,("创建桌面快捷方式","关于"))
	if choice=="创建桌面快捷方式":
		create_shortcut(p_path,desktop,name,name)
	elif choice=="关于":
		eg.msgbox("寒冬利刃制作。",title,"好的")
	else:
		pass