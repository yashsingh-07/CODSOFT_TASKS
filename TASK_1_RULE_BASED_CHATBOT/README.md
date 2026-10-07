🏆 Alex - Sports Expert Chatbot

A rule-based sports chatbot built using Python for CodSoft Internship Task 1.

Alex is a command-line chatbot that answers predefined questions about different sports, famous players, rules, scoring systems, tournaments, and sports terminology.

---

🚀 Features

- 💬 Interactive command-line conversation
- 🧠 Rule-based responses using "if/elif" statements
- 🏏 Cricket information
- ⚽ Football / Soccer information
- 🏀 Basketball information
- 🎾 Tennis information
- 🏸 Badminton information
- 🏑 Hockey information
- 🏐 Volleyball information
- 🏓 Table Tennis information
- 🥊 Boxing information
- 🥋 Karate information
- 🏃 Athletics information
- 🏊 Swimming information
- 🏎️ Formula 1 information
- ⛳ Golf information
- 🏅 Olympics information
- 👤 Famous player information
- 📊 Basic rules and scoring
- 🏆 Major tournament information
- 🕐 Current date and time
- ❓ Help command
- 👋 Exit command
- 🛡️ Unknown-input handling

---

🛠️ Technologies Used

- Python 3
- datetime — Python standard library
- No external APIs
- No machine-learning libraries
- No external dependencies

---

📂 Project Structure

Alex-Sports-Expert-Chatbot/
│
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
├── CODSOFT_SUBMISSION.md
│
└── screenshots/
    ├── chatbot_start.png
    ├── cricket_demo.png
    ├── famous_player_demo.png
    ├── football_demo.png
    └── chatbot_exit.png

---

▶️ How to Run

1. Install Python

Download and install Python 3 from the official Python website.

2. Clone the repository

git clone https://github.com/yashsingh-07/Alex-Sports-Expert-Chatbot.git

3. Open the project folder

cd Alex-Sports-Expert-Chatbot

4. Run the chatbot

python main.py

If your system uses "python3":

python3 main.py

---

💬 Example Questions

You can ask Alex questions such as:

Hello

What can you do?

What are the formats of cricket?

Who is a famous player of cricket?

Who is Virat Kohli?

Tell me about MS Dhoni

What is T20?

What is football offside?

Who is Lionel Messi?

Who is a famous basketball player?

Who is Stephen Curry?

What are the Grand Slam tournaments?

Who is a famous badminton player?

Who is Usain Bolt?

Tell me about Formula 1

Who is a famous F1 driver?

What are the benefits of sports?

What time is it?

What is today's date?

help

bye

---

🧠 How the Chatbot Works

Alex uses a rule-based approach.

The basic process is:

User Input
     ↓
Convert input to lowercase
     ↓
Check predefined conditions
     ↓
Identify sport/topic
     ↓
Match keywords
     ↓
Generate predefined response
     ↓
Display response

For example:

elif "cricket" in user:
    cricket_response(user)

Inside the cricket function:

elif "virat" in user or "kohli" in user:
    print("Alex: Virat Kohli is an Indian international cricketer.")

This means the chatbot does not use machine learning or an external AI API. It responds according to predefined rules written in Python.

---

🎯 CodSoft Internship

Internship: CodSoft Internship
Task: Task 1 - Rule-Based Chatbot
Project: Alex - Sports Expert Chatbot
Programming Language: Python

---

📸 Screenshots

Screenshots of the chatbot running are available in the "screenshots" folder.

The screenshots demonstrate:

- Chatbot startup
- Cricket questions
- Famous player questions
- Football questions
- Chatbot exit

---

📚 Concepts Learned

This project helped me practice:

- Python variables
- Functions
- Conditional statements
- "if/elif/else"
- "while" loops
- String methods
- User input
- Functions and modular programming
- Date and time handling
- Rule-based chatbot development
- GitHub repository management

---

🔮 Future Improvements

Possible future improvements include:

- GUI using Tkinter
- Web-based chatbot interface
- Voice input and output
- Live sports scores using APIs
- Sports database integration
- Natural Language Processing
- More sports and athletes
- Conversation history
- Improved natural-language understanding

---

👨‍💻 Author

Nishesh Raj Singh

BTech CSE (AI/ML) Student

GitHub:
https://github.com/yashsingh-07

LinkedIn:
https://www.linkedin.com/in/nishesh-raj-singh-5b5246372/

---

📄 License

This project is licensed under the MIT License.