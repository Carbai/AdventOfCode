with open('./Data/day5.txt') as ifile:
    lines=ifile.read().strip('\n')
    rules,pages=lines.split('\n\n')[0].split(),lines.split('\n\n')[-1].split()
    
    def get_rules_dict(rules):
        my_dict={}
        for rule in rules:
            prev_page,next_page=rule.split('|')[0],[rule.split('|')[1]]
            try: 
                my_dict[prev_page].extend(next_page)
            except KeyError:
                my_dict[prev_page]=next_page
        return my_dict
    
    def is_ordered(rules_dict, pages):
        for i in reversed(range(1,len(pages))):
            try:
                rules=rules_dict[pages[i]]
                if len(set(pages[:i]).intersection(set(rules)))>0:
                    return False
            except KeyError:
                pass
        return True
    
    def get_ordered_pages(rules_dict, pages):
        old_page=None
        for i in reversed(range(1,len(pages))):
            curr_page=pages[i]
            while curr_page!=old_page:
                try:
                    rules=rules_dict[pages[i]]
                    if len(set(pages[:i]).intersection(set(rules)))>0:
                        res = list(set([pages[:i].index(x)for x in set(pages[:i]).intersection(set(rules))]))
                        pages[min(res)],pages[i]=pages[i],pages[min(res)]
                except KeyError:
                    pass
                old_page=curr_page
                curr_page=pages[i]
        return pages

    p1_res=0
    p2_res=0
    for page in pages:
        page=page.split(',')
        if is_ordered(get_rules_dict(rules), page):
            p1_res+=int(page[len(page)//2])
        else:
            ord_page=get_ordered_pages(get_rules_dict(rules),page)
            p2_res+=int(ord_page[len(page)//2])
    print('Solution to part one: ', p1_res)
    print('Solution to part two: ', p2_res)
