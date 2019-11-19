import testLocalGame
import result

size = 10
result = result.Result()
print("----- start benchmark ------")
for i in range(size):
    testLocalGame.launchLocalGame(result)
print("----- end ------")

print("Results on a ", size, " Benchmark : ", result.toPercent())
