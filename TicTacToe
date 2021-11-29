Board=[i for i in range(0,9)]
User,Computer='X','O'
Picks=[i for i in range(1,10)]
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

def print_board():
  x=1
  for i in Board:
    if  x%3==0:
      if i in('X','O'):print( i ,end='\n' + '---------'+'\n')
      else:print( i+1 ,end='\n' + '---------'+'\n')
    if x%3!=0:
      if i in('X','O'):print( i ,end=' | ')
      else:print( i+1 ,end=' | ')
    x+=1

def space_exist():
  return Board.count('X')+Board.count('O')!=9

def can_move(brd,plyr,mve):
  if mve in Picks and brd[mve-1]==mve-1:
   return True

def can_win(brd,plyr,mve):
  for i in winners:
    win=True
    for j in i:
      if brd[j]!=plyr:
        win=False
        break
    if win == True:break
  return win

def make_move(brd,plyr,mve,undo=False):
  if can_move(brd,plyr,mve):
    brd[mve-1]=plyr
    win=can_win(brd,plyr,mve)
    if undo:
      brd[mve-1]=mve-1
    return(True,win)
  else:return(False,False)
  
def computer_move():
  move=-1
  for i in range(1,10):
    if make_move(Board,Computer,i,True)[1]:
      move=i
      break
  if move==-1:
   for i in range(1,10):
      if make_move(Board,User,i,True)[1]:
        move=i
        break
  if move==-1:
    for i in range(1,10):
      if can_move(Board,Computer,i):
        move=i
  return make_move(Board,Computer,move)

while space_exist():
  print_board()
  move=int(input("Pick a number [1-9]" ))
  moved,won=make_move(Board,User,move)
  if not moved:
    print("pick another number you dumbfuck")
    continue
  if won:
    print("You won!")
  elif computer_move()[1]:
    print("You Lost")
    break
if not space_exist(): print("Tie")
print_board()
