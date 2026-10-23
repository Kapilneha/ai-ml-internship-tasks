
import numpy as np


def get_top_results(scores, top_k=3):
    scores = np.asarray(scores)

    # Sort scores from highest to lowest
    top_indices = np.argsort(scores)[::-1][:top_k]

    return top_indices


# Dummy similarity scores for four documents
scores = [0.35, 0.91, 0.62, 0.80]

top_indices = get_top_results(scores, top_k=3)

print("Top document indices:", top_indices)

for rank, index in enumerate(top_indices, start=1):
    print(f"Rank {rank}: Document {index}, Score: {scores[index]:.2f}")
