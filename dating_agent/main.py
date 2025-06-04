from planner import plan_recommendation
from grounder import find_matches
from verifier import filter_and_score
from answerer import generate_response
import json

def load_data():
    with open("data/users.json", "r", encoding="utf-8") as f:
        users = json.load(f)
    with open("data/candidates.json", "r", encoding="utf-8") as f:
        candidates = json.load(f)
    return users, candidates

def main():
    users, candidates = load_data()
    print("載入使用者：", users)
    print("候選對象：", candidates)

    for user in users:
        plan = plan_recommendation(user)
        print("推薦策略：", plan)

        matched = find_matches(user, candidates, plan)
        print("匹配結果：", matched)

        final = filter_and_score(user, matched)
        print("最終推薦：", final)

        for candidate in final:
            response = generate_response(user, candidate)
            print(response)


if __name__ == "__main__":
    main()
