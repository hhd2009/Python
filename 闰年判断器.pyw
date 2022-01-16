import easygui as g

while True:
	Result_1_str=g.enterbox(msg='请输入年份：',title='闰年判断器')
	if Result_1_str=='' or Result_1_str is None:
		exit()
	Result_1_int=int(Result_1_str)
	Result_2_int=Result_1_int%4
	if Result_2_int==0:
		Result_3_str='闰年'
	else:
		Result_3_str='平年'
	g.msgbox(msg='年份：'+Result_1_str+'\n结果：'+Result_3_str,title='闰年判断器',ok_button='好的')