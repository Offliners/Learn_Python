# create custom iterators
class C:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        # let's stop when n = 3
        if self.n == 3:
            raise StopAsyncIteration
        self.n += 1
        return self.n

c = C()
i = iter(c) # get an iterator

for _ in range(5):
    try: # exception has to be caught
        print(next(i))
    except:
        break

# Output:
# 1
# 2
# 3
