def find_matches(user, candidates, plan):
    keywords = user["likes"]
    matches = []
    for c in candidates:
        if any(kw in c["description"] for kw in keywords):
            matches.append(c)
    return matches
