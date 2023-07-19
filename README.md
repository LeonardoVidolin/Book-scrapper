

README - Web Scraping Books from "books.toscrape.com" using Python
This Python script allows you to scrape book data from the website "books.toscrape.com" using the BeautifulSoup library. The script extracts information such as book titles, categories, ratings, prices, and availability from multiple pages and saves the data into a CSV file.

Installation
To run this script, make sure you have Python installed on your system. Additionally, install the required libraries using the following commands:

bash
Copy code
pip install selenium
pip install requests
Usage
Clone or download the Python script to your local machine.

Open the terminal or command prompt and navigate to the directory containing the script.

Run the script using the following command:

bash
Copy code
python script_name.py
Replace script_name.py with the actual name of the Python script file.

The script will start scraping data from the website "books.toscrape.com." It will fetch information about books, including title, category, rating, price, and availability.

The script will display the extracted information on the console as it progresses. The total time taken for extraction will also be shown.

The script will save the scraped data into a CSV file named "books_scraped.csv" in the specified directory.

Note: Ensure that you have an internet connection while running the script, as it requires making HTTP requests to fetch book data.

Output
The CSV file "books_scraped.csv" will contain the following columns:

Title: The title of the book.
Category: The category or genre of the book.
Rating: The star rating of the book.
Price: The price of the book.
Availability: The availability status of the book.
Disclaimer
This script is intended for educational purposes and to demonstrate web scraping techniques using BeautifulSoup and Python. Make sure to review the website's terms of service and legal policies before scraping data from any website. Scraping websites without permission may violate the website's terms of service and could potentially lead to legal consequences.

Use this script responsibly and at your own risk.

If you encounter any issues or have suggestions for improvement, feel free to reach out or contribute to the project.

Happy web scraping!
