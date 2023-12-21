from fastapi import FastAPI, APIRouter
from __init__ import Config
import requests


_temp_body = """
{'text': '**Issue Type:** Feature Request\n\n**Project:** Backstage\n\n**Summary:** Update text input box\n\n**Description:**\n\nThe current text input box in Backstage is not very user-friendly. It is difficult to see what is being typed, and it is easy to make mistakes.\n\nI would like to request that the text input box be updated to make it more user-friendly. Some possible improvements include:\n\n* Increasing the font size of the text\n* Adding a border to the text box\n* Adding a placeholder to the text box\n* Making the text box wider\n\n**Priority:** Medium\n\n**Labels:** UX, Frontend\n\n**Acceptance Criteria:**\n\n* The text input box should be easy to see and use.\n* The text in the text box should be easy to read.\n* The text box should be wide enough to accommodate a reasonable amount of text.\n\n**Additional Information:**\n\nI would be happy to provide more information about this request if needed.'}"""

def get_jira_ticket(ticket_id: int):
  print(ticket_id)

def create_jira_ticket(body):
  resp = requests.post(url=Config.JIRA_HOST, headers={"Authorixation": Config.JIRA_TOKEN}, data=body)
  if resp.status_code != 201:
    print(resp.json())
    return {"error":resp.json()}
  return {"status":"ok", "message": resp.json()}

def add_jira_comment(body):
  resp = requests.post(url=Config.JIRA_HOST, headers={"Authorixation": Config.JIRA_TOKEN}, data=body)
  if resp.status_code != 201:
    print(resp.json())
    return {"error":resp.json()}
  return {"status":"ok", "message": resp.json()}

