# print('Введите путь до файла с информацией для формирования админского пути:')
# path_start = input()
#
# print('Введите путь, куда хотите сохранить файл и название файла с расширением:')
# path_finish = input()

with open(r'E:\Gordey$\WS\Python\files\Общие папки.txt', 'r') as f:
    paths = f.read().splitlines()

path_list = []
for path in paths:
    path_list.append(path.split(';'))

path_true_list = []
for path in path_list:
    path_true_list.append('\\\\' + path[0] + '\\' + path[2].replace(path[2][1:2], '$'))

index = 0
flag = 0
with open(r'E:\GordeyGV$\WS\Python\\files\path_true_list2.txt', 'w') as file:
    # file.write('--------------------Гордей-----------------------------------------------------------------------------'
    #            '---\n')
    for line in path_true_list:
        # Без id
        file.write(line + '\n')
        # index += 1
