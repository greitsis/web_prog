class Dict(object):

    def __init__(self, d):
        self._d = d if d is not None else {}

    def sum_keys(self, key):
        arr = self._d.get(key, 0)
        sum = 0
        if arr == 0: 
        	print("Key", key, "does not exist")
        	return 0
        else:
    		n = len(arr)
        	for i in range(0, n ):
        		if i % 2 == 0 or 1 == 0:
        			sum += arr[i]
        			print(sum)
        			return arr
d1 = {
    "abc": [1, 2, 3],
    "def": [4, 5, 6],
    "klm": [7, 8, 9]
}

d2 = {
    ".": [],
    "-": [532, 0],
    ",": [0, 1, 0, -1]
}

d3 = {
    "one": [-1],
    "two": [0],
    "three": [1]
}

print(Dict(d1).sum_keys('abc'))
print(Dict(d1).sum_keys('def'))
print(Dict(d1).sum_keys('klm'))
print(Dict(d1).sum_keys('ADB'))

print(Dict(d2).sum_keys('.'))
print(Dict(d2).sum_keys('-'))
print(Dict(d2).sum_keys(','))

print(Dict(d3).sum_keys('one'))
print(Dict(d3).sum_keys('two'))
print(Dict(d3).sum_keys('three'))