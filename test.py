import yaml

with open("configuration.yaml", "r") as file:
    config = yaml.safe_load(file)

print(config["INPUT_PATH"])