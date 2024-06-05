import json

with open("D:\solocoding\python studi\songlocked\cipher.json") as file:
    print(len(json.load(file)["list"]))