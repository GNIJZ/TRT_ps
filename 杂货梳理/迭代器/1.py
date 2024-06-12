class MyCollection:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]

    def __iter__(self):
        # 返回一个迭代器对象
        return MyIterator(self.numbers)

class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        # 迭代器本身就是一个迭代器对象，因此返回自身
        return self

    def __next__(self):
        if self.index < len(self.collection):
            # 返回当前元素并将索引加一
            result = self.collection[self.index]
            self.index += 1
            return result
        else:
            # 迭代结束，抛出 StopIteration 异常
            raise StopIteration

# 创建集合对象
collection = MyCollection()

# 使用 for 循环遍历集合中的元素
for number in collection:
    print(number)
