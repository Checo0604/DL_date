def filter_and_score(user, candidates):
    scored = []
    for c in candidates:
        score = 0
        for like in user["likes"]:
            if like in c["description"]:
                score += 1
        for dislike in user["dislikes"]:
            if dislike in c["description"]:
                score -= 1
        if score > 0:
            scored.append((score, c))
    scored.sort(reverse=True)
    return [c for score, c in scored]
