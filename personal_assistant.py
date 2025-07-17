
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import random
import time

# News Scraper
def get_top_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = []
    for item in soup.find_all('h3'):
        headline = item.get_text()
        if headline:
            headlines.append(headline)

    return headlines[:10]  # Return top 10 headlines

# Weather Simulation
def generate_weather_data(city):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    temperatures = [random.randint(15, 30) for _ in range(7)]  # Random temperatures between 15°C and 30°C

    return days, temperatures

def visualize_weather(city, days, temperatures):
    plt.plot(days, temperatures, marker='o')
    plt.title(f"Weather Forecast for {city}")
    plt.xlabel("Days of the Week")
    plt.ylabel("Temperature (°C)")
    plt.show()

# Stock Simulation
def generate_stock_data(symbol):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    prices = [random.randint(100, 500) for _ in range(5)]  # Random stock prices between 100 and 500

    return days, prices

def visualize_stock(symbol, days, prices):
    plt.plot(days, prices, marker='x', color='r')
    plt.title(f"Stock Price for {symbol}")
    plt.xlabel("Days of the Week")
    plt.ylabel("Stock Price (USD)")
    plt.show()

# Recommendation Engine
def recommend_tasks(interests):
    tasks = {
        "fitness": "Go for a run",
        "coding": "Work on your Python project",
        "reading": "Read a book on Machine Learning",
        "music": "Listen to a new album"
    }

    recommendations = []
    for interest in interests:
        if interest in tasks:
            recommendations.append(tasks[interest])

    return recommendations

# Personal Assistant
def personal_assistant():
    print("Welcome to your Personal Assistant!
")

    # News Section
    print("Fetching top news headlines...")
    news = get_top_news()
    print("Top News Headlines:")
    for i, headline in enumerate(news, 1):
        print(f"{i}. {headline}")

    # Weather Section
    city = input("
Enter your city for the weather forecast: ")
    print(f"Fetching weather data for {city}...")
    days, temperatures = generate_weather_data(city)
    visualize_weather(city, days, temperatures)

    # Stock Section
    stock_symbol = input("
Enter a stock symbol for market data: ")
    print(f"Fetching stock data for {stock_symbol}...")
    stock_days, stock_prices = generate_stock_data(stock_symbol)
    visualize_stock(stock_symbol, stock_days, stock_prices)

    # Recommendation Section
    interests = input("
Enter your interests (comma-separated): ").split(",")
    recommended_tasks = recommend_tasks([interest.strip() for interest in interests])
    print("
Recommended Tasks:")
    for task in recommended_tasks:
        print(f"- {task}")

    print("
Have a great day!")
    time.sleep(2)

if __name__ == "__main__":
    personal_assistant()
