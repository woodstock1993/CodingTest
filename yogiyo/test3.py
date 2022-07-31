# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Solution(object):
    def __init__(self):
        self.array = []
        self.transaction = []
        self.content = []
        pass

    def push(self, value):
        if len(self.transaction) >= 1:
            self.content.append({'push': value})
            self.transaction = []
        self.array.append(value)

    def top(self):
        if len(self.array) >= 1:
            return self.array[-1]
        if len(self.array) == 0:
            return 0

    def pop(self):
        if (len(self.array) == 0):
            return
        if len(self.transaction) >= 1:
            self.content.append({'pop': self.array[-1]})
            self.transaction = []
        if len(self.array) >= 1:
            return self.array.pop()

    def begin(self):
        if len(self.transaction) == 0:
            self.transaction.append(1)
            self.transaction = set(self.transaction)

    def rollback(self):
        if len(self.content) <= 0:
            return False
        dic = self.content[-1]
        command = ""
        value = ""
        for k, v in dic.items():
            command = k
            value = v
        if k == 'push' and len(self.array) >= 1:
            self.array.pop()
            return True
        elif k == 'pop' and len(self.array) >= 0:
            self.array.append(v)
            return True

    def commit(self):
        if len(self.content) >= 1:
            self.content = []
            return True
        if len(self.content) <= 0:
            return False


def test():
    # Define your tests here
    sol = Solution()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"
