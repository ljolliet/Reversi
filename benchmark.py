from testLocalGame import launchLocalGame
import result

size = 20
result = result.Result()
print("----- start benchmark ------")
for i in range(size):
    launchLocalGame(result)
print("----- end ------")

print("Results on a ", size, " Benchmark : \n", str(result))
