#codeBuddy.py - Advanced AI programming assistant
import json #used to store data, since AI needs past details from a conversation
import datetime #get current date, time, formatting
import random #used to make random choices
import re #smart text pattern recognition
from typing import Dict, List, Optional #use hints for better communication - returns a list, returns a dictionary,...

class codeBuddy:
    """ An advanced AI chatbot for programming assistance""" #docstring - explains what does the method do. triple quotations for multi lines
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
        self.responses = { #this is a data dictionary, other than a method
            "greeting":[ #inside the square brackets is a "list"
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
    def _load_knowledge_base(self)->Dict: #this is a type hint: telling this method is returning a dictionary
        """Load programming knowledge from file or create default"""
        return{ #three level structure : has three key values in it
            "python":{
                "variables": "In Python, variables store data. Example: x = 5",
                "functions": "Functions are defined with def. Example: def hello(): print('Hello')",
                "loops": "Python has for and while loops. Example: for i in range(5):",
                "lists": "Lists store multiple items: my_list = [1, 2, 3]",
                "dictionaries": "Dictionaries store key-value pairs: {'name': 'John'}",
                "classes": "Classes are blueprints for objects. Use class keyword."
            },
            "javascript":{
                "variables": "JS uses var, let, const: let x = 5;",
                "functions": "Functions: function hello() { console.log('Hello'); }",
                "loops": "for(let i=0; i<5; i++) { }",
                "arrays": "Arrays: let arr = [1, 2, 3];"
            },
            "concepts":{
                "oop": "Object-Oriented Programming uses classes and objects.",
                "api": "API = Application Programming Interface - how software communicates.",
                "debugging": "Debugging is finding and fixing errors in code.",
                "algorithm": "Algorithms are step-by-step problem-solving methods."
            }
        }
    def _save_conversation(self):
        """save conversation history to a file"""
        with open("chat_history.json","w") as f: #open a file under the name "----" and write
            json.dump({ #writes python content on a json file 
                "user":self.user_context["name"] or "Anonymous",
                "history":self.user_context["conversation_history"][-10], #last 10 messages 
                "timestamp":datetime.datetime.now().isformat()
            },f,indent = 2)
    def _handle_greeting(self, match) -> str: #type hint
        """Handle greeting messages"""
        return random.choice(self.responses["greeting"]).format(bot_name=self.name)  #formatting bot name with self.name      
    def _handle_help(self, match) -> str:
        """Show help menu"""
        help_text = """
        🤖 **I CAN HELP YOU WITH:**
        
        💻 **Programming Questions:**
        • Explain programming concepts
        • Provide code examples
        • Help debug errors
        • Explain different programming languages
        
        🛠️ **Features:**
        • Remembers your name and skill level
        • Saves conversation history
        • Provides personalized explanations
        • Generates simple code snippets
        
        💬 **Try asking:**
        • "Explain variables in Python"
        • "How to write a function?"
        • "What is OOP?"
        • "Show me a loop example"
        • "Help me debug this error: ..."
        
        Type 'bye' to exit. Happy coding! 🚀
        """
        return help_text            
    def _handle_explain(self, match) -> str:
        """Explain a programming concept"""
        user_input = match.string.lower() #converting the string to lowercase
        
        # Extract topic from input
        for topic in ["variable", "function", "loop", "class", "array", "list", "dictionary"]: #loop through this list
            if topic in user_input:
                lang = self.user_context["preferred_language"].lower()
                if lang in self.knowledge_base and topic in self.knowledge_base[lang]:
                    self.user_context["current_topic"] = topic
                    return f"📚 **{topic.title()} in {lang.title()}:**\n{self.knowledge_base[lang][topic]}"
        
        return "I can explain variables, functions, loops, classes, arrays, lists, and dictionaries. Which one?" #if the above statements are false           
        
    
