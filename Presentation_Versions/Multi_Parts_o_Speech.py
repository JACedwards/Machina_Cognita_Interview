from Preprocessing import masterDictionary, letNumCombos, bodiesNIDs, noun, verb, art

id_body = bodiesNIDs()

def parse(s):
    master_d = masterDictionary()
    let_num = letNumCombos()
    noun_lst = noun()
    verb_lst = verb()
    art_lst = art()

    if '?' in s:
        return 'Question: Ends in question mark'

    p_o_s = []
    sent_d = {}
    s_lst = s.split()
   
    for w in s_lst:
        if w in let_num:
            sent_d[w] = master_d.get(w)  
        else: 
            sent_d[w] = master_d.get(w.lower())
    p_o_s = list(sent_d.values())



    ###Deals with any instance where same word could be verb or noun###

    for i in range(len(s_lst)):
        if s_lst[i].lower() in noun_lst and s_lst[i].lower() in verb_lst:
            if i == 0:
                p_o_s[0] = 'verb'
                print(f"\nSentence: \n\t{s} \n\n Part of speech:  \n\t'request' = verb")
            else:
                if s_lst[i-1] in art_lst:
                    p_o_s[i] = 'noun'
                    sent_d[s_lst[i]] = 'noun'
                    print(f"\nSentence: \n\t{s} \n\n Part of speech:  \n\t'request' = noun")

                else:
                    p_o_s[i] = 'verb'
                    sent_d[s_lst[i]] = 'verb'
                    print(f"\nSentence: \n\t{s} \n\n Part of speech:  \n\t'request' = verb")

    ###End of multi-POS check###


    if p_o_s[0] == 'conditional':
        return f'\nCategory: \n\tQuestion (conditional)\n\n-------------'

    # Interogative = 1st:
    if p_o_s[0] == 'interogative':
        return f'\nCategory: \n\tQuestion (interrogative)\n\n-------------'

    # Other verb = 1st:
    if p_o_s[0] == 'verb' and s_lst[0][-2:] != 'ed' and s_lst[0][-3:] != 'ing' and s_lst[0][-1:] != 's':
        if len(s_lst) <= 2:
            return f'\nCategory: \n\tCommand (2 or fewer words)\n\n-------------'
        if p_o_s[1] == 'noun' or p_o_s[1] == 'pronoun':
            return f'\nCategory: \n\tQuestion (verb followed by pro/noun)\n\n-------------'
        else:
            return f'\nCategory: \n\tCommand\n\n-------------'
    
    #Something else = 1st:
    return f'\nCategory: \n\tObservation\n\n-------------'

print(parse('Can you make a request tomorrow'))  
print(parse('Request for cougar to fly'))
print(parse('Tomorrow I will request a boat'))















