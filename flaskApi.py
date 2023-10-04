from flask import Flask, jsonify
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from gtts import gTTS
import os


app = Flask(__name__)

# Sample array data
sample_array = [1, 2, 3, 4, 5]


def text_to_speech(text, language='es'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language)

    # Save the audio file
    tts.save('output.mp3')

    # Play the audio file (optional)
    os.system('mpg123 output.mp3')  # You need 'mpg123' or any other audio player installed

@app.route('/datos', methods=['GET'])
def get_datos():

    


    # spanish_text = "¡Hola! Esto es una prueba de texto a voz en español."
    # text_to_speech(spanish_text)

    chrome_options = Options()


    chrome_options.add_argument('--headless')  # Run in headless mode


    # URL of the website you want to visit
    url = 'https://twitter.com'

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)



    #driver = webdriver.Chrome()

    try:
        # Navigate to the URL
        driver.get(url)
        time.sleep(1)
        # XPath of the button
        button_xpath = '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div'

        button = driver.find_element(By.XPATH, button_xpath)



        # Click the button
        button.click()
        # Optional: Wait for 5 seconds to simulate a pause
        time.sleep(2)

        button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div'

        button = driver.find_element(By.XPATH, button_xpath)



        # Click the button
        button.click()
        # Optional: Wait for 5 seconds to simulate a pause
        time.sleep(2)

        

        usuarioInputXpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'

        usuarioInput = driver.find_element(By.XPATH, usuarioInputXpath)

        usuarioInput.click()
        # Click the button
        
        time.sleep(1)

        usuarioInput.send_keys("digital34web")

        time.sleep(1)

        btnXpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'

        btnContinuar = driver.find_element(By.XPATH, btnXpath)

        btnContinuar.click()

        time.sleep(1)

        
        
        psswdInputXpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'

        passwdInput = driver.find_element(By.XPATH, psswdInputXpath)

        passwdInput.click()

        time.sleep(1)

        passwdInput.send_keys("meqWyv-siqnun-suxko2")
        time.sleep(1)

    

        btnContinuarXpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'

        btnContinuar = driver.find_element(By.XPATH, btnContinuarXpath)

        btnContinuar.click()
        # Continue with other actions on the webpage

        time.sleep(1)

        driver.get("https://twitter.com/AlertaNews24")
        time.sleep(5)  
        driver.execute_script('window.scrollBy(0, 1200);')
    
        time.sleep(5)


    
        posts = []

        for x in range(13):

            # Print the content of each tweet article
            tweet_articles_xpath = '//article[@data-testid="tweet"]//div[@data-testid="tweetText"]//span'

            # Find all article elements with data-testid="tweet"
            tweet_articles = driver.find_elements(By.XPATH, tweet_articles_xpath)

            for i, article in enumerate(tweet_articles):
            
                textArticle = article.text
                textArticle.replace(" ", "")
                # print(article.text)  # Print the text content of the article

                if textArticle.startswith(' | ') == True:
                    if not article.text in posts:
                        posts.append(article.text)
                        
            
                
                # Check if this is the last iteration
                if i == len(tweet_articles) - 1:
                    print("This is the last tweet article.")    
            driver.execute_script('window.scrollBy(0, 1200);')
            time.sleep(2)

        print(posts)

        for post in posts:
            print(post)
            print()
        print(len(posts))
    
    finally:
        # Close the browser
        driver.quit()

    # Convert the array to JSON format
    return jsonify({'data': posts})

if __name__ == '__main__':
    app.run(debug=False)