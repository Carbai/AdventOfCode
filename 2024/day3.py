import re

with open('./Data/day3.txt') as ifile:
    lines=ifile.readlines()
    line=''.join([i for i in lines])

    def get_matches(text, pattern, dis_pattern=None):
        if not dis_pattern:
            return re.findall(pattern,text)
        else:
            all_matches = [(m.group(), m.start(), m.end()) for m in re.finditer(pattern, line)]
            disable_matches = [(m.start(), m.end()) for m in re.finditer(dis_pattern, line)]
            return [match[0] for match in all_matches if not any(start <= match[1] and match[2] <= end for start, end in disable_matches)]   
    
    def get_res(matches):
        res=0
        for match in matches:
            res+=int(match.split(',')[0].split('(')[1])*int(match.split(',')[1].split(')')[0])
        return res
        
    ##Part one
    pattern = r"mul\(\d+\,\d+\)"
    print('Part one: ', get_res(get_matches(line,pattern)))

    ##Part two
    disable_pattern = r"don\'t\(\)(.|\n)*?do\(\)"  
    print('Part two: ', get_res(get_matches(line, pattern, dis_pattern=disable_pattern)))