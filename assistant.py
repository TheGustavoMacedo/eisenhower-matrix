import openai
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_KEY"))

conn = sqlite3.connect('matrix.db')
c = conn.cursor()

def table_extract():
    c.execute("SELECT * FROM eisenhower")
    rows = c.fetchall()

    return rows

def user_input():
    try:
        print('\n' + '╔' + '═' * 48 + '╗')
        user_input = input("║ 👤 You: ")
        print('╚' + '═' * 48 + '╝')
        if user_input == "":
            print("❌ You didn't type anything!")
            return None
        elif user_input in ["Bye", "Exit", "Quit"]:
            print('\n' + '┌' + '─' * 30 + '┐')
            print('│  See you soon 👋🏻🤖           │')
            print('└' + '─' * 30 + '┘\n')
            return "EXIT"
        return user_input
    except:
        print("⚠️  Error reading your message") 
        return None

def assistant_ia(rows, user_question):
    try:
        formatted_data = str(rows) if rows else "No data found in the table"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are an assistant specialized in Eisenhower Matrix analysis.
                                                 
                                                 Analyze data from the 'eisenhower' table with the following fields:
                                                 - id_task: Unique task ID
                                                 - task: Task name/title
                                                 - description: Detailed task description
                                                 - status: Task category within the matrix
                                                 - date: Date related to the task
                                                 
                                                 The status represents the 4 quadrants of the Eisenhower Matrix:
                                                 • "Do": Do It Now (Urgent + Important) - Crises, emergencies, critical deadlines
                                                 • "Decide": Schedule It (Important + Not Urgent) - Planning, prevention, development
                                                 • "Delegate": Delegate It (Urgent + Not Important) - Interruptions, some meetings, some calls
                                                 • "Delete": Eliminate It (Not Urgent + Not Important) - Distractions, some social media, excessive TV
                                                 
                                                 Provide clear analysis about productivity and time management based on the data."""},
                {"role": "user", "content": f"Table data: {formatted_data}\n\nUser question: {user_question}"}
            ],
            max_tokens=250,
            temperature=0.7
        )
        ia_output = response.choices[0].message.content
        return ia_output
    
    except Exception as e:
        return f"Error generating response: {str(e)}"
