# main.py

import sys

def main(environment):
    if environment == 'prod':
        # Main logic for production environment
        print("PROD : titans rtm data api batch started ...")
    elif environment == 'stg':
        # Main logic for staging environment
        print("STG : batch started ...")
    else:
        # Default to development environment
        print("DEV : batch started ...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        env = sys.argv[1]
    else:
        env = 'dev'

    main(env)
