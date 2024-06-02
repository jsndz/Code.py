# b=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
b= {'TL':' ','TM':' ','TR':' ','ML':' ','MM':' ','MR': ' ','LL':' ','LM':' ','LR':' ',}
def printBoard():
	print(''+b['TL']+'|' +b['TM']+'|'+b['TR'] )
	print('-+-+-')
	print(''+b['ML']+'|' +b['MM']+'|'+b['MR'] )
	print('-+-+-')
	print(''+b['LL']+'|' +b['LM']+'|'+b['LR'] )


def userInput():
    count =0 
    while(count<9):
        move=input("Enter Your Key")
        a=input("enter player  choice for position")
        b[(a)]=move
        count =count +1
        printBoard()
        
        
printBoard()
userInput()