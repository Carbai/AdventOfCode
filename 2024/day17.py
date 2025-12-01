from operator import add, sub, mul, truediv, xor, mod

with open('./Data/day17.txt') as ifile:
    lines=ifile.read().split()
    ops={'0': truediv, '1': xor, '2': mod, '3': xor,
         '4': xor, '5': mod, '6': truediv, '7': truediv}
    comb={'A': lines[2], 'B': lines[5], 'C': lines[8], 'prog': lines[-1].split(',')}
    print(comb)
    def do_ops(comb: dict, operations: dict) -> list:
        out=''
        combos={'0': 0, '1': 1, '2': 2, '3': 3, '4': int(comb['A']), 
                '5': int(comb['B']), '6': int(comb['C']), '7': None}
        program=comb['prog']
        pointer=0
        while pointer<len(program):
            i=pointer
            op=operations[program[i]]
            if program[i] in ['0','6','7']:
               # print('HERE')
                num=int(comb['A'])
                try:
                    den=2**combos[program[i+1]]
                   # print('num den',num,den)
                    res=int(num/den) 
                                   
                    if program[i] == '0':
                        comb['A']=res
                        combos['4']=res
                     #   print('UPDATING A', comb['A'])
                    elif program[i] == '6':
                    #    print('doing', num, den)
                        comb['B']=res
                        combos['5']=res
                    else:
                        comb['C']=res 
                        combos['6']=res 
                  #  out=out+','+str(comb['A'])
                except:
                    continue
                pointer+=2

            elif program[i] == '1':
             #   print('1', int(comb['B']), int(program[i+1]))
                try:
                    res=operations[program[i]](int(comb['B']),int(program[i+1]))
                    comb['B']=res
                    combos['5']=res
                 #   print('updated B', res)
                except:
                    continue
                pointer+=2
              #  print('POINTER', pointer)
            elif program[i] == '2':
             #   print('2 yoooo', operations[program[i]],combos[program[i+1]])
                try:
                    res=operations[program[i]](combos[program[i+1]],8)
                    comb['B']=res
                    combos['5']=res
                #    print('updated B', res, int(program[i]), operations[program[i]](6,6))
                except: 
                    continue

                pointer+=2
            elif program[i] == '3' and int(comb['A']==0):
                pointer+=2
            elif program[i] == '3' and int(comb['A']!=0):
                pointer=int(program[i+1])
            elif program[i] == '4':
                try:
                    res=operations[program[i]](int(comb['B']),int(comb['C']))
                    comb['B']=res
                    combos['5']=res
                except:
                    continue
                pointer+=2
            elif program[i] == '5':
              #  print('ENTERING HERE 5', program[i+1], combos[program[i+1]], operations[program[i]](combos[program[i+1]],8))
             #   print('OUOT', out)
                try:
                    res=operations[program[i]](combos[program[i+1]],8)
                    out=out+','+str(res)
                   # print('5', res, out)
                except:
                    continue
                pointer+=2
      #  print('updated', comb, 'output', out)
        return out
    print('Solution to part one: ', do_ops(comb, ops)[1:])
    
    comb={'A': lines[2], 'B': lines[5], 'C': lines[8], 'prog': lines[-1].split(',')}
    target=comb['prog']
    n=len(target)-1
    res=''
    prev=len(do_ops(comb, ops)[1:].split(','))
    new=0
    val_lw=8**n
    print('Solution to part one: ', do_ops(comb, ops)[1:])
##PART TWO
    comb={'A': str(val_lw), 'B': lines[5], 'C': lines[8], 'prog': lines[-1].split(',')}
    print(do_ops(comb, ops)[1:])
    val_up=8**(n+1)#val+(16*(8**14))
    comb={'A': str(val_up), 'B': lines[5], 'C': lines[8], 'prog': lines[-1].split(',')}
    res=do_ops(comb,ops)[1:]
    j=0
    print(val_lw,res)
    prev=[]
    k=0
    count_n={i: 0 for i in range(len(target))}
    val=val_lw
    prev=None
    while res.split(',') != target and val<=val_up and j<100:
            prev=val
            k=0
            comb={'A': str(val), 'B': lines[5], 'C': lines[8], 'prog': lines[-1].split(',')}
            res=do_ops(comb,ops)[1:]
            print('j', j, res, val, count_n[0], count_n[1], target)
            if res.split(',')[0]==target[0] and count_n[0]>=7:
                print('in first')
                val+=(57)
                count_n[0]=0
                count_n[1]=0 
            # if res.split(',')[1]==target[1] and count_n[1]>=7:
            #     print('in first 1')
            #     val+=(512-7)
            #     count_n[1]=0            
            else:
                print('in second')
                val+=1
                count_n[0]+=1
                count_n[1]+=1
            
          #  val+=1


            # while k != len(res.split(',')) and res.split(',')[k]==target[k]:   
            #     count_n[k]+=1     
            #     k+=1
            # if k==0:
            #     val+=1
            # elif count_n[k-1]!=8:
            #     val+=1
            # else:
            #     count_n[k-1]=0
            #     val+=64*(8**(k-1))-8+1             
            j+=1
    print(prev)

 
    