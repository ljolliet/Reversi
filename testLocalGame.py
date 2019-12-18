import Reversi
import myPlayer
import randomPlayer
import time


def launchLocalGame(result=None, player1=myPlayer.myPlayer(), player2=myPlayer.myPlayer()):
    b = Reversi.Board(10)

    players = []
    # player1 = quickMovePlayer.myPlayer()
    ##player1.setHeuristic(simpleEvaluator.simpleEvaluator())
    player1.newGame(b._BLACK)
    players.append(player1)
    # player2 = myPlayer.myPlayer()
    player2.newGame(b._WHITE)
    player2._multiprocessing = False
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

    print("\nThe game is over")
    (nbwhites, nbblacks) = b.get_nb_pieces()
    print("Time:", totalTime)
    print("Winner: ", end="")
    if nbwhites > nbblacks:
        print(player2.getPlayerName())
        if result is not None: result.addLose()
    elif nbblacks > nbwhites:
        print(player1.getPlayerName())
        if result is not None: result.addWin()
    else:
        print("DEUCE")
        if result is not None: result.addDeuce()
    if result is not None: result.addScore(nbblacks, nbwhites)

launchLocalGame()
