
#If the space is blank, acept 'x' and 'o'
tic_tac_toe_board = [ [ ' ' , ' ' , ' ' ] , 
                      [ ' ' , ' ' , ' ' ] , 
                      [ ' ' , ' ' , ' ' ] ]

#    0  1  2
# 0 00 10 20
# 1 01 11 21
# 2 02 12 22
# 

def match( sequence, player ):
    if player == sequence[0][0] == sequence[1][1] == sequence[2][2]:
        print( 'Win' )

    elif player == sequence[2][0] == sequence[1][1] == sequence[0][2]:
        print( 'Win' )
        
    elif player == sequence[0][0] == sequence[1][0] == sequence[2][0]:
        print( 'Win' )
        
    elif player == sequence[0][1] == sequence[1][1] == sequence[2][1]:
        print( 'Win' )
        
    elif player == sequence[0][2] == sequence[1][2] == sequence[2][2]:
        print( 'Win' )
        
    elif player == sequence[0][0] == sequence[0][1] == sequence[0][2]:
        print( 'Win' )
        
    elif player == sequence[1][0] == sequence[1][1] == sequence[1][2]:
        print( 'Win' )
        
    elif player == sequence[2][0] == sequence[2][1] == sequence[2][2]:
        print( 'Win' )
        
    else:
        print( 'Lose' )
        

def progress( sequence ):
	print( '\n' )
	print( '   ' + sequence[0][0] + ' | ' + sequence[1][0] + ' | ' + sequence[2][0] + ' ' )
	print( '  ---+---+---' )
	print( '   ' + sequence[0][1] + ' | ' + sequence[1][1] + ' | ' + sequence[2][1] + ' ' )
	print( '  ---+---+---' )
	print( '   ' + sequence[0][2] + ' | ' + sequence[1][2] + ' | ' + sequence[2][2] + ' ' )
	print( '\n' )

def main():
	playing = True
	while playing:
		progress( tic_tac_toe_board )
		playing = False

main()