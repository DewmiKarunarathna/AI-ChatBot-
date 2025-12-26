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
    #coversation patters
    self.patterns = {   #this is a dictionary                                               
        r'\b(hi|hello|hey|greetings)\b': self._handle_greeting,
        r'\b(what can you do|help|features)\b': self._handle_help,
        r'\b(explain|what is|tell me about)\b.+': self._handle_explain,
        r'\b(how to|example of|show me)\b.+': self._handle_example,
        r'\b(python|javascript|java|c\+\+|html|css)\b': self._handle_language,
        r'\b(variable|function|loop|class|array|list)\b': self._handle_concept,
        r'\b(time|date|day)\b': self._handle_time,
        r'\b(thank you|thanks)\b': self._handle_thanks,
        r'\b(bye|exit|quit|goodbye)\b': self._handle_exit,
        r'\b(my name is|I am|call me)\b(.+)': self._handle_name,
        r'\b(beginner|intermediate|advanced)\b': self._handle_skill_level,
        r'\b(remember|what do you know|context)\b': self._handle_context,
        r'\b(debug|error|problem|fix)\b.+': self._handle_debug,
        r'\b(write code|generate|create)\b.+': self._handle_code_generation,
    }
    #response templates with personality
    self.responses = { 
        "greeting":[
            "Hello! I'm {bot_name}, your programming assistant! 👨‍💻",
            "Hey there! Ready to code? I'm {bot_name}! 🚀",
            "Hi! I'm {bot_name}, here to help with all things programming! 💻"
        ],
        "unknown":[
            "I'm not sure about that. Could you rephrase? 🤔",
            "That's interesting! Could you tell me more?",
            "I'm still learning about that. Ask me about programming instead! 📚"
        ]
    }
            
        
    
