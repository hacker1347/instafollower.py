import requests

# Function to get the followers of a given account
def get_followers(username):
    url = f"https://api.instagram.com/v1/users/{username}/media/recent/?access_token=ACCESS_TOKEN"
    response = requests.get(url)
    data = response.json()
    
    return data['items']

# Function to generate a link for the follower tool
def generate_follower_link(username, followers):
    return f"[Click Here to Support {username}!]({username})"

# Main function
if __name__ == "__main__":
    username = input("Enter the username of the account you want to gain followers for: ")
    followers = get_followers(username)
    
    print(generate_follower_link(username, followers))
