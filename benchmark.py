from testLocalGame import launchLocalGame
import result

size = 20
result = result.Result()
print("----- start benchmark ------")
for i in range(size):
    print('\x1b[6;30;41m' +"################################### GAME NUMBER", str(i), "###################################" + '\x1b[0m');
    launchLocalGame(result=result)
print("----- end ------")

print("Results on a ", size, " Benchmark : \n", str(result))
