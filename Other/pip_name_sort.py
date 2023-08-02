pip_data = input().split()
pip_lower_data = [name.lower() for name in pip_data]
pip_dict = {}
for i in range(len(pip_data)):
    pip_dict[pip_lower_data[i]] = pip_data[i]
pip_lower_data = sorted(pip_lower_data)
print(" ".join([pip_dict[name] for name in pip_lower_data]))
