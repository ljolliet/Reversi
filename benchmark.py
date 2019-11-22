from testLocalGame import launchLocalGame
import result

size = 15
result = result.Result()
print("----- start benchmark ------")
for i in range(size):
    launchLocalGame(result=result)
print("----- end ------")

print("Results on a ", size, " Benchmark : \n", str(result))
