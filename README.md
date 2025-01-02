# GitHub Activity CLI

## Overview
This is a simple Command Line Interface (CLI) application that fetches and displays the recent activity of a GitHub user. It provides insights into actions like commits, issues, and starred repositories by interacting with the GitHub API.

## Features
- Fetches recent activity of a GitHub user.
- Supports event types such as commits, issues, and stars.
- Displays a user-friendly list of activities in the terminal.
- Handles errors gracefully, such as invalid usernames or network issues.

## Prerequisites
- Python 3.6 or higher.
- `requests` library (Install it using `pip install requests`).

## Usage
1. Clone the repository or save the script.
2. Run the script from the terminal with the following command:

   ```bash
   python github_activity.py <username>
   ```

   Replace `<username>` with the GitHub username you want to query.

## Example
### Command:
```bash
python github_activity.py kamranahmedse
```

### Output:
```plaintext
Recent activity for GitHub user 'kamranahmedse':
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened an issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
```

## Code Explanation
1. **Fetch GitHub Activity**:
   - The `fetch_github_activity` function retrieves the user’s recent events from the GitHub API.

2. **Parse Events**:
   - The `parse_activity` function processes the JSON data and extracts meaningful activity descriptions.

3. **Display Activity**:
   - The `display_activity` function formats and outputs the activity in a readable format.

4. **Main Function**:
   - Handles the CLI arguments, fetches data, and displays results.

## Error Handling
- If an invalid username is provided or there is a network issue, the script exits with an error message.

## Dependencies
- Python 3.6+
- Requests library: Install it with:
  ```bash
  pip install requests
  ```

## Project URL
You can access the repository at [GitHub Activity CLI Repository](https://github.com/MBA2022/GitHub-User-Activity.git).


## License
This project is open-source and available under the MIT License.
