import Reversi
import myPlayer
import randomPlayer
import time
from io import StringIO
import sys



def launchLocalGame(result=None):
    b = Reversi.Board(10)

    players = []
    player1 = myPlayer.myPlayer()
    ##player1.setHeuristic(simpleEvaluator.simpleEvaluator())
    player1.newGame(b._BLACK)
    players.append(player1)
    player2 = randomPlayer.randomPlayer()
    player2.newGame(b._WHITE)
    players.append(player2)

    totalTime = [0, 0]  # total real time for each player
    nextplayer = 0
    nextplayercolor = b._BLACK
    nbmoves = 1

    while not b.is_game_over():

        print("Referee Board:")
        print(b)
        print("Before move", nbmoves)
        print("Legal Moves: ", b.legal_moves())
        nbmoves += 1
        otherplayer = (nextplayer + 1) % 2
        othercolor = b._BLACK if nextplayercolor == b._WHITE else b._WHITE

        currentTime = time.time()
        move = players[nextplayer].getPlayerMove()
        totalTime[nextplayer] += time.time() - currentTime
        print("Player ", nextplayercolor, players[nextplayer].getPlayerName(), "plays" + str(move))
        (x, y) = move
        if not b.is_valid_move(nextplayercolor, x, y):
            print(otherplayer, nextplayer, nextplayercolor)
            print("Problem: illegal move")
            break
        b.push([nextplayercolor, x, y])
        players[otherplayer].playOpponentMove(x, y)

        nextplayer = otherplayer
        nextplayercolor = othercolor

        print(b)

    print("The game is over")
    print(b)
    (nbwhites, nbblacks) = b.get_nb_pieces()
    print("Time:", totalTime)
    print("Winner: ", end="")
    if nbwhites > nbblacks:
        print("WHITE")
        if result is not None: result.addLose()
    elif nbblacks > nbwhites:
        print("BLACK")
        if result is not None: result.addWin()
    else:
        print("DEUCE")
        if result is not None: result.addDeuce()
    if result is not None: result.addScore(nbblacks, nbwhites)


launchLocalGame()
