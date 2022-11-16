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
        print(s_lst)
        if p_o_s[0] == 'verb' and s_lst[0][-2:] != 'ed' and s_lst[0][-3:] != 'ing' and s_lst[0][-1:] != 's':
            if len(s_lst) <= 2:
                return f'\nCategory = Command (2 or fewer words)'
            if p_o_s[1] == 'noun' or p_o_s[1] == 'pronoun':
                return f'\nCategory = Question (verb followed by pro/noun)'
            else:
                return f'\nCategory = Command'

        return f'\nCategory = Observation'

