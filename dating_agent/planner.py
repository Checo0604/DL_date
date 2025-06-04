def plan_recommendation(user):
    if user["state"]["new_user"]:
        return "broad"
    elif user["state"]["many_dislikes"]:
        return "strict"
    else:
        return "normal"
