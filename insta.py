import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Your Instagram credentials
USERNAME = ''  # Change this to your Instagram username
PASSWORD = ''  # Change this to your Instagram password

def print_logo(message):
    logo = """
██████╗ ███████╗██████╗  ██████╗                 
██╔══██╗██╔════╝██╔══██╗██╔═══██╗                
██████╔╝█████╗  ██████╔╝██║   ██║                
██╔══██╗██╔══╝  ██╔══██╗██║   ██║                
██████╔╝███████╗██████╔╝╚██████╔╝                
╚═════╝ ╚══════╝╚═════╝  ╚═════╝                 
"""
    print("\033[91m" + logo + "\033[0m")  # Red color for logo
    print("\033[92m" + message + "\033[0m")  # Green color for message

def init_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-extensions")
    
    # Use the correct path to ChromeDriver
    service = Service('/usr/bin/chromedriver')  # Adjust this path as necessary
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login_to_instagram(driver):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)

    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    
    time.sleep(5)
    print_logo("Successfully logged in.")

def fetch_usernames():
    # Replace this list with actual usernames or randomize as needed
    return ['user1', 'user2', 'user3', 'user4', 'user5']

def is_real_user(driver, username):
    try:
        driver.get(f'https://www.instagram.com/{username}/')
        time.sleep(3)

        follower_count = driver.find_element(By.XPATH, '//a[contains(@href, "/followers")]/span').text
        # You can add more criteria to check if the user is real based on follower count
        if int(follower_count.replace(',', '')) > 10:  # Example criteria
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking user {username}: {e}")
        return False

def main():
    print_logo("Starting Instagram Automation...")
    
    driver = init_driver()
    login_to_instagram(driver)
    
    usernames = fetch_usernames()
    selected_users = random.sample(usernames, k=min(3, len(usernames)))  # Random selection of 3 users
    
    print_logo(f"Selected users: {selected_users}")
    
    for username in selected_users:
        if is_real_user(driver, username):
            print_logo(f"{username} is a real user.")
            # You can add liking/following functionality here
        else:
            print_logo(f"{username} is not a real user based on the criteria.")

    driver.quit()

if __name__ == "__main__":
    main()