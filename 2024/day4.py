with open('./Data/day4.txt') as ifile:
    h_lines=ifile.read().splitlines()
    v_lines=[]
    d_lines=[]
    d_nlines=[]
    m_lines=[]
    ##get vertical lines
    for i in range(len(h_lines[0])):
        v_lines.append(''.join(line[i] for line in h_lines))
    ##get diagonal strings
    def get_rdiagonal(lines):
        rd_str=''
        counter=0
        for line in lines[i:len(lines)]:
            rd_str+=line[counter]
            counter+=1
        return rd_str

    for i in range(len(h_lines[0])-3):
        d_nlines.append(get_rdiagonal(v_lines))
        d_nlines.append(get_rdiagonal(h_lines))
    d_nlines=[i for i in d_nlines[1:]]

    def get_ldiagonal(lines,i,counter,flag='upper'):
        ld_str=''
        if flag=='upper':
            for line in lines[:i+1]:
                ld_str+=line[i-counter]
                counter+=1
        elif flag=='down':
            for line in lines[i+1:len(lines)]:
                ld_str+=line[counter]
                counter-=1
        return ld_str
    for i in range(3,len(h_lines[0])):
        d_nlines.append(get_ldiagonal(v_lines,i=i,counter=0))
    for i in range(len(h_lines[0])-4):
        d_nlines.append(get_ldiagonal(v_lines,i=i,counter=len(h_lines)-1,flag='down'))
     
    def count_word(string, substrings='XMAS'):
        count=string.count(substrings)
        count+=string.count(substrings[::-1])
        return count
    
    p1_count=0
    all_=h_lines+v_lines+d_nlines
    for line in all_:
        p1_count+=count_word(line)
    print('Part one solution: ', p1_count)

    ##Part two

    def check_pattern(my_arr):
        l_diag=my_arr[0][0]+my_arr[1][1]+my_arr[2][2]
        r_diag=my_arr[2][0]+my_arr[1][1]+my_arr[0][2]
        if l_diag=='MAS' or l_diag=='SAM':
            if r_diag=='MAS' or r_diag=='SAM':
                return 1
        return 0
    
    p2_count=0
    for i in range(len(h_lines[0])-2):
        for j in range(len(h_lines[0])-2):
            
            my_arr=[line[j:j+3] for line in h_lines[i:i+3]]
            p2_count+=check_pattern(my_arr)
    print('Part two solution: ', p2_count)