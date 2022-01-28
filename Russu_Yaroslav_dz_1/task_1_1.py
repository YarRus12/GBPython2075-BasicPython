def convert_time(duration: int) -> str:
    if duration >= 86400:
        return days(duration)
    elif duration >= 3600:
        return hours(duration)
    elif duration >= 60:
        return minutes(duration)
    else:
        return seconds(duration)

def seconds(duration):
    s = duration
    return f'{s} сек'

def minutes(duration):
    m = duration//60
    s = duration%60
    return f'{m} мин {s} сек'

def hours(duration):
    h = duration // 3600
    m = (duration - (h*3600))//60
    s = duration % 60
    return f'{h} час {m} мин {s} сек'

def days(duration):
    d = duration // 86400
    h = (duration - d*86400) // 3600
    m = (duration - (d*86400) - (h*3600))//60
    s = duration % 60
    return f'{d} дн {h} час {m} мин {s} сек'

duration = 400153
result = convert_time(duration)
print(result)