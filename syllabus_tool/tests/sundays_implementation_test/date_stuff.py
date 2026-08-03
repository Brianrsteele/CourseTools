from datetime import date, datetime, timedelta

t = date.today()
dt = datetime.now()
td = timedelta(days=7)

print(t, "|", dt, "|", t + td, "|", dt + td)
