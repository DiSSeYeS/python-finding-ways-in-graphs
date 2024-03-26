from string import ascii_uppercase # alphabet


global roads # globaling for use this variable in functions without calling


last = ascii_uppercase.find(input('Enter last letter of graph in english alphabet: ').upper())            # entering of last letter in graph
roads = {ascii_uppercase[i] : input(f'{ascii_uppercase[i]} --> ').upper().split() for i in range(last+1)} # letters may be in lowercase
end_letter = ''.join(filter(lambda x: roads[x] == [], roads.keys()))                                      # finding of letter from which there is no way
letter_to_del = input('Enter letter need to delete from ways (space if it doesn\'t need): ').upper()



def get_ways(letter):              # getting ways from selected letter
    res, ways, keys = [], roads.get(letter), list(roads.keys())
    for c in keys:                 
        temp = list(letter).copy() # make copy of letter as list for add there ways
        for k in ways:
            if k == c:             # if letter which is in key found in ways from key, then update list
                temp.append(c)
        if temp != list(letter):   # update result list if templist is not there
            res.append(temp)
    return res


def extend_of_ways(old, new):          # extending of two ways
    if len(new) > 0:                   # if length of list with new ways is 0, then just return old ways
        res = []
        for c in old:
            for k in new:
                temp = c.copy()
                if c[-1] == k[0]:      # if last letter of old way is first letter of new way, then expend
                    temp.extend(k[1:])
                if temp not in res:    # to avoid duplicates
                    res.append(temp)
        return res
    else:
        return old


res = get_ways(list(roads.keys())[0])
while not all(map(lambda x: x[-1] == end_letter, res)): # do until all ways contain the desired letter
    for c in list(roads.keys())[1:]:                    # find ways from 2nd letter of graph
        res = extend_of_ways(res, get_ways(c))


for c in res: # if need to delete some letter from ways
    if letter_to_del in c:
        res.remove(c)


print(len(res)) # now i can sleep calmly