horizon=3
vertic=3
free_cells=9
fass=[[" "," "," "],[" "," "," "],[" "," "," "]]
def judge(antipod):
	step_by_horizon=0
	checklist=[]
	for x in fass:
		checklist.append(x)
	while step_by_horizon<horizon:
		step_by_vetric=0
		post=[]
		while step_by_vetric<vertic:
			post.append(fass[step_by_vetric][step_by_horizon])
			step_by_vetric+=1
		checklist.append(post)
		step_by_horizon+=1
	c=0
	tost=[]
	ost=[]
	rev=horizon-1
	while c < vertic:
		tost.append(fass[c][c])
		ost.append(fass[c][(rev-c)])
		c+=1
	checklist.append(ost)
	checklist.append(tost)
	checked=[]
	for check in checklist:
		checked.append(" " in check or antipod in check)
	return not all(checked)
def show():
	print(" ",0,1,2)
	i=0
	while i<len(fass):
		print(i,*fass[i])
		i+=1
def damp():
	show()
	global free_cells
	while free_cells>0:
		mark=""
		compare=""
		if free_cells%2==0:
			mark="X"
			compare="O"
		else :
			mark="O"
			compare="X"
		entrance=input("Выберите клетку(строка,столбец).Ход "+mark).split(",")
		numbers=[]
		for i in entrance:
			numbers.append(int(i))
		if (numbers[0]>=len(fass) or numbers[1]>=len(fass[0])):
			print("Такой клетки нет!")
		elif (fass[numbers[0]][numbers[1]]!=" "):
			print("Эта клетка занята!")
		else:
			free_cells-=1
			fass[numbers[0]][numbers[1]]=mark
			show()
		if free_cells<=5:
			if judge(compare):
				print("Победил "+mark)
				break
damp()