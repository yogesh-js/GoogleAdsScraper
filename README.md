# Google Ads Scraper
This Python script scrapes Google search results for advertisements and outputs the ad headline, description, and URL to a CSV file. It uses Selenium for web scraping and BeautifulSoup for parsing the HTML.

## Installation
1) Clone this repository.
2) Install Selenium.
3) Download the appropriate version of the ChromeDriver executable for your system and replace the executable_path variable in the Service() function with the path to the downloaded file.

## Usage
1) Create a keywords.csv file containing a list of keywords to search for, with one keyword per line.
2) Run the script by entering python main.py in your terminal.
3) After the script finishes running, a output_data.csv file will be created containing the scraped ad data.

## Contributing
Contributions are welcome! Please open an issue or pull request if you find any bugs or have suggestions for improvements.
