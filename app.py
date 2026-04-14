from endee import Client
import openai

# Initialize
client = Client()
openai.api_key = "YOUR_API_KEY"

# Step 1: Study material (you can change this)
notes = [
    "Photosynthesis is the process by which plants make food using sunlight.",
    "Newton's First Law states that an object remains at rest or in motion unless acted upon.",
    "Python is a popular programming language used for AI and web development.",
    "Machine Learning is a subset of Artificial Intelligence.",
    "The heart pumps blood throughout the human body."
]

# Store notes in Endee
for i, note in enumerate(notes):
    client.add(id=str(i), document=note)

print("📚 AI Study Assistant Ready!")
query = input("Ask your question: ")

# Step 2: Retrieve relevant note
results = client.search(query=query, top_k=1)
context = results[0]['document']

# Step 3: Generate answer
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Answer clearly using the given context."},
        {"role": "user", "content": f"Context: {context}\nQuestion: {query}"}
    ]
)

print("\n📖 Answer:")
print(response['choices'][0]['message']['content'])