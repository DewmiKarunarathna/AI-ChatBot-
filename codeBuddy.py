#codeBuddy.py - Advanced AI programming assistant
import json #used to store data, since AI needs past details from a conversation
import datetime #get current date, time, formatting
import random #used to make random choices
import re #smart text pattern recognition
from typing import Dict, List, Optional #use hints for better communication - returns a list, returns a dictionary,...

class codeBuddy:
    """ An advanced AI chatbot for programming assistance"""
def __init__(self):
    self.name = "CodeBuddy🤖"
    self.user_context = {
        "name": None,
        "skill_level":"beginner",
        "current_topic": None,
        "conversation_history" : [],
        "preferred_language": "Python"
    }
    self.knowledge_base = self._load_knowledge_base()
    
    
