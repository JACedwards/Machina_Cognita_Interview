from Preprocessing import masterDictionary, letNumCombos, bodiesNIDs

id_body = bodiesNIDs()

def parse(s):
    master_d = masterDictionary()
    let_num = letNumCombos()
    id_body = bodiesNIDs()

    id_t = s[0]
    mult_sent = []
    ind_sent = []
    lst_sent = []

    #Check for multiple sentences, divided by comma

    if ',' in s[1]:
        i = s[1].index(',')
        ind_sent= s[1][:i]
        lst_sent.append(ind_sent) 
        mult_sent.append(lst_sent)

        lst_sent = []
        ind_sent= s[1][i+2:]
        lst_sent.append(ind_sent) 
        mult_sent.append(lst_sent)
        print(mult_sent)


    #Check for multiple sentences, divided by period, ignoring period at end
    elif '.' == s[1][-1]:
        s[1] = s[1][:-1]
        print(s[1])
        if '.' in s[1]:
            i = s[1].index('.')
            ind_sent= s[1][:-i]
            lst_sent.append(ind_sent) 
            mult_sent.append(lst_sent)

            lst_sent = []
            ind_sent= s[1][i+2:]
            lst_sent.append(ind_sent) 
            mult_sent.append(lst_sent)
            print(mult_sent)

    else:
        ind_sent.append(s[1])
        mult_sent.append(ind_sent)

    p_o_s = []
    sent_d = {}
    output = []

    ### Loop through separate sentences ###
    for i in range(len(mult_sent)): 
        if '?' in mult_sent[i][0]:
            output.append(mult_sent[i][0])
            output.append("Category = Question")

        else:
            w = mult_sent[i][0].split()
            for x in w:
                if x in let_num:
                    sent_d[x] = master_d.get(x) 
                else: 
                    sent_d[x] = master_d.get(x.lower())
            p_o_s = list(sent_d.values())
            print(f"this is list version of diagram: \n{p_o_s}")
            print(f"This is dictionary diagram: \n{sent_d}")

            if p_o_s[0] == 'conditional':
                output.append(mult_sent[i][0])
                output.append("Category = Question")

            elif p_o_s[0] == 'interogative':
                    output.append(mult_sent[i][0])
                    output.append("Category = Question: interrogative") 

            elif p_o_s[0] == 'verb' and w[0][-2:] != 'ed' and w[0][-3:] != 'ing' and w[0][-1:] != 's':
                if len(w) <= 2:
                    return f'\nCategory = Command (2 or fewer words)'
                if p_o_s[1] == 'noun' or p_o_s[1] == 'pronoun':
                    output.append(mult_sent[i][0])
                    output.append("Category = Question")                
                else:
                    output.append(mult_sent[i][0])
                    output.append("Category = Command")                      
            else:
                output.append(mult_sent[i][0])
                output.append("Category = Observation")                  

    output.insert(0, id_t)
    return output

print(parse(id_body[0][1]))







