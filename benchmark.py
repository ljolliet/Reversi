from testLocalGame import launchLocalGame
import result
import myPlayer
import randomPlayer
import lastEvaluator

size = 10
assert size % 2 is 0  # size must be an even number ( multiple of 2)
assert size > 0
first = result.Result()
second = result.Result()
print("----- start benchmark ------")
for i in range(size):
    player1 = myPlayer.myPlayer()
    player2 = myPlayer.myPlayer()
    player2.setEvaluator(lastEvaluator.myEvaluator(player2._board))
    print('\x1b[6;30;41m' + "################################### GAME NUMBER", str(i),
          "###################################" + '\x1b[0m')
    if i < size / 2:
        launchLocalGame(first, player1, player2)
    else:
        launchLocalGame(second, player2, player1)

print("----- end ------")

print("Results on a ", size, " Benchmark :")
print(player1.getPlayerName(), " starting")
print("First oppositions :\n", str(first))
print(player2.getPlayerName(), " starting")
print("Second oppositions :\n", str(second))
print("\nResume : ", player1.getPlayerName())
reverse = second.reverse()
first.add(reverse)
print(str(first))
