from groq import Groq
import time

client = Groq()
completion = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[
        {
            "role": "user",
            "content": "respond in fastest time"
        }
    ],
    temperature=0.5,
    max_tokens=32768,
    top_p=1,
    stream=True,
    stop=None,
)
start_time=time.time()
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")

print(f"\nElapsed time: {time.time() - start_time} seconds")
