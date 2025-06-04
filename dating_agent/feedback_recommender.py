from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_feedback(path="data/feedback.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_candidates(path="data/candidates.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_user_preference_vector(feedback_list):
    liked_reasons = [f["reason"] for f in feedback_list if f["like"]]
    if not liked_reasons:
        return None
    embeddings = model.encode(liked_reasons, convert_to_tensor=True)
    return embeddings.mean(dim=0)

def recommend(user_vector, candidates, top_k=3):
    descriptions = [c["description"] for c in candidates]
    candidate_embeddings = model.encode(descriptions, convert_to_tensor=True)
    scores = util.cos_sim(user_vector, candidate_embeddings)[0]
    top_indices = scores.argsort(descending=True)[:top_k]
    return [candidates[i] for i in top_indices]

def run_feedback_based_recommendation():
    feedback_data = load_feedback()
    candidates = load_candidates()
    
    for user_data in feedback_data:
        print(f"為使用者 {user_data['user_id']} 推薦：")
        pref_vector = build_user_preference_vector(user_data["feedback"])
        if pref_vector is None:
            print("  沒有喜歡的理由，無法推薦。")
            continue
        top_candidates = recommend(pref_vector, candidates)
        for c in top_candidates:
            print(f"  - {c['id']}: {c['description']}")
        print()

if __name__ == "__main__":
    run_feedback_based_recommendation()
