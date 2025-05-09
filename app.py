from scriptGenerator import getScript
from xmlConverter import extract_user_actions
extract_user_actions("recording.xml")
selenium_data = getScript()

print(selenium_data)