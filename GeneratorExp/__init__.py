colors = ['black', 'white']
size = ['S', 'M', 'L']

for col in ('%s %s' % (c,s) for s in size for c in colors):
    print(col)

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for pasport in sorted(traveler_ids):
    print(*pasport)

for country, _ in traveler_ids:
    print(country)

lat, lon = lax_coordinates

print('%s/%s' % (lat,lon))
print(lon)
