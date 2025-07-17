# AI-Assitant


# Personal Assistant Project

This is a simple command-line personal assistant built with Python. It provides weather forecasts, stock market data, news headlines, and personalized task recommendations. The project demonstrates web scraping, synthetic data generation, and data visualization.

## Features

1. **News Scraping:** Fetches the latest news headlines from BBC.
2. **Weather Simulation:** Simulates weather data for a specific city.
3. **Stock Simulation:** Generates and visualizes synthetic stock data.
4. **Task Recommendation:** Suggests tasks based on user interests.
5. **Data Visualization:** Displays weather and stock trends using `matplotlib`.

## Prerequisites

To run this project, you will need to install the following Python libraries:

- `beautifulsoup4` for web scraping
- `requests` for making HTTP requests
- `matplotlib` for data visualization

You can install these libraries using pip:

```bash
pip install beautifulsoup4 requests matplotlib
```

## Running the Project

1. Clone or download the project files.
2. Ensure you have the necessary libraries installed.
3. Run the `personal_assistant.py` script:

```bash
python personal_assistant.py
```

The assistant will:
- Fetch the latest news headlines.
- Simulate weather data for a city of your choice.
- Generate synthetic stock market data for a stock symbol of your choice.
- Provide personalized task recommendations based on your interests.

## Example Usage

```
Welcome to your Personal Assistant!

Fetching top news headlines...
Top News Headlines:
1. Headline 1
2. Headline 2
...

Enter your city for the weather forecast: London
Fetching weather data for London...

Enter a stock symbol for market data: AAPL
Fetching stock data for AAPL...

Enter your interests (comma-separated): fitness, coding
Recommended Tasks:
- Go for a run
- Work on your Python project

Have a wonderful day!


## License

This project is open-source and available under the MIT License.
