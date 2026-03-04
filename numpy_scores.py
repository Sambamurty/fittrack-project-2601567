import numpy as np

# Task 1 - Generate and Inspect the Data

np.random.seed(42)
scores = np.random.randint(50,101,(5,4))
print(scores)
print("Score of the 3rd student in the second subject -",scores[2,1],"\n")
print("All scores of the last 2 students -",scores[-2:,:],"\n")
print("All scores of the first 3 students in subject 2 and 3 only -",scores[0:3,1:3],"\n")

# Task 2 - Analyze with Broadcasting

print("Column-wise Mean -",np.round(np.mean(scores,axis=0),2),"\n")

curve = np.array([5,3,7,2])
curved_score = scores + curve
curved_score = np.clip(curved_score,None,100)
print("Curved_score :",curved_score,"\n")

print("row-wise max -",np.max(curved_score,axis=1),"\n")

# Task 3 - Normalize and Identify

row_min = np.min(curved_score,axis=1,keepdims=True)
row_max = np.max(curved_score,axis=1,keepdims=True)

normalized_scores = (curved_score-row_min)/(row_max-row_min)
print(f"Normalize -{normalized_scores}\n")

max_idx = np.unravel_index(np.argmax(normalized_scores),normalized_scores.shape)
print(f"student index and subject index {max_idx}\n")

high_scores = curved_score[curved_score>90] 
print(f"scores above then 90 -{high_scores}")




