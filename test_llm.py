import json
from openai import OpenAI

# Load the JSON file with stories
with open('stories.json') as f:
    stories = json.load(f)

# Initialize the OpenAI client
client = OpenAI(base_url="http://172.30.80.1:7878/v1", api_key="lm-studio")

# Define a placeholder for your prompt (replace `{story}` with the actual story)
prompt_placeholder = """
{story}
**Task-based Analysis of Customer Testimonial Data for [Company Name]**

**Objective: Extract key insights from the customer testimonial about [Company Name]'s Business Intelligence (BI) adoption and implementation process.**

**Guiding Questions:**

* What were the primary drivers behind [Company Name]'s BI adoption? (e.g., [adoption driver 1], [adoption driver 2], etc.)
* Which strategies did [Company Name] employ to successfully deploy its BI capabilities? (e.g., [implementation strategy 1], [implementation strategy 2], etc.)
* What were the most common challenges faced by [Company Name] during its BI implementation process, and how were they addressed? (e.g., [common challenge 1], [common challenge 2], etc.)
* How did [Company Name] monetize its BI capabilities? (e.g., [monetization approach 1], [monetization approach 2], etc.)
* What strategies did [Company Name] use to promote team collaboration and data-driven decision-making within its organization as a result of implementing BI?
* Does [Company Name] displays their dashboard in mobile apps?

**Output:** Please summarize the extracted information into the following categorical entities:

`drivers`: List of primary drivers behind [Company Name]'s BI adoption
`imp_strategies`: Strategies employed by [Company Name] to deploy its BI capabilities
`challenges`: Common challenges faced by [Company Name] during its BI implementation process and how they were addressed
`monetization`: Monetization approaches used by [Company Name]
`collaboration`: Strategies promoted by [Company Name] for team collaboration and data-driven decision-making
`mobile`: Information on mobile app usage for the dashboard

**Output Format:** Please provide the extracted information only in JSON format with the specified keys mentioned above.
"""

# Create an empty list to store the results
results = []

# Run the LLM model for each story
for i, story in enumerate(stories):
    # Extract the content and ID of the current story
    content = story['content']
    story_id = str(i)

    # Generate the prompt for the current story
    prompt = prompt_placeholder.replace('{story}', content)

    # Create a new completion request
    completion = client.chat.completions.create(
        model="MaziyarPanahi/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[
            {"role": "system", "content": "You are a helpful, smart, and efficient AI assistant, you're task is to analyze a customer testimonial from a BI service and extract some variables from it."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    # Extract JSON data from the response 
    response_text = completion.choices[0].message.content
    response_text = response_text.replace('\n', '')  # Remove newlines
    json_start_index = response_text.find('{')
    json_end_index = response_text.rfind('}') + 1
    json_text = response_text[json_start_index:json_end_index]

    try:
        extracted_data = json.loads(json_text)

        # Add the result, integrating the extracted JSON
        results.append({
            'story_id': story_id,
            # 'story_content': content,
            # 'response': response_text,  # Keep the original response
            **extracted_data  # Merge the extracted JSON
        })

    except json.JSONDecodeError:
        results.append({
            'story_id': story_id,
            # 'story_content': content,
            # 'response': response_text,  
            'json_error': 'Invalid JSON in response' 
        })
        
# Save the results in a JSON file
with open('results.json', 'w') as f:
    json.dump(results, f)