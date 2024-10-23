# **Bag Tag Payment Confirmation Script**

## **Overview**

This Python script automates the confirmation of payments for bag tags in a band organization. It compares data between two CSV files: one containing the list of members who have bag tags and another with transaction records. The script then checks if the members have paid for their bag tags and updates the payment status in the bag tag CSV file.
Features

CSV Comparison: Reads member names from both CSV files and cross-references them to verify payments.
Automated Status Update: Updates the payment status in the bag tag CSV file by marking paid members as True.
Case-insensitive Matching: Ensures member names are matched without regard to letter case.

## File Structure

The script expects two CSV files:
* tags.csv: Contains a list of members who have been issued bag tags. The member name should be in the second column.

* transactions.csv: Contains a list of transactions. The member name should be in the second column.

## Features
* CSV Comparison: Reads member names from both CSV files and cross-references them to verify payments.
  
* Automated Status Update: Updates the payment status in the bag tag CSV file by marking paid members as True.
  
* Case-insensitive Matching: Ensures member names are matched without regard to letter case.

## Requirements

* Python 3.x

* CSV Files: Ensure the correct format and column placement for names in both files.

## Installation

1. Clone the repository

```bash
git clone https://github.com/YourUsername/YourRepository.git
```
2. Prepare your CSV files: Ensure you have two CSV files: **tags.csv**  and **transactions.csv** Place them in the same directory as the script.

## Usage
1. Run the script:

```bash
python bag_tag_payment_confirmation.py
```
2. The script will
   * Read the names from tags.csv and transactions.csv
   * Cross-reference the names to determine who has paid
   * Update the 6th column of tags.csv (payment status) to True for members who have paid

3. **Check the Output:** After running, the tags.csv file will be updated with the payment status

## Customization

If the name is located in a different column or the payment status should be in a different column, you can modify the script by adjusting the column indices (e.g., row[1] for names and row[5] for payment status).

