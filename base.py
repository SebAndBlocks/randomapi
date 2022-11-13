from datetime import *
ws = date(2022, 2, 23)
td = datetime.today().strftime(%Y, %m, %d)
wd = td - ws
print(wd.days)
