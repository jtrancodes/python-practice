keep_playing = True

def rps():
    player1_score = 0
    player2_score = 0

    while player1_score < 5 and player2_score < 5:
        player1 = input('Player 1, input rock (r), paper(p), or scissors (s): ')
        player2 = input('Player 2, input rock (r), paper(p), or scissors (s): ')

        if (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p'):
            # print('Player 1 wins.')
            player1_score += 1
        elif player1 == player2:
            print('It\'s a tie this round!')
        else:
            # print('Player 2 wins.')
            player2_score += 1
        
        print(f'Player 1 Score: {player1_score} ------- Player 2 Score: {player2_score}')

    if player1_score > player2_score:
        print('Congratulations to Player 1 for winning!')
    else:
        print('Congratulations to Player 2 for winning!')


while keep_playing:
    new_game = input('Would you like to start a new game of rock, paper, scissors? (y/n) ')

    if new_game == 'y':
        rps()
    else:
        keep_playing = False


