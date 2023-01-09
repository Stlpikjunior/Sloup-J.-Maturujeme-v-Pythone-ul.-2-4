fr = open('meteo_stanice.txt','r')
measure_count = 0
measured_temps = 0
max_temp = -100
max_code = ''
for row in fr:
    measure_count += 1
    row = row.strip().split(' ')
    numbers = row[3].split(',')
    code = row[0]
    temp = int(numbers[0] + numbers[1])
    measured_temps += temp
    if temp > max_temp:
        max_temp = temp
        max_code = code
    print(temp/10)
print('p.merani:', measure_count,'\n','max teplota a kod stanice:',max_temp/10,', ',max_code,'\n','priemer. teplota:',measured_temps/measure_count/10)



