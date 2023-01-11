from selenium import webdriver
import hashlib

driver = webdriver.Firefox()

driver.get("https://coderbyte.com/")
driver.close()
# create a sha1 hash object
hash_object = hashlib.new("sha1", "https://coderbyte.com/".encode())
print(hash_object)