from testLocalGame import launchLocalGame
import result
import myPlayer
import quickMovePlayer
import randomPlayer

# import lordinateursupreme

size = 3
assert size % 2 is 0  # size must be an even number ( multiple of 2)
first = result.Result()
second = result.Result()
print("----- start benchmark ------")
for i in range(size):
    player1 = quickMovePlayer.myPlayer()
    player2 = randomPlayer.myPlayer()
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
