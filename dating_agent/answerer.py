def generate_response(user, candidate):
    reason = ""
    for like in user["likes"]:
        if like in candidate["description"]:
            reason += f"你喜歡的「{like}」對方也有提到；"
    return f"推薦 {candidate['id']}：{candidate['description']}。\n推薦理由：{reason}"
