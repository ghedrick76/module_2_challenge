# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# function for creating a CSV file of the qualifying loans, using the list
# of qualifying loans as an argument.
def save_csv(qualifying_loans):
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
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
        for loan in qualifying_loans:
            csv_writer.writerow(loan)
       