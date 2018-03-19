import sys
from datetime import date
print(sys.argv)
date1 = date.today()
li = sys.argv[1].split("-")
date2 =  date(int(li[0]), int(li[1]),int(li[2]))
print ((date2 - date1).days)
