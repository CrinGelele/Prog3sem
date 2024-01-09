class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = list(set([str(i) for i in items]))
        self.index = 0
        if self.ignore_case:
            tmp = []
            for i in self.items:
                if i.lower() not in [j.lower() for j in tmp]:
                    tmp.append(i)
            self.items = tmp

    def __next__(self):
        try:
            item = self.items[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return item

    def __iter__(self):
        return self
