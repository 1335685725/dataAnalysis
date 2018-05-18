game_result =[
        "X.O0",
        "XX.0",
        "XOO0"]

rotate_results = zip(*game_result)
for vresult in rotate_results:
        print(vresult)
print(rotate_results)