# Tinder Bot Automation 🤖❤️

This project automates the process of logging into Tinder using Google credentials and simulates liking profiles. It uses Selenium WebDriver for browser automation.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium package

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/tinder-bot-automation.git
    cd tinder-bot-automation
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv .venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install selenium
    ```

5. **Download ChromeDriver:**

    - Ensure you have the ChromeDriver that matches your version of Google Chrome.
    - Download from: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
    - Place the `chromedriver` executable in a directory included in your system's PATH, or specify the path directly in the script:
      ```python
      search_engine = webdriver.Chrome(executable_path='/path/to/chromedriver', options=chrome_options)
      ```

## Configuration

Replace the placeholders for email and password in the script with your Google credentials:

```python
WebDriverWait(search_engine, 10).until(
    EC.visibility_of_element_located((By.ID, "identifierId"))
).send_keys("your_email@example.com", Keys.ENTER)

WebDriverWait(search_engine, 10).until(
    EC.visibility_of_element_located((By.NAME, 'Passwd'))
).send_keys("your_password", Keys.ENTER
