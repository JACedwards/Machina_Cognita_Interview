from Preprocessing import masterDictionary, letNumCombos, bodiesNIDs


id_body = [['d03f7fc5-46bf-4edc-a0c3-4ea0222c696a', 'ugv1 holding 75m east of cp17, awaiting instructions'],
['1a276751-2053-49fa-a025-d11725a0006a', 'Push to 17 to link with S3/4'],
['f1e762bd-236f-47be-9c06-46a6bb489c96', 'Retain CP8'],
['3b57f661-0452-4545-856f-978f4383df26', 'Withdraw to squad 4'],
['3afdc017-b1de-4042-9078-b01b9f2ed46a', 'We are sending boats back'],
['d45f679d-70a4-426a-a704-532944c90382', 'That also in a weird grid,  are you getting a valid reading?'],
['2d344ba2-4bf1-4694-81ae-effcb15ca67b', 'uav scouting in front of squad 4'],
['3e7d58bb-fca3-4083-b098-a5bcf6144ceb', 'Squad three is halfway between checkpoint 18 And check .9 pushing South'],
['3fc4fae8-af37-4221-84ee-54ccc36bdf90', 'Drones on their way'],
['1b64f8e9-af36-4cbf-90fe-75bc22a54f38', 'ugv2 now pushing south to cp30, then west to cp17: no weapon active.'],
['20014dd7-29b7-4d12-b498-323795abc043', 'Squad 3 is Conducting accountability and will return to start location'],
['c5207108-898b-4303-8b40-f131dcde07d4', "Please pass the UAS 4 line as soon as you're able to for this run. It will help us get to where we're needed to adjudicate."],
['feccbe1b-d850-4f0d-8fdd-288dee92265d', 'Are uavs still enroute'],
['88201f43-a1e0-49f4-81cd-fbb59f4b601a', 'can you confirm uav mission'],
['c55c1396-85f8-4385-94dc-822ffd6821e2', 'Squad 4 update?'],
['32ed2883-038b-4682-ad57-ad4fc5ad910e', 'Have you observed firing'],
['080a5089-f1be-4fbe-a19b-50f77ec137e1', 'Squad three taking heavy contacts in multiple directions need reinforcements ASAP']]

def parse(s):
    print(f"Input text: \n\t{s[1]}")
    master_d = masterDictionary()
    let_num = letNumCombos()
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


    #Check for multiple sentences, divided by period, ignoring period at end.
    elif '.' in s[1]:

        if '.' == s[1][-1]:
            s[1] = s[1][:-1]
        
        i = s[1].index('.')
        ind_sent= s[1][:-i]
        lst_sent.append(ind_sent) 
        mult_sent.append(lst_sent)

        lst_sent = []
        ind_sent= s[1][i+2:]
        lst_sent.append(ind_sent) 
        mult_sent.append(lst_sent)

    else:
        ind_sent.append(s[1])
        mult_sent.append(ind_sent)

    
    p_o_s = []
    sent_d = {}
    output = []
    for i in range(len(mult_sent)): 
        w = mult_sent[i][0].split()
        for x in w:
            if x in let_num:
                sent_d[x] = master_d.get(x)  #deals with letter-number anomoly
            else: 
                sent_d[x] = master_d.get(x.lower())
        p_o_s = list(sent_d.values())

        # Conditional check:
        if p_o_s[0] == 'conditional':
            output.append(mult_sent[i][0])
            output.append("Question")

        ####hard coding for example that ends in an observation
        else:
            output.append(mult_sent[i][0])
            output.append("Observation")
        sent_d = {}
        p_o_s = []

    output.insert(0, id_t)
    return f"\nText ID: \n\t{output[0]}\n\nFirst sentence:\n\t{output[1]}\n\nCategory:\n\t{output[2]}\n\nSecond sentence: \n\t{output[3]}\n\nCategory:\n\t{output[4]}"

print(parse(id_body[9]))
# print(parse(['c5207108-898b-4303-8b40-f131dcde07d4', "Please pass the UAS 4 line as soon as you're able to for this run. It will help us get to where we're needed to adjudicate."]))







