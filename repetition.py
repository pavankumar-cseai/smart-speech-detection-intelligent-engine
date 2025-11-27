import difflib
def dedupe_repetition(text):
    # conservative approach: remove immediate repeated runs
    tokens = text.split()
    out = []
    for i,t in enumerate(tokens):
        if i>0 and t.lower()==tokens[i-1].lower():
            continue
        out.append(t)
    return ' '.join(out)
