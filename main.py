import csv   #We imported CSV Files for our Storage System and the Data in Our Program/System

class Voter:   #Created a Class Voter For All the Attributes for Voters
    def __init__(self, name, voter_ID, age):   #Attributes such as a Voter's Name, their ID, and their Age
        self.name = name    #This Attribute is for the Name of the Voters
        self.voter_ID = voter_ID   #This Attribute is for the ID of the Voters
        self.age = age     #This Attribute is for the age of the Voters
        self.vote = None   #This is for the Vote Function and the Count of the Votes
        self.feedback = None   #This Attribute is for the Feedback Function

    def display(self):   #This Function will print out/display the details of a voter
        print(f"Name: {self.name}")   #Will display the Voter's Name
        print(f"voter_ID: {self.voter_ID}")   #Will display the Voter's ID
        print(f"Age: {self.age}")   #Will display the Voter's Age
        if self.vote:   #This will check if the voter has voted yet
            print(f"Vote: {self.vote}")    #If they did it will print out their vote
        if self.feedback:   #This will check if the voter has left any feedback
            print(f"Feedback: {self.feedback}")   #If there is any feedback, this will print out that feedback

class Candidate:   #Created a Class Candidate For All the Attributes for Candidates
    def __init__(self, name, party, goals):   #Attributes such as the Name, Their Political Party, and Their Goals as President for Candidates
        self.name = name   #This Attribute for the Name of the Candidate
        self.party = party   #This Attribute for the Party of the Candidate
        self.goals = goals   #This Attribute for the Goals of the Candidate

    def display(self):   #This function will print out/display the details of a Candidate
        print(f"Name: {self.name}")   #Will display the Name of a Candidate
        print(f"Party: {self.party}")   #Will display the Candidate's Political Party
        print(f"Goals: {self.goals}")   #Will display the Candidate's Goals as President

class Admin:   #Created a Class Admin For All the Attributes for Admins
    def __init__(self, username, password):   #Attributes such as the Username of an Admin and a Password for the Admin Account
        self.username = username   #This Attribute for the Username of the Admin
        self.password = password   #This Attribute for the Password of the Admin

class Election:   #Created a Big Class Election For All The Attributes for Election
    def __init__(self, voters_file="voters.csv", candidates_file="candidates.csv", admins_file="admins.csv"):   #Attributes for the Storage System and Election Candidates
        self.voters = []   #Voters in Election Class in a List
        self.candidates = []   #Candidates in Election Class in a List
        self.admins = []   #Admins in Election Class in a List
        self.voters_file = voters_file    #File of the Voters in Voters Storage CSV System
        self.candidates_file = candidates_file    #File of the Candidates Storage CSV System
        self.admins_file = admins_file   #File fo the Admins Storage CSV Storage
        self.admin_key = "WJES"   #Admin Key for New Admins Signing Up. #WJES - WilsonJasonElectionSystem
        self.feedback_list = []   #Feedback in a list for Admin's to view from their menu
        self.votes_info = {}   #This is to store votes in a dictionary to tell us who voted

    def add_voter(self, voter):   #Function for Adding a New Voter
        self.voters.append(voter)   #This will add the new voter to the list of voters

    def remove_voter(self, name):   #Function for Removing a Voter
        self.voters = [voter for voter in self.voters if voter.name.lower() != name.lower()]  #This will decrease the number of voters when wanted

    def add_candidate(self, candidate):   #Function for Adding a Candidate
        self.candidates.append(candidate)   #This will add the new candidate to the list of candidates

    def remove_candidate(self, name):   #Function for Removing a Candidate from that list
        self.candidates = [candidate for candidate in self.candidates if candidate.name.lower() != name.lower()]   #This will decrease the number of Candidates when wanted

    def add_admin(self, admin):   #Function for Adding a New Admin
        self.admins.append(admin)    #This will add a new Admin to the List of Admins

    def remove_admin(self, username):   #Function for Removing an Admin
        self.admins = [admin for admin in self.admins if admin.username.lower() != username.lower()]   #This will decrease the number of Admins when wanted

    def search_voters(self, name):   #Function for Admins to Search for a Voter
        return [voter for voter in self.voters if name.lower() in voter.name.lower()]   #This will look for the inputted voter in the list of voters

    def search_candidates(self, name):   #Function for Admins to Search for a Candidate
        return [candidate for candidate in self.candidates if name.lower() in candidate.name.lower()]   #This will look for the inputted voter in the list of voters

    def login_admin(self, username, password):   #The Login Function for Admins in the Main Menu with attributes of Username and Password
        for admin in self.admins:   #This will go through the list of admins
            if admin.username == username and admin.password == password:   #This will check if the username and the password match
                print("Admin Login Successfully!")   #This will print if they do match
                return True
        print("Invalid Admin Information.")   #This will print out if they don't match
        return False

    def signup_admin(self, username, password, key):   #The Signup Function for Admins in the Main Menu with attributes of Username, Password, and Key
        if key.lower() != self.admin_key.lower():   #This will check if the inputted key is equal to our admin key(WJES)
            print("Incorrect Admin Key!")  #This will print out when the key is wrong
            return False

        for admin in self.admins:   #Go through the list of admins
            if admin.username == username:   #This will check if the admin username already exists
                print("Admin Username Already Exists.")   #This will print out when the admin username already exists
                return False
        new_admin = Admin(username, password)   #If the key is right, it will create a new Admin
        self.add_admin(new_admin)   #Adds to list of admins
        print("Admin Signup Was Successful!")  #Prints after the New Admin was Created
        return True

    def login_voter(self, name, voter_ID):   #The Login Function for Voters in the Main Menu with attributes of their names and ID
        for voter in self.voters:   #This will go through the list of voters
            if voter.name.lower() == name.lower() and voter.voter_ID == voter_ID:   #This will check if their name and ID match
                print("Voter Login Successfully!")   #This will print out if they do match
                return voter
        print("Invalid Voter Information.")   #This will print out they don't match
        return None

    def signup_voter(self, name, voter_ID, age):   #The Signup Function for Voters in the Main Menu with Attributes of their names, ID, and Age
        age = int(age)  #This turns the inputted age into an integer
        if age < 18:   #If inputted age is less than 18
            print("You Must be 18 or Older to Sign Up!")  #This will Print Out
            return None
        for voter in self.voters:   #This will go through the list of Voters
            if voter.name.lower() == name.lower() and voter.voter_ID == voter_ID:   #This will check if the voter already exists
                print("Voter Already Exists.")   #Print if they do
                return None
        new_voter = Voter(name, voter_ID, age)  #Creates a new Voter
        self.add_voter(new_voter)   #Adds to the list of voters
        print("Voter Signup Was Successful. Now Just Log In.")   #Prints when Voter Signup worked
        return new_voter

    def vote(self, ID, candidate_name):   #Function for attributes of ID and the Candidate's Name when Someone votes
        voter = next((v for v in self.voters if v.voter_ID == ID), None)   #Finds the voter by their ID
        if voter:   #If the Voter is Found in the storage
            candidate = next((c for c in self.candidates if c.name.lower() == candidate_name.lower()), None)  #Finds the Candidate with their name
            if candidate:   #If the Candidate is found in the storage
                voter.vote = candidate_name   #This will set the vote of the voter to the candidate's name
                if candidate_name not in self.votes_info:   #If the candidate's name is not in votes_info, it will add it with the voter's information
                    self.votes_info[candidate_name] = [(voter.name, voter.voter_ID)]
                else:   #If the candidate's name is already in votes_info, it will append the voter's information
                    self.votes_info[candidate_name].append((voter.name, voter.voter_ID))
                print(f"Vote casted for {candidate_name}.")   #Prints the success message to show that they voted for someone
            else:
                print("Candidate Not Found")   #This will print out if the Candidate isn't found in the system
        else:
            print("Voter Not Found")   #This will print out if the Voter isn't found in the system

    def leave_feedback(self, name, voter_ID, feedback):   #Function for Attributes of a voter's name,their ID, and their feedback
        voter = next((v for v in self.voters if v.name.lower() == name.lower() and v.voter_ID == voter_ID), None)   #This will find the voter by their name and ID
        if voter:   #If the Voter is Found
            voter.feedback = feedback
            self.feedback_list.append((name, voter_ID, feedback))   #This will append the feedback to the list
            print("Feedback Submitted. Thank You!")  #This will print after submitting Feedback
        else:
            print("Invalid Voter Information.")  #This will print if the Voter isn't Found

    def view_feedback(self):   #Defining the view_feedback function for Admins
        if self.feedback_list:   #If any feedback is found
            print("Feedback from Voters:")   #This will print out
            for feedback in self.feedback_list:   #Will go through the list of feedback
                print(f"Name: {feedback[0]}, Voter ID: {feedback[1]}, Feedback: {feedback[2]}")  #This will print out the name of a voter, their ID, and the feedback they left if it's found
        else:
            print("Nobody Left Feedback :(")   #This will print out, if nobody left any feedback

    def election_analysis(self):   #Function for the Election Analysis
        print("Here's the Election Analysis:")
        for candidate_name, votes_info in self.votes_info.items():  #Will go through each candidate's votes information
            print(f"Candidate: {candidate_name}")  #Will print out the Candidate's name
            print("Votes:")
            for voter_info in votes_info:   #Will go through the list of voter's information who voted for the candidate
                voter_name, voter_ID = voter_info
                print(f"Voter Name: {voter_name}, Voter ID: {voter_ID}")  #This will print out the voter's name and ID
            print()

    def count_votes(self):   #Function for Counting Votes
        return sum(1 for voter in self.voters if voter.vote)   #Count the number of voters who have voted

    def generate_voter_report(self):  #Function for Admin's to View and Generate Voter Reports
        print("Voter Report: ")
        for voter in self.voters:   #This will go through the list of voters
            voter.display()   #This will print out along with voter report and display all the voters

    def generate_candidate_report(self):  #Function for Admin's to View and Generate Candidate Reports
        print("Candidate Report: ")
        for candidate in self.candidates:   #This will go through the list of candidates
            candidate.display()   #This will print out along with Candidate Report and display all the candidates

    def election_results(self):   #Defining the Function for Election Results
        print("Election Results: ")
        if not self.voters:   #This will check if there are no voters
            print("No Votes Have Been Made Yet.")   #This will print out if no votes have been made yet
            return
        votes_count = {}   #Storing the count of votes for each candidate in a dictionary

        for voter in self.voters:   #Go through each voter in the list
            if voter.vote:    #This will check if the voter has voted yet
                if voter.vote in votes_count:
                    votes_count[voter.vote] += 1   #This will add the vote for that candidate
                else:
                    votes_count[voter.vote] = 1  #This will initialize the count of votes for that candidate

        for candidate_name, votes in votes_count.items():   #This will go through the dictionary of voters
            print(f"{candidate_name}: {votes} votes")  #This will print out the candidate's name and the number of votes they got

        if votes_count:   #If there are any votes
            winner = max(votes_count, key=votes_count.get)   #Find the candidate with the most number of votes
            print(f"The Winner of the Election is {winner}!")   #This will print out the winner
        else:
            print("No Votes Have Been Made Yet.")   #If there are no votes, this will print out

    def save_data(self):   #Defining the Save_Data Function with Try and Except statements/method
        try:
            with open(self.voters_file, "w", newline="") as f:   #This will open the voters file for writing
                writer = csv.writer(f)   #This will create a CSV writer
                writer.writerow(["Name", "ID", "Age"])
                for voter in self.voters:   #This will go through each voter in the list
                    writer.writerow([voter.name, voter.voter_ID, voter.age])   #Write/Save the Voter's Data to the file storage system
        except Exception as e:  #This will handle error exceptions
            print(f"Error saving voters data: {e}")   #Prints this error message after error handling
        try:
            with open(self.candidates_file, "w", newline="") as f:   #This will open the candidates file for writing
                writer = csv.writer(f)   #This create a CSV writer
                writer.writerow(["Name", "Party", "Goals"])
                for candidate in self.candidates:   #Goes through the list of candidate
                    writer.writerow([candidate.name, candidate.party, candidate.goals])  #Writes/saves the candidate's data to the files
        except Exception as e:   #Error Handling
            print(f"Error saving candidates data: {e}")   #Prints this error message after error handling

    def load_data(self):   #Defining the Load Data Function to load data when the program initialize
        try:
            with open(self.voters_file, "r") as f:   #Open the voters file for reading
                reader = csv.DictReader(f)   #Creates a CSV Reader
                for row in reader:   #Goes through each row in the file
                    voter = Voter(row["Name"], row["ID"], row["Age"])   #Creates a new a Voter for data storage
                    self.voters.append(voter)   #Adds the new voter to the list of voters
        except FileNotFoundError:   #Error Handling
            pass   #Pass the Code through to do nothing if the file isn't found
        try:
            with open(self.candidates_file, "r") as f:   #Opens the Candidates File for Reading
                reader = csv.DictReader(f)   #Creates a CSV Reader
                for row in reader:   #Goes through each row in the file
                    candidate = Candidate(row["Name"], row["Party"], row["Goals"])   #Creates a new Candidate from the row data
                    self.candidates.append(candidate)   #Adds the new Candidate to the list of Candidates
        except FileNotFoundError:   #Error Handling
            pass   #Passes the code through to do nothing if the file isn't found

    def clear_data(self):
        self.voters.clear()   #This will clear the list of voters
        self.candidates.clear()   #This will clear the list of candidates
        print("Data Cleared.")    #This will print after that data is cleared

def display_admin_menu():   #The Admin's Menu after they login from Main Menu Function
    print("\nAdmin Menu")    #This will print out the title of the Admin Menu using the \n (new line) method
    print("1. Remove a Voter")    #Option to Remove a Voter
    print("2. Search for a Voter")    #Option to Search for a Voter
    print("3. Add a Candidate")     #Option to Add a New Candidate
    print("4. Remove a Candidate")    #Option to Remove a Candidate
    print("5. Election Analysis")    #Option to Perform the Election Analysis
    print("6. View Total Number of Votes")    #Option to View the Total Number of Votes
    print("7. Generate Voter Report")    #Option to Generate and View the Voter Report
    print("8. Generate Candidate Report")    #Option to Generate and View the Candidate Report
    print("9. Election Results")   #Option to View the Election Results and the Winner
    print("10. Check Feedback")    #Option to Check Any Feedback, Voters May Have Left
    print("11. Save Data")    #Option to Save Any Data
    print("12. Clear Data")    #Option to Clear any Saved Data
    print("13. Sign out of the System")   #Option to Sign Out of the System and Takes You Back to the Main Menu

def display_voter_menu():   ##Shows the menu options that the voter's account is able to choose from
    print("\nVoter Menu")
    print("14. Vote for a Candidate")
    print("15. Search All Candidates")
    print("16. View Candidate's Attributes")
    print("17. Modify Vote (Must be Done Before Election Ends)")
    print("18. View Election Status")
    print("19. View Your Voting Status")
    print("20. Provide Feedback to Our System :)")
    print("21. Save Data")
    print("22. Clear Data")
    print("23. Sign out of the System")

def admin_menu(election):   #Handles admin actions within the election system
    while True:
        display_admin_menu()
        choice = input("Enter your choice: ")

        if choice == "1":   #Removes an existing voter
            name = input("Enter Voter Name to Remove: ")
            election.remove_voter(name)
            print("Voter Removed.")

        elif choice == "2":   #Searches for a voter account by name and displays voters matching a query
            query = input("Enter Search for Voters: ")
            results = election.search_voters(query)
            if results:
                print("Search Results: ")
                for voter in results:
                    voter.display()
            else:
                print("No Voters Found.")

        elif choice == "3":   #Add a new candidate, collects the candidates details, creating a candidate object and adds them to the system.
            name = input("Enter Candidate Name: ")
            party = input("Enter Party: ")
            goals = input("Enter Election Goals: ")
            candidate = Candidate(name, party, goals)
            election.add_candidate(candidate)
            print("Candidate Added!")

        elif choice == "4":   #Removes a candidate by name.
            name = input("Enter Candidate Name to Remove: ")
            election.remove_candidate(name)
            print("Candidate Removed.")

        elif choice == "5":   #Calls the Function to Perform Election Analysis
            election.election_analysis()

        elif choice == "6":   #Counts and Displays the total number of votes
            print(f"Total Number of Votes: {election.count_votes()}")

        elif choice == "7":   #Displays details and reports of all voters
            election.generate_voter_report()

        elif choice == "8":   #Displays details for all candidates
            election.generate_candidate_report()

        elif choice == "9":   #Display for election results
            election.election_results()

        elif choice == "10":
            election.view_feedback()

        elif choice == "11":   #Saves the election data to persistent storage
            election.save_data()
            print("Data Saved!")

        elif choice == "12":   #Clears the data from the election system
            election.clear_data()

        elif choice == "13":   #Sign out of the admin menu
            print("Sign out of the Program.")
            return False

        else:
            print("Invalid Option. Pick a Valid Option.")

def voter_menu(election, voter):   #Provides a menu for voter's accounts
    display_voter_menu()
    choice = input("Enter Your Choice: ")

    if choice == "14":  #Voter chooses the candidate to vote for, lists the candidates and records the choice the voter makes
        if not election.candidates:
            print("No Candidates Registered Yet.")
        else:
            print("List of Candidates: ")
            for candidate in election.candidates:
                candidate.display()
            candidate_name = input("What Candidate Would You Like to Vote For: ")
            chosen_candidate = next((c for c in election.candidates if c.name.lower() == candidate_name.lower()), None)
            if chosen_candidate:
                election.vote(voter.voter_ID, chosen_candidate.name)  #Marks Down the Vote
                print("Vote Has Been Marked Down.")
            else:
                print("Invalid Candidate Name.")

    elif choice == "15":  #Displays a list with details of all the candidates
        print("List of all Candidates:")
        for candidate in election.candidates:
            candidate.display()

    elif choice == "16":   #Displays details of a selected candidate
        candidate_name = input("Enter the Name of the Candidate's Attributes You Want to See: ")
        chosen_candidate = next((c for c in election.candidates if c.name.lower() == candidate_name.lower()), None)
        if chosen_candidate:
            chosen_candidate.display()
        else:
            print("Candidate Not Found.")

    elif choice == "17":   #Allows the voter to change who they voted for
        if voter.vote:
            print("Your Current Vote:")
            print(voter.vote)
            new_vote = input("Enter the Name of the New Candidate You Wish To Vote For: ")
            chosen_candidate = next((c for c in election.candidates if c.name.lower() == new_vote.lower()), None)
            if chosen_candidate:
                voter.vote = chosen_candidate.name
                print("Your Vote Has Been Changed.")
            else:
                print("Invalid Candidate.")
        else:
            print("You Haven't Voted Yet.")

    elif choice == "18":    #Displays the election's current state
        print("Election Status: Ongoing")

    elif choice == "19":   #Displays the voter's current vote or indicated the voter if they have not voted
        if voter.vote:
            print("You Have Already Voted.")
            print(voter.vote)
        else:
            print("You Haven't Voted Yet.")

    elif choice == "20":   #Collects and records the voter's feedback
        feedback = input("Enter Any Feedback, You May Have on Our System: ")
        election.leave_feedback(voter.name, voter.voter_ID, feedback)

    elif choice == "21":   #Saves the current election data
        election.save_data()
        print("Data Saved!")

    elif choice == "22":    #Clears all election data
        election.clear_data()

    elif choice == "23":   #Exits the voter menu and takes you back to the main menu
        print("Exiting the System")
        return False

    else:   #Handles invalid inputs and prompts for a valid choice
        print("Invalid Option. Pick a Valid Choice.")

    return True

def main():   #Main function to run the election system application/the Main Menu
    election = Election()
    election.load_data()

    while True:   #Display the main login/signup menu
        print("\nWelcome to Election Login Page")
        print("1. Admin Log In")
        print("2. Admin Sign Up")
        print("3. Voter Log In")
        print("4. Voter Sign Up")
        print("5. Exit System")
        choice = input("Enter Your Choice: ")

        if choice == "1":   #Admin login process
            username = input("Enter Admin Username: ")
            password = input("Enter Admin Password: ")
            if election.login_admin(username, password):
                while admin_menu(election):
                    pass

        elif choice == "2":   #Admin signup process
            username = input("Enter New Admin Username: ")
            password = input("Enter New Admin Password: ")
            key = input("Enter Admin Key To Sign Up: ")
            election.signup_admin(username, password, key)

        elif choice == "3":   #Voter login process
            name = input("Enter Your Name: ")
            voter_ID = input("Enter Your ID: ")
            user = election.login_voter(name, voter_ID)
            if user:
                while voter_menu(election, user):
                    pass

        elif choice == "4":   #Voter signup process
            name = input("Enter Your Name: ")
            voter_ID = input("Enter Your ID: ")
            age = input("Enter Your Age: ")
            election.signup_voter(name, voter_ID, age)

        elif choice == "5":   #Exits the application and it will End using the Break Method
            print("Thanks for Using Our System!.")
            break
        else:
            print("Invalid Choice. Enter A Valid Choice.")

if __name__ == "__main__":
    main()

#Admin Key = WJES