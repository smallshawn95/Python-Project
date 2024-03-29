import json

with open("input.json", "r") as file:
    json_data = json.load(file)

with open("output.csv", "w") as file:
    # csv_label = [*json_data[0]] 另外方法
    csv_label = [label for label in json_data[0]]
    file.writelines(f"{','.join(csv_label)}\n")
    for data in json_data:
        csv_data = [str(data[label]) for label in csv_label]
        file.writelines(f"{','.join(csv_data)}\n")
