import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="google/gemma-3n-e2b-it:free",  # or any other supported model
    messages=[
        {"role": "user", "content": "Hello, who are you?"}
    ],
    temperature=0.7,
)

print(response["choices"][0]["message"]["content"])
