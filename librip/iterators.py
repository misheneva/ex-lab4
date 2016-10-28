class Unique(object):
    def __init__(self, items, **kwargs):
        if ('ignore_case' in kwargs.keys()) and (kwargs['ignore_case']):
        	self.data = [str(i).lower() for i in items]
        else:
        	self.data = items

        self.index = 0
        self.mas = []

    def __next__(self):
        while self.data[self.index] in self.mas:
            self.index += 1
            if self.index == len(self.data):
                raise StopIteration

        self.mas.append(self.data[self.index])

        return self.data[self.index]

    def __iter__(self):
        return self
