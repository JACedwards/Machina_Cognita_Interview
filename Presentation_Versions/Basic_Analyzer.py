from Preprocessing import masterDictionary, letNumCombos, bodiesNIDs

def parse(s):
    master_d = masterDictionary()
    let_num = letNumCombos()
    id_body = bodiesNIDs()

    # Question mark check:

    if '?' in s:
        return 'Question'

    p_o_s = []
    sent_d = {}
    s_lst = s.split()
    
    for w in s_lst:
        if w in let_num:
            sent_d[w] = master_d.get(w)  #deals with letter-number hybrid (3dc)
        else: 
            sent_d[w] = master_d.get(w.lower())
    p_o_s = list(sent_d.values())

    print(f'Input text: \n"{s}"')
    print(f"\nList diagram:  \n{p_o_s}")
    print(f"\nDictionary diagram:  \n{sent_d}")
  

    
    
    # sent_d = {'Have': 'verb', 'you': 'pronoun', 'observed': 'verb', 'firing': 'noun'}
    # p_o_s = ['verb', 'pronoun', 'verb', 'noun']

    #Check part of speech for FIRST WORD

    # Conditional check:
    if p_o_s[0] == 'conditional':
        return f'\nCategory = Question (conditional)'

    # Interogative check:
    if p_o_s[0] == 'interogative':
        return f'\nCategory = Question (interrogative)'

    # Verb = 1st
    # Neither questions nor commands are present or past participles, so rule those out.
    # (!= 's' would be one way of putting 'drones' in verb, but ruling out as verb because in
    #     1st position and neither questions nor commands would start with verb in indicative)
    if p_o_s[0] == 'verb' and s_lst[0][-2:] != 'ed' and s_lst[0][-3:] != 'ing' and s_lst[0][-1:] != 's':
        if len(s_lst) <= 2:
            return f'\nCategory = Command (2 or fewer words)'
        if p_o_s[1] == 'noun' or p_o_s[1] == 'pronoun':
            return f'\nCategory = Question (verb followed by pro/noun)'
        else:
            return f'\nCategory = Command'

    return f'\nCategory = Observation'

print(parse('Retain CP8'))







