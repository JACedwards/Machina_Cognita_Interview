#  Lists of entries:  id + body

def bodiesNIDs():
    '''Lists of chat ID + text bodies'''

    id_body = [['d03f7fc5-46bf-4edc-a0c3-4ea0222c696a', 'ugv1 holding 75m east of cp17, awaiting instructions'],
['1a276751-2053-49fa-a025-d11725a0006a', 'Push to 17 to link with S3/4'],
['f1e762bd-236f-47be-9c06-46a6bb489c96', 'Retain CP8'],
['3b57f661-0452-4545-856f-978f4383df26', 'Withdraw to squad 4'],
['3afdc017-b1de-4042-9078-b01b9f2ed46a', 'We are sending boats back'],
['d45f679d-70a4-426a-a704-532944c90382', 'That also in a weird grid, are you getting a valid reading?'],
['2d344ba2-4bf1-4694-81ae-effcb15ca67b', 'uav scouting in front of squad 4'],
['3e7d58bb-fca3-4083-b098-a5bcf6144ceb', 'Squad three is halfway between checkpoint 18 And check .9 pushing South'],
['1b64f8e9-af36-4cbf-90fe-75bc22a54f38', 'ugv2 now pushing south to cp30, then west to cp17: no weapon active.'],
['20014dd7-29b7-4d12-b498-323795abc043', 'Squad 3 is Conducting accountability and will return to start location'],
['c5207108-898b-4303-8b40-f131dcde07d4', "Please pass the UAS 4 line as soon as you're able to for this run. It will help us get to where we're needed to adjudicate"],
['feccbe1b-d850-4f0d-8fdd-288dee92265d', 'Are uavs still enroute'],
['88201f43-a1e0-49f4-81cd-fbb59f4b601a', 'can you confirm uav mission'],
['c55c1396-85f8-4385-94dc-822ffd6821e2', 'Squad 4 update?'],
['32ed2883-038b-4682-ad57-ad4fc5ad910e', 'Have you observed firing'],
['080a5089-f1be-4fbe-a19b-50f77ec137e1', 'Squad three taking heavy contacts in multiple directions need reinforcements ASAP'],
['063ea395-2811-41d3-ae2e-668c10fa0590', 'Request for cougar to fly'],
['093ea395-2811-41d3-ae2e-668c10fa0590', 'Can you make a request tomorrow'],
['074ea395-2811-41d3-ae2e-668c10fa0590', 'Tomorrow I will request a boat'],
['f52e9493-becc-4b64-a2c5-ebe4e67e8fbc', "Why aren't we game on yet"]]

    return id_body

def masterDictionary():
    '''Lists of vocab from bodies by part of speech'''
    '''Dictionary:  key = vocab, value = part of speech'''

    noun = ['firing', 'uav', 'mission', 'uavs', 'squad', 'three', 'contacts', 'drone','directions', 'reinforcements', 'accountability', 'location', 'boats', 'halfway', 'checkpoint', 'check', 'south',  'way', '17', 'instructions', 'weapon', 'uas', 'line', 'run', 'where', 'cougar', 'request', 'boat', 'game']
    verb = ['have', 'observed', 'confirm', 'are', 'taking', 'need', 'is', 'conducting', 'will', 'return', 'scouting', 'are', 'sending', 'pushing', 'push', 'link', 'withdraw', 'retain', 'holding', 'awaiting', 'active', 'please', 'pass', 'able', 'will', 'help', 'get', 'needed', 'adjudicate', 'request', 'drone', 'fly', 'make', "aren't"]
    introg = ['who', 'when', 'how', 'how much', 'how many', 'what', 'why', 'whose', 'which']
    cond = ['would','could', 'should', 'can', 'may', 'might']
    pron = ['you', 'we', 'their', "you're", 'it', 'us', "we're", 'i']
    adj = ['uav', 'three', 'heavy', 'multiple', '3', 'enroute', 'still','front','start','18', '.9', 'no', 'this']
    adv = ['asap','back', 'east', 'now', 'south', 'then', 'west', 'soon', 'tomorrow', 'yet']
    prep = ['in', 'to', 'between', 'on', 'with', 'of', 'as', 'for']
    conj = ['and']
    art = ['the', 'a']
    let_num = ['S3/4', 'CP3','Cp9', 'CP8', 'ugv1', '75m', 'cp17', 'ugv2', 'cp30'] #temp workaround for .lower() issue below; edge '75m' not noun

    #Individual dictionaries by part of speech

    noun_d = {noun[i] : 'noun' for i in range(len(noun))}
    verb_d = {verb[i] : 'verb' for i in range(len(verb))}
    introg_d = {introg[i] : 'interogative' for i in range(len(introg))}
    cond_d = {cond[i] : 'conditional' for i in range(len(cond))}
    pron_d = {pron[i] : 'pronoun' for i in range(len(pron))}
    adj_d = {adj[i] : 'adjective' for i in range(len(adj))}
    adv_d = {adv[i] : 'adverb' for i in range(len(adv))}
    prep_d = {prep[i] : 'preposition' for i in range(len(prep))}
    conj_d = {conj[i] : 'conjunction' for i in range(len(conj))}
    art_d = {art[i] : 'article' for i in range(len(art))}
    let_num_d = {let_num[i] : 'noun' for i in range(len(let_num))}

    #Master dictionary
    master_d = noun_d | verb_d | introg_d | cond_d | pron_d | adj_d | adv_d | prep_d | conj_d | art_d | let_num_d

    return master_d


#Needed to access following lists individually in processing files

def noun():
    noun = ['firing', 'uav', 'mission', 'uavs', 'squad', 'three', 'contacts', 'drone','directions', 'reinforcements', 'accountability', 'location', 'boats', 'halfway', 'checkpoint', 'check', 'south',  'way', '17', 'instructions', 'weapon', 'uas', 'line', 'run', 'where', 'cougar', 'request', 'boat']

    return noun

def verb():
    verb = ['have', 'observed', 'confirm', 'are', 'taking', 'need', 'is', 'conducting', 'will', 'return', 'scouting', 'are', 'sending', 'pushing', 'push', 'link', 'withdraw', 'retain', 'holding', 'awaiting', 'active', 'please', 'pass', 'able', 'will', 'help', 'get', 'needed', 'adjudicate', 'request', 'drone', 'fly', 'make']
    return verb

def art():
    art = ['the', 'a']
    return art

def letNumCombos():
    '''Temporary workaround for problems caused by letter/number combos'''
    #Might solve via reg ex

    let_num = ['S3/4', 'CP3', 'Cp9', 'CP8', 'ugv1', '75m', 'cp17', 'ugv2', 'cp30']
    return let_num