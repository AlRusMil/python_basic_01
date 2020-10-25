time_seconds = int(input("Введите время (сек.): "))

hours = time_seconds // 360
time_seconds -= hours * 360
minutes = time_seconds // 60
seconds = time_seconds - minutes * 60

if (hours < 10):
    hours = '0' + str(hours)

if (minutes < 10):
    minutes = '0' + str(minutes)

if (seconds < 10):
    seconds = '0' + str(seconds)

print(f"{hours}:{minutes}:{seconds}")
