
from sentence_transformers import SentenceTransformer, util
import numpy as np

# 1. Create a collection of documents
documents = [
    "Python is a popular programming language used for automation and web development.",
    "Machine learning allows computers to learn patterns from data.",
    "Deep learning uses neural networks with multiple layers.",
    "SQL is used to query and manage relational databases.",
    "PostgreSQL is an open-source relational database management system.",
    "Docker packages applications and their dependencies into containers.",
    "Git is a version control system used to track code changes.",
    "REST APIs allow applications to communicate over HTTP.",
    "Natural language processing helps computers understand human language.",
    "Generative AI can create text, images, and other content.",
    "Neural networks are inspired by interconnected neurons in the brain.",
    "Data analysis involves cleaning, exploring, and interpreting data.",
    "HTML structures content on web pages.",
    "CSS controls the visual appearance of web pages.",
    "Operating systems manage computer hardware and software resources.",
    "Computer networks allow devices to exchange information.",
    "Cybersecurity protects systems and data from digital attacks.",
    "Cloud computing provides computing resources over the internet.",
    "Software testing helps identify defects in applications.",
    "Retrieval-Augmented Generation combines document retrieval with language generation."
]

print("Number of documents:", len(documents))

# 2. Load the pretrained embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    cache_folder="./model_cache"
)

print("Embedding model loaded successfully!")

# 3. Generate embeddings for all documents
document_embeddings = model.encode(
    documents,
    convert_to_tensor=True
)

print("Embedding generation complete!")
print("Embedding shape:", document_embeddings.shape)


#Add the semantic search function


def semantic_search(query, top_k=3):
    # Convert the search query into an embedding
    query_embedding = model.encode(
        query,
        convert_to_tensor=True
    )

    # Calculate similarity with all 20 documents
    similarities = util.cos_sim(
        query_embedding,
        document_embeddings
    )[0]

    # Get the indices of the highest-scoring documents
    top_indices = similarities.argsort(descending=True)[:top_k]

    print(f"\nSearch query: {query}")
    print(f"\nTop {top_k} results:\n")

    for rank, index in enumerate(top_indices, start=1):
        index = index.item()
        score = similarities[index].item()

        print(f"{rank}. {documents[index]}")
        print(f"   Similarity score: {score:.4f}\n")



if __name__ == "__main__":
    test_queries = [
        "How do computers learn from data?",
        "How can I store and retrieve information from a database?",
        "How do I track changes in my code?",
        "How can I build a website?",
        "How can I protect my computer from hackers?"
    ]

    for query in test_queries:
        semantic_search(query, top_k=3)
        print("-" * 60)

