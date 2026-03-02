#!/usr/bin/env python3
"""
Screenshot tool for Periodic Table
Requires: pip install selenium pillow

Usage: python3 take-screenshots.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PIL import Image
import os
import time

# Create screenshots directory
os.makedirs('screenshots', exist_ok=True)

# Use headless Chrome with webdriver-manager
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--force-device-scale-factor=1')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure you have: pip install selenium webdriver-manager pillow")
    exit(1)

url = "https://helmutqualtinger.github.io/PeriodicTable/"

try:
    # Dark Mode Screenshot
    print("📸 Taking Dark Mode screenshot...")
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "element"))
    )
    time.sleep(1)

    # Make sure dark theme is active
    driver.execute_script("document.body.classList.remove('light-theme'); localStorage.setItem('theme', 'dark');")
    time.sleep(1)

    driver.save_screenshot('screenshots/periodic-table-dark.png')
    print("✅ Dark Mode screenshot saved!")

    # Light Mode Screenshot
    print("📸 Taking Light Mode screenshot...")
    driver.execute_script("document.body.classList.add('light-theme'); localStorage.setItem('theme', 'light');")
    time.sleep(1)

    driver.save_screenshot('screenshots/periodic-table-light.png')
    print("✅ Light Mode screenshot saved!")

    print("\n✨ Screenshots created successfully!")
    print("   - screenshots/periodic-table-dark.png")
    print("   - screenshots/periodic-table-light.png")

finally:
    driver.quit()
