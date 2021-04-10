from itertools import combinations
from tqdm import tqdm
import json

class CombinationsOfNumbers(object):

    def __init__(self, *numbers):
        self.numbers = [*numbers]
        self.all_results = []

    @staticmethod
    def operation(a, b, type):
        if type == 'add':
            return a + b
        if type == 'sub':
            return a - b
        if type == 'mul':
            return a * b
        if type == 'div':
            return a / b

    def all_combinations(self, numbers):
        if len(numbers) == 1:
            self.all_results.append(numbers[0])
            return 'Done'
        else:
            #self.all_results += numbers
            numbers_dict = {idx: num for idx, num in enumerate(numbers)}
            for idx1 in numbers_dict.keys():
                for idx2 in [key for key in list(numbers_dict.keys()) if key != idx1]:
                    for operation in ['add', 'sub', 'mul', 'div']:
                        number1 = numbers_dict[idx1]
                        number2 = numbers_dict[idx2]
                        try:
                            result = self.operation(number1, number2, operation)
                            self.all_results += [result]
                        except Exception as e:
                            continue

                        new_list = [result] + [numbers_dict[key] for key in numbers_dict.keys() if key not in [idx1, idx2]]
                        self.all_combinations(new_list)


def search(list):
    for i in range(1, 100):
        if i in list:
            continue
        else:
            return i-1


if __name__ == '__main__':

    all_combinations = {}


    import numpy as np
    L = np.arange(1, 30)
    for idx, comb in tqdm(enumerate(combinations(L, 4))):
        comb = list(comb)
        comb.sort()
        if str(comb) in list(all_combinations.keys()):
            continue
        else:
            obj = CombinationsOfNumbers(*comb)
            obj.all_combinations(obj.numbers)

            all_combinations[str(comb)] = search(obj.all_results)

    with open('result.json', 'w') as f:
        f.write(json.dumps({k: v for k, v in sorted(all_combinations.items(), key=lambda item: item[1])}, default=str, indent=4))