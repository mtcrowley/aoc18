import re

f= open("input.txt","r")

a = [ [0] * 1100 for _ in range(1100)]

claims = f.readlines()

for claim in claims:
  num = int(re.search("(?<=#)[0-9]+(?= )",claim).group(0))
  xStart = int(re.search("(?<=@ )[0-9]+(?=,)",claim).group(0))
  yStart = int(re.search("(?<=,)[0-9]+(?=:)",claim).group(0))
  xLen = int(re.search("(?<=: )[0-9]+(?=x)",claim).group(0))
  yLen = int(re.search("(?<=x)[0-9]+",claim).group(0))
  for i in range(xStart,xStart+xLen):
    for j in range(yStart,yStart+yLen):
      a[i][j] = a[i][j] + 1


count = 0

for row in a:
  for item in row:
    if item > 1:
      count += 1

print(count)

for claim in claims:
  count = 0
  num = int(re.search("(?<=#)[0-9]+(?= )",claim).group(0))
  xStart = int(re.search("(?<=@ )[0-9]+(?=,)",claim).group(0))
  yStart = int(re.search("(?<=,)[0-9]+(?=:)",claim).group(0))
  xLen = int(re.search("(?<=: )[0-9]+(?=x)",claim).group(0))
  yLen = int(re.search("(?<=x)[0-9]+",claim).group(0))
  for i in range(xStart,xStart+xLen):
    for j in range(yStart,yStart+yLen):
      if a[i][j] > 1:
        count += 1
  if count is 0:
    print(num)
