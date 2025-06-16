🗳️ Wilson & Jason Election System
A console-based Python election system built for educational and simulation purposes. It allows users to register as voters or admins, cast votes, manage candidates, view reports, and analyze election results—all through a terminal interface with CSV-based persistent storage.

📌 Features
👤 Voter Actions

Register and log in

View candidates

Cast and modify votes

Provide feedback

🧑‍💼 Admin Actions

Add/remove voters and candidates

Analyze election data

View and count votes

View voter feedback

Save/load data to/from CSV

Generate reports

🗂 Persistent CSV Storage
Data is saved across three files:

voters.csv

candidates.csv

admins.csv

🧱 Technologies
Component	Technology
Language	Python 3
Data Storage	CSV Files
Interface	CLI (Command Line)

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/wilsonquilli/Wilson_and_Jason_Election_System.git
cd Wilson_and_Jason_Election_System
2. Run the Program
Make sure Python 3 is installed, then run:

bash
Copy
Edit
python main.py
3. Admin Key
Use the following admin key to sign up as an admin:

nginx
Copy
Edit
WJES
📂 File Structure
bash
Copy
Edit
Wilson_and_Jason_Election_System/
├── voters.csv            # Saved voter data
├── candidates.csv        # Saved candidate data
├── admins.csv            # Saved admin credentials
└── main.py               # Main Python file with all logic
📝 Example Usage
Launch the program.

Sign up as an admin using the key WJES.

Add candidates.

Sign up as a voter.

Log in and vote.

Admin can analyze results, view feedback, and generate reports.

🛡️ Security Notes
No password hashing or encryption — for learning/demo use only.

CSV files are used for simplicity instead of a database.

🤝 Contributors
Wilson Quilli

Jason

📜 License
This project is licensed for educational use. Feel free to fork and modify it to learn Python and basic file I/O operations.

