some_string = '1h 45m,360s,25m,30m 120s,2h 60s'
new_string = some_string.replace(' ' , ',')
last_string = new_string.split(',')
count_time = 0

for time in last_string: 
    if time[len(time)-1]== 'm':
        time = time[:len(time)-1]
        count_time += int(time) 
    elif time[len(time)-1]== 'h':
        time = time[:len(time)-1]
        count_time += int(time) *60
    elif time[len(time)-1]== 's':
        time = time[:len(time)-1]
        count_time += int(time) //60

print(count_time)