# Mini Project 8: Voting System
# Count votes for candidates.


# Voting System

votes = {}

def add_candidate():
    name = input("Enter Candidate Name: ")
    votes[name] = 0
    print("Candidate Added")


def cast_vote():
    name = input("Enter Candidate name to vote: ")
    if name in votes:
        votes[name] += 1
        print("Vote Added")
    else:
        print("Candidate Not Found")


def show_winner():
    if len(votes) == 0:
        print("No Candidate")
    else:
        winner = max(votes, key=votes.get)
        print("Winner:", winner, "-", votes[winner], "votes")


# Menu
while True:
    print("\n1.Add Candidate 2.Vote 3.Show Winner 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_candidate()
    elif choice == "2":
        cast_vote()
    elif choice == "3":
        show_winner()
    elif choice == "4":
        break
    else:
        print("Invalid Choice")