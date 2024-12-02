with open('./Data/day2.txt') as ifile:
    lines=ifile.readlines()
    lines=[i.split() for i in lines]
    
    def cast_list(line: list) -> list:
        return [int(i) for i in line]
    
    def cal_diff(line):
        return [line[i]-line[i-1] for i in range(1,len(line))]

    def is_increasing_by_k(diff_list: list, k=3) -> bool:
        return all([x>0 for x in diff_list]) and all([x in range(1,k+1) for x in diff_list])
    
    def is_decreasing_by_k(diff_list, k=3):
        return all([x<0 for x in diff_list]) and all([abs(x) in range(1,k+1) for x in diff_list])
    
    def part_one(lines: list) -> int:
        n_safe=0
        usl_ndx=[]
        for n, line in enumerate(lines):
            if is_increasing_by_k(line) or is_decreasing_by_k(line):
                n_safe+=1   
            else:
                usl_ndx.append(n)
        return n_safe, usl_ndx

    def part_two(lines: list, n_safe) -> int:
        for line in lines:
            for i in range(len(line)):
                diff_line=cal_diff(line[0:i]+line[i+1:len(line)])
                if is_increasing_by_k(diff_line) or is_decreasing_by_k(diff_line):
                    n_safe+=1
                    break
        return n_safe

    int_lines=[cast_list(line) for line in lines]
    diff_lines=[cal_diff(line) for line in int_lines]

    n_safe_p1, usl_ndx = part_one(diff_lines)
    print('Number of safe reports: ', n_safe_p1)

    lines_p2=[int_lines[i] for i in usl_ndx]
    
    print('Number of safe reports including single level failure tolerance: ', part_two(lines_p2,n_safe_p1))
                



