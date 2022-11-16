import os 
import openai
from django.conf import settings




openai.api_key = settings.OPENAI_API_KEYS



def generate_blog_topic(topic, keywords):
    blog_topics = []

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Generate 10 blog topic ideas on the following topic : {topic}\nKeywords: {keywords} \n*",
    temperature=0.8,
    max_tokens=301,
    top_p=1,
    best_of=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
        else:
            return []
    else:
        return []

    b_list = res.split('*')
    if len(b_list) > 0:
        for blog in b_list:
            blog_topics.append(blog)
    else:
        return []
 
    return blog_topics

def generate_blog_section_headings(topic, keywords):

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Generate blog section headings and section titles based on the following blog section topic\nTopic : {topic}\nKeywords: {keywords}\n*",
    temperature=0.8,
    max_tokens=301,
    top_p=1,
    best_of=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            res = response['choices'][0]['text']
        else:
            res = None
    else:
        res = None
    
   
    return res


# topic = 'How to become an author'
# keyword = 'become an author, tips, guide, how to, aurthor'

# res = generate_blog_topic(topic, keyword).replace('\n', '')
# b_list = res.split('*')

# for blog in b_list:
#     blog_topics.append(blog)
#     print('\n')
#     print(blog)
#     print(blog_topics)