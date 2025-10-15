import numpy as np

name = np.array(['홍길동', '김철수', '임꺽정', '김이철', '철이임'])

print(np.char.find(name, '철'))

print(name[np.char.find(name, '철') != -1])