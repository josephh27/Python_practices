from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
freq = "ooookaayy"
my_counter = Counter(freq)
print(my_counter)
list_elem = list(my_counter.elements())
print(list_elem)

Point = namedtuple("Point", "x11 ,y ")
pt = Point(1, -4) 
print(pt.x11)

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["e"] = 5
ordered_dict["f"] = 6
print(type(ordered_dict))
print(ordered_dict["e"])

ordered_dict2 = dict({})
ordered_dict2["a"] = 1
ordered_dict2["b"] = 2
ordered_dict2["c"] = 3
ordered_dict2["d"] = 4
ordered_dict2["e"] = 5
ordered_dict2["f"] = 6
print(type(ordered_dict2))
print(ordered_dict2["f"])

default_dict = defaultdict(dict)
default_dict["a"] = "1"
default_dict["b"] = 2
default_dict["c"] = 3
default_dict["d"] = 4
default_dict["e"] = 5
default_dict["f"] = 6
print(type(default_dict))
val1 = default_dict.get("g", 10)
print(val1)

my_deque = deque()
my_deque.append(2)
my_deque.appendleft(1)
my_deque.append(3)
my_deque.extendleft([0,-1,-2])
print(my_deque)
my_deque.rotate(-5)
print(my_deque)
