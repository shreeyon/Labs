# 10. Given a list of temperatures in Celsius [36.5, 37.0, 39.2, 35.6, 38.7],convert them to Fahrenheit
# using map(),Filter out those above 100°F using filter().

c=[36.5, 37.0, 39.2, 35.6, 38.7]
n=list(map(lambda x: round((9*x+160)/5,2), c))
m=list(filter(lambda x: x>100, n))
print(m)

