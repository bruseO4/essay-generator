mport os
import openai
#$ pip install openai 
openai.api_key = os.getenv("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")


essay_prompt=input("Enter text to be autocompleted:\n")


response = openai.Completion.create(
  api_key = "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",
  engine="ada",
  prompt=essay_prompt,
  temperature=0.7,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
d
essay=essay_prompt+response.choices[0].text

print(essay)
