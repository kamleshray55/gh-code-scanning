import truffleHog.truffleHog as truffleHog

def main():
    rules = [
        {
            "regex": "^ssh-rsa [A-Za-z0-9+/]+[=]{0,3} [A-Za-z0-9+/]+[=]{0,3} .*$",
            "description": "SSH Public Key"
        }
    ]
    truffleHog.scan(".", regex=True, custom_rules=rules)

if __name__ == "__main__":
    main()
