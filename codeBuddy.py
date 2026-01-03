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
        
    def _handle_example(self, match) -> str: #gets parameters from here
        """Provide code examples"""
        user_input = match.string.lower()
        #this is a nested 
        examples = { 
            "python": { #dictionary for python
                "function": "```python\ndef greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('Alice'))\n```", #another dictionary
                "loop": "```python\nfor i in range(5):\n    print(f'Number: {i}')\n```",
                "list": "```python\nfruits = ['apple', 'banana', 'cherry']\nfor fruit in fruits:\n    print(fruit)\n```"
            },
            "javascript": {
                "function": "```javascript\nfunction greet(name) {\n    return `Hello, ${name}!`;\n}\n\nconsole.log(greet('Alice'));\n```",
                "loop": "```javascript\nfor(let i = 0; i < 5; i++) {\n    console.log(`Number: ${i}`);\n}\n```"
            }
        }
        
        lang = self.user_context["preferred_language"].lower()
        if lang in examples:
            for concept, code in examples[lang].items():
                if concept in user_input:
                    return f"💡 **Example of {concept} in {lang.title()}:**\n{code}" #replacing the place holders with the laguage user prefers
        
        return f"Tell me what example you want (function, loop, list, etc.) for {lang.title()}!"   #default 
    def _handle_concept(self, match) -> str: #in here, regex choose only the word part, not a single letter more than that
        """Handle specific programming concepts
        This function explains programming concepts when users mention them directly.
    It's triggered when the pattern matcher detects words like "variable", 
    "function", "loop", etc. in the user's message.
    
    HOW IT WORKS:
    1. Uses regular expressions to find specific programming terms in the user's input
    2. Extracts the matched concept (e.g., "variable", "function", "loop")
    3. Looks up the explanation from the knowledge base based on user's preferred language
    4. Returns a formatted explanation with the concept and its definition
    
    INPUT:
    - match: A regex match object containing the user's input text
    
    OUTPUT:
    - A formatted string explaining the concept
    - OR a fallback message suggesting available concepts
    
    EXAMPLES:
    - User: "What is a variable?" → Returns: "📖 **Variable in Python:**\nIn Python, variables store data..."
    - User: "Explain functions" → Returns: "📖 **Function in Python:**\nFunctions are defined with def..."
    - User: "How do loops work?" → Returns: "📖 **Loop in Python:**\nPython has for and while loops..."
    
    FEATURES:
    - Case-insensitive matching (matches "Variable", "VARIABLE", "variable")
    - Whole-word matching only (doesn't match "variables" inside "many variables")
    - Language-aware (uses user's preferred language from context)
    - Returns formatted response with emoji and bold text
    
    FALLBACK:
    If no concept is found or the concept isn't in the knowledge base,
    returns a helpful message listing available concepts.
    
    RELATED METHODS:
    - _handle_explain(): For "explain X" type requests
    - _handle_example(): For "show me example of X" requests
        """ #\b is a boundary
        concept_match = re.search(r'\b(variable|function|loop|class|array|list)\b', match.string, re.IGNORECASE) #re.search() searches for a pattern
        if concept_match: #if there is a matched element, this loop executes
            concept = concept_match.group(1).lower()
            lang = self.user_context["preferred_language"]
            if lang.lower() in self.knowledge_base and concept in self.knowledge_base[lang.lower()]:
                return f"📖 **{concept.title()} in {lang}:**\n{self.knowledge_base[lang.lower()][concept]}"
        return "I can explain variables, functions, loops, classes, arrays, and lists. Which one?"        
    def _handle_time(self, match) -> str:
        """Return current time"""
        now = datetime.datetime.now()
        return f"⏰ It's {now.strftime('%I:%M %p')} on {now.strftime('%A, %B %d, %Y')}"
    def _handle_thanks(self, match) -> str:
        """Handle thank you messages"""
        responses = [
            "You're welcome! Happy to help! 😊",
            "Anytime! Keep coding! 🚀",
            "Glad I could assist! Let me know if you need more help! 💻"
        ]
        return random.choice(responses)     
    def _handle_exit(self, match) -> str:
        """Handle exit command"""
        self._save_conversation()
        return "👋 Goodbye! Remember to save your code! Check out chat_history.json for our conversation." 
    def _handle_name(self, match) -> str:
        """Extract and remember user's name"""
        name = match.group(2).strip()
        self.user_context["name"] = name
        self.user_context["conversation_history"].append(f"User name set to: {name}")
        return f"Nice to meet you, {name}! I'll remember that. 😊"        
