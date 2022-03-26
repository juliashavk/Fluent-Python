from collections import namedtuple

City = namedtuple('City','name country population coordinates')
Tokyo = City('Tokyo','JP', 36.933, (35.689722, 139.691667))
print(Tokyo._fields)
print(Tokyo._asdict().keys())
print(Tokyo)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi=City._make(delhi_data)
print(delhi)
print(delhi._asdict().items())

print(reversed(Tokyo))