from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

for elem in tqdm(range(333)):
    sleep(0.005)
print()

for elem in ft_tqdm([1, 2, 3, 4, 5]):
    sleep(0.005)
print()

for elem in tqdm([1, 2, 3, 4, 5]):
    sleep(0.005)
print()
