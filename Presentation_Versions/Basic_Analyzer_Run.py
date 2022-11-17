from Preprocessing import masterDictionary, letNumCombos, bodiesNIDs

id_body = bodiesNIDs()

def parse(s):
    master_d = masterDictionary()
    let_num = letNumCombos()


    # Question mark check:
    if '?' in s:
        return  f'\nInput Text: \n\t{s} \n\nCategory:\n\t Question (? mark)\n\n-------------'

    #String to list
    p_o_s = []
    sent_d = {}
    s_lst = s.split()
    print(f"\nList version of input: \n\t{s_lst}")

     
    # Create list and dictionary diagrams
    for w in s_lst:
        if w in let_num:
            sent_d[w] = master_d.get(w)  #deals with letter-number hybrid (3dc)
        else: 
            sent_d[w] = master_d.get(w.lower())
    p_o_s = list(sent_d.values())
    print(f"\nList diagram: \n\t{p_o_s}")

    # Conditional check:
    if p_o_s[0] == 'conditional':
        return f'\nCategory:\n\t Question (conditional) \n\n-------------'

    # Interogative check:
    if p_o_s[0] == 'interogative':
        return f'\nCategory:\n\t Question (interrogative)\n\n-------------'

    # Other verb = 1st

    # Rules out present or past participles (regular verbs).
    #   If verb followed by noun or pronoun -> Question
    #   Else -> Command
    if p_o_s[0] == 'verb' and s_lst[0][-2:] != 'ed' and s_lst[0][-3:] != 'ing' and s_lst[0][-1:] != 's':
        if len(s_lst) <= 2:
            return f'\nCategory:\n\t Command (2 or fewer words)\n\n-------------'
        if p_o_s[1] == 'noun' or p_o_s[1] == 'pronoun':
            return f'\nCategory:\n\t Question (verb followed by noun or pronoun)\n\n-------------'
        else:
            return f'\nCategory:\n\t Command (verb NOT followed by noun or pronoun)\n\n-------------'
    
    #If 1st word != verb
    return f'\nCategory:\n\t Observation\n\n-------------'

print(parse(id_body[13][1]))
print(parse(id_body[12][1]))
print(parse(id_body[19][1]))
print(parse(id_body[2][1]))
print(parse(id_body[14][1]))
print(parse(id_body[1][1]))
print(parse(id_body[18][1]))







