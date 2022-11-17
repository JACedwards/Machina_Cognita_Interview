from Preprocessing import masterDictionary, letNumCombos, bodiesNIDs

id_body = bodiesNIDs()

def parse(s):
    master_d = masterDictionary()
    let_num = letNumCombos()


    # Question mark check:
    if '?' in s:
        return 'Question'

    p_o_s = []
    sent_d = {}
    s_lst = s.split()

     
    # Create list and dictionary diagrams
    for w in s_lst:
        if w in let_num:
            sent_d[w] = master_d.get(w)  #deals with letter-number hybrid (3dc)
        else: 
            sent_d[w] = master_d.get(w.lower())
    p_o_s = list(sent_d.values())

    # Conditional check:
    if p_o_s[0] == 'conditional':
        return f'\nCategory = Question (conditional)'

    # Interogative check:
    if p_o_s[0] == 'interogative':
        return f'\nCategory = Question (interrogative)'

    # Other verb = 1st

    # Rules out present or past participles (regular verbs).
    #   If length <= 2
    #   If verb followed by noun or pronoun -> Question
    #   Else -> Command
    if p_o_s[0] == 'verb' and s_lst[0][-2:] != 'ed' and s_lst[0][-3:] != 'ing' and s_lst[0][-1:] != 's':
        if len(s_lst) <= 2:
            return f'\nCategory = Command (2 or fewer words)'
        if p_o_s[1] == 'noun' or p_o_s[1] == 'pronoun':
            return f'\nCategory = Question (verb followed by pro/noun)'
        else:
            return f'\nCategory = Command'
    
    #If 1st word != verb
    return f'\nCategory = Observation'

print(parse(id_body[12][1]))







