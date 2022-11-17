from Preprocessing import masterDictionary, letNumCombos, bodiesNIDs, noun, verb

id_body = bodiesNIDs()

def parse(s):
    master_d = masterDictionary()
    let_num = letNumCombos()
    noun_lst = noun()
    verb_lst = verb()


    # Question mark check:

    if '?' in s:
        return 'Question'

    p_o_s = []
    sent_d = {}
    s_lst = s.split()
    print(f"this is list version of input: \n{s_lst}")

   
    for w in s_lst:
        if w in let_num:
            sent_d[w] = master_d.get(w)  #deals with letter-number hybrid (3dc)
        else: 
            sent_d[w] = master_d.get(w.lower())
    p_o_s = list(sent_d.values())

    # print(f'Input text: \n"{s}"')
    print(f"\nList diagram:  \n{p_o_s}")
    print(f"\nDictionary diagram:  \n{sent_d}")

    #<Check if ANY words are both nouns and verbs. problem is that dictionary is already formed here.
    for i in range(len(s_lst)):
        if s_lst[i].lower() in noun_lst and s_lst[i].lower() in verb_lst:
            if i == 0:
                p_o_s[0] = 'verb'
            else:
                p_o_s[i] = 'noun'
                sent_d[s_lst[i]] = 'noun'
                print({f"Index {i} should be 'noun'"})
                print(f"This is refactored p_o_s:  \n{p_o_s}")
                print(f"This is refactored dictionary where 'request' should = 'noun': \n{sent_d}")


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

print(parse('Request for cougar to fly'))
#'Can you make a request tomorrow'
#'Request for cougar to fly'














