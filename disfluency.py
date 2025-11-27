# Rule-based disfluency/filler remover with conservative rules.
FILLERS = set([
    "uh", "um", "uhm", "erm", "like", "you know", "I mean", "so", "well"
])

def remove_fillers(text):
    # naive token-based removal; keeps case
    tokens = text.split()
    out = []
    i = 0
    while i < len(tokens):
        tok = tokens[i].lower().strip(".,?!")
        if tok in FILLERS:
            i += 1
            continue
        # remove repeated short tokens (e.g., "the the")
        if i+1 < len(tokens) and tokens[i].lower() == tokens[i+1].lower():
            # drop one
            i += 1
            continue
        out.append(tokens[i])
        i += 1
    return ' '.join(out)
