import os


directory = input()
dict_files = {}
for root, dirs, files in os.walk(directory):
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in dict_files:
            dict_files[extension] = [f'---{file_name}{extension}']
        else:
            dict_files[extension].append(f'---{file_name}{extension}')
    for dir in dirs:
        for sub_root, sub_dirs, sub_files in os.walk(directory + '//' + dir):
            for file in sub_files:
                file_name, extension = os.path.splitext(file)
                if extension not in dict_files:
                    dict_files[extension] = [f'---{file_name}{extension}']
                else:
                    dict_files[extension].append(f'---{file_name}{extension}')
            break
    break

dict_files = {k: v for k, v in sorted(dict_files.items(), key=lambda x: x[0])}

with open(f'{directory}//report.txt', 'w') as f:
    for k, v in dict_files.items():
        f.write(k)
        f.write('\n')
        for file in sorted(v):
            f.write(file)
            f.write('\n')
