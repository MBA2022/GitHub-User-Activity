import sys
import requests

def fetch_github_activity(username):
    """Fetch recent activity of a GitHub user."""
    api_url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub: {e}")
        sys.exit(1)

def parse_activity(events):
    """Parse GitHub events into a readable format."""
    parsed_events = []

    for event in events:
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        
        if event_type == "PushEvent":
            commit_count = len(event["payload"]["commits"])
            parsed_events.append(f"Pushed {commit_count} commits to {repo_name}")
        elif event_type == "IssuesEvent":
            action = event["payload"]["action"]
            parsed_events.append(f"{action.capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            parsed_events.append(f"Starred {repo_name}")
        else:
            parsed_events.append(f"{event_type} in {repo_name}")

    return parsed_events

def display_activity(username, activities):
    """Display the user's activity in the terminal."""
    print(f"Recent activity for GitHub user '{username}':")
    for activity in activities:
        print(f"- {activity}")

def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    events = fetch_github_activity(username)

    if events:
        activities = parse_activity(events)
        display_activity(username, activities)

if __name__ == "__main__":
    main()
