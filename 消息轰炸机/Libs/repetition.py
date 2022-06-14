def run():
    print(r"Libs\repetition.py is runing.")
    import pyautogui
    import time
    import easygui as eg
    #导入库

    title="消息轰炸机"
    names=["内容：","次数："]
    result=eg.multenterbox("",title,names)
    msg=result[0]
    times=int(result[1])

    eg.msgbox("请做好准备，确认该消息后，在5秒内切换到消息窗口的输入框，轰炸开始后请不要移动鼠标。",title,"好的")
    # 设置切换窗口时准备的时间
    time.sleep(5)
    print("轰炸开始")
    mouse=pyautogui.position()
    print(mouse)
    #显示鼠标的x,y位置

    import pyautogui
    # 控制键盘鼠标
    import pyperclip
    # 控制电脑的复制版

    #split("/n")把文章分成一句一句的
    t=0
    for i in msg.split("/n")*times:
        t+=1
        print("第"+str(t)+"次："+i)
        pyautogui.click(mouse)
        #复制到截切版上去
        pyperclip.copy(i)
        #粘贴
        pyautogui.hotkey("ctrl", "v")
        #回车
        pyautogui.typewrite("\n")
        #发送
        pyautogui.hotkey("ctrl","enter")