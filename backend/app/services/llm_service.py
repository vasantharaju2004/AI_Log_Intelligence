# for safe llm run
import os
from openai import OpenAI, RateLimitError

class LLMService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)

    def explain_incident(self, logs):
        if not self.client:
            return "LLM not configured. Using fallback explanation."

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You analyze production incidents."},
                    {"role": "user", "content": "\n".join(logs)}
                ]
            )
            return response.choices[0].message.content

        except RateLimitError:
            return (
                "LLM quota exceeded. Likely root cause involves service failure, "
                "resource exhaustion, or connectivity issues."
            )



# it is crashing with this client initialization
# import os
# from openai import OpenAI, RateLimitError


# # pure LLM AI logic gpt-3.5 turbo through api fetching AI answer.
# # for explaining  anomaly incident using chatgpt.
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# class LLMService:
#     def explain_incident(self, logs):
#         """
#         logs: list of anomaly log messages
#         """
#         prompt = f"""
#         You are a senior DevOps engineer.
#         Analyze the following application logs and explain:

#         1. What is the likely root cause?
#         2. Why did this issue happen?
#         3. Suggested fixes or preventive steps.PermissionError

#         Logs:
#         {chr(10).join(logs)} 
#         """
#         # using fallback RCA logic when LLM quota/bill/subscription 
#         # is exhausted to prevent system failure.
#         try:
#             response = client.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role":"system", "content":"You analyze production incidents."},
#                     {"role":"user", "content":prompt}
#                 ]
#             )

#             return response.choices[0].message.content
        
#         except RateLimitError:
        
#             # FallBack Explaination.
#             return (
#                 "LLM quota exceeded. Based on the error logs, the issue is likely "
#                 "related to service failures such as database connectivity, "
#                 "resource exhaustion, or configuration errors. "
#                 "Please check service health, retry logic, and infrastructure limits."
#             )
    

