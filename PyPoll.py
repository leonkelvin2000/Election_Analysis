# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filen ame variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. The total number of votes cast.
total_votes = 0
# Candidate options 
candidate_options = []
# Declare empty dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print in the header row.
    headers = next(file_reader)


    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the condidate name from each row
        candidate_name = row[2]
    
        # Add the candidate name to the candidate list.

        if candidate_name not in candidate_options:

            # Add it to the list of candidate
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add  a vote to that condidate's couant
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine winning vote count and candidate
    # Winning Candidate with Winning Count Tracker
    winning_candidate = " "
    winning_count = 0
    winning_percentage = 0

    # 3. The percentage of votes each candidate won

    for candidate_name in candidate_votes:
        # Retreive vote count of a candidate
        votes = candidate_votes[candidate_name]
        
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. The total number of votes each candidate 

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # 5. The winner of the election based on popular vote.
        
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percen t = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        
            winning_candidate_summary = (
                f"--------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"WInning Percentage: {winning_percentage:.1f}%\n"
                f"--------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)





