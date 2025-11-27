# Lightweight punctuation and casing heuristics
import re
def naive_punctuate(text):
    # Split on long pauses indicated by '  ' or by sentence length heuristics
    # This is conservative: place a period every 12 tokens if no punctuation present.
    if not text:
        return text
    if any(p in text for p in '.?!'):
        # basic capitalization
        s = '. '.join([seg.strip().capitalize() for seg in re.split(r'[.?!]+', text) if seg.strip()])
        if s.endswith('.'):
            return s
        return s + '.'
    toks = text.split()
    if len(toks) <= 12:
        return text.capitalize() + '.'
    parts = []
    for i in range(0, len(toks), 12):
        part = ' '.join(toks[i:i+12]).capitalize() + '.'
        parts.append(part)
    return ' '.join(parts)
