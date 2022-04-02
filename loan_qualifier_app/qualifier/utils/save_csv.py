import csv

# function for creating a CSV file of the qualifying loans, using the list
# of qualifying loans as an argument.
def save_csv(qualifying_loans):
    header = ["Qualifying Loans"]
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    # chooses the file to write the new information to
    with open('/Users/grayson/Documents/Challenges/module_2_challenge/loan_qualifier_app/data/qualified_loans.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header)
        csv_writer.writerow(qualifying_loans)
