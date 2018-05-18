import json
filename = "population_data111.json"
with open(filename) as f:
    pop_data = json.load(f)
for pop_dict in pop_data:
    for k, v in pop_dict.items():
        if pop_dict[k] == "":
            print(pop_dict)
            print(k, v)
    print("--------------------------------------------------")