from configparser import ConfigParser
config = ConfigParser()
config.read("settings.ini")

print("logging_on: ", config["Log"]["logging_on"])
