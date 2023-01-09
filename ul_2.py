fr = open('hada.txt','r')
k = open('hadacopy.txt','w')
phier = 1
letc = 1
zoz = []
longest_game = 0
for row in fr:
   game_steps = 0
   if '\n' in row:
       phier += 1
   x = row.strip()
   for i in x:
       game_steps += 1
   if game_steps > longest_game:
       longest_game = game_steps
   zoz = []
   row += ' '
   lcount = 1
   lenght = len(row.strip())
   for i in range(0,lenght):
        if row[i] == row[i+1]:
            lcount += 1
        else:
            if lcount> 1:
              zoz.append(row[i] + str(lcount))
              lcount = 1
            else: zoz.append(row[i] + '1')

   k.write(str(zoz)+'\n')
print(phier)
print(longest_game)
# fr.close()
kr = open('hada.txt','r')
whole = kr.read()
k.write('\n'+whole)



