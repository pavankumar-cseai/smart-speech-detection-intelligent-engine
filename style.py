# Rule-based style transforms. Conservative by default.
CONTRACTIONS = {"do not":"don't", "does not":"doesn't", "I am":"I'm"}

def apply_style(text, style='neutral'):
    t = text
    if style.lower() == 'concise':
        # remove parentheticals and short adverbials naively
        import re
        t = re.sub(r"\([^\)]*\)", "", t)
        t = ' '.join([w for w in t.split() if len(w)>2 or w.lower() in ('a','an','to','of','in')])
    elif style.lower() == 'casual':
        for k,v in CONTRACTIONS.items():
            t = t.replace(k, v)
    elif style.lower() == 'formal':
        # expand common contractions conservatively
        for k,v in CONTRACTIONS.items():
            t = t.replace(v, k)
    return t
