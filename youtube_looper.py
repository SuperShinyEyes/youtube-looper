#!/usr/bin/env python3
from selenium import webdriver
import time
import sys

# Example url: "https://www.youtube.com/watch?v=UE4uHtZPmAc"

class YouTubeItem():
    def __init__(self, url, button_selector):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        self.play_button = self.driver.find_element_by_css_selector(button_selector)
        self.title = self.driver.find_element_by_id("eow-title").get_attribute("title")

    def is_playing(self):
        return self.play_button.get_attribute("aria-label") == "Pause"

    def play(self):
        self.play_button.click()

    def terminate(self):
        self.driver.close()

    def repeat(self):
        repeat_num = 1
        while True:
            print("--- Song repeat# %d. Listening to %s"%(repeat_num, self.title))
            while self.is_playing():
                time.sleep(1)
            self.play()
            repeat_num += 1



if __name__=="__main__":
    if len(sys.argv) == 1:
        url = "https://www.youtube.com/watch?v=UE4uHtZPmAc"
    else:
        url = sys.argv[1]
        print("Get url from command line\n%s"%url)

    try:
        song = YouTubeItem(url, ".ytp-play-button")
        song.repeat()

    except KeyboardInterrupt:
        print("Ctrl-C clicked!\nBye!")

    finally:
        song.terminate()
