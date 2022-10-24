nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

def flat_generator(My_list):
   for list_ in My_list:
    for item in list_:
        yield item

class FlatIterator:
    def __init__(self, list_):
        self.My_list = list_

    def __iter__(self):
        self.cursor = 0
        self.cursor2 = -1
        self.full_list = []
        return self

    def __next__(self):
        self.cursor2 += 1
        if len(self.My_list[self.cursor]) == self.cursor2:
            self.cursor += 1
            self.cursor2 = 0
        if self.cursor == len(self.My_list):
            raise StopIteration
        self.full_list = self.My_list[self.cursor][self.cursor2]
        return self.full_list


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list2 = [item for item in FlatIterator(nested_list)] 
    print(flat_list2)

    flat_list = [item for item in flat_generator(nested_list)] 
    print(flat_list)         
    for item in flat_generator(nested_list):
        print(item)

