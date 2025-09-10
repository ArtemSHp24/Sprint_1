time_string = ('1h 45m,360s,25m,30m 120s,2h 60s')

parts = time_string.split(',')
total_minutes = 0


for part in parts:
    sub_part = part.split()


    for item in sub_part:
        if 'h' in item:
            item = item.replace('h', '')
            item = int(item)
            minutes = item * 60
            total_minutes += minutes
        elif 'm' in item:
            item = item.replace('m', '')
            item = int(item)
            total_minutes += item
        elif 's' in item:
            item = item.replace('s', '')
            item = int(item)
            minutes = item // 60
            total_minutes += minutes

print(total_minutes)

        



   
