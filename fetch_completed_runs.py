#!/usr/bin/env python3
import requests
import sys

def fetch_activities(auth_token, before_id="*"):
    """Fetch activities from Nike API"""
    url = f"https://api.nike.com/plus/v3/activities/before_id/v3/{before_id}"

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {auth_token}",
        "accept-charset": "utf-8",
        "accept-language": "en-IN;q=1.0",
        "user-agent": "NRC/7.71.0 (prod; 2509221646; iPadOS 18.5; iPad13,18)"
    }

    params = {
        "limit": 30,
        "types": "jogging,run",
        "include_deleted": "false"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_completed_guided_runs(auth_token):
    """Fetch all completed guided runs"""
    completed_runs = []
    before_id = "*"

    while True:
        print(f"Fetching activities (before_id: {before_id})...", file=sys.stderr)

        data = fetch_activities(auth_token, before_id)
        activities = data.get("activities", [])

        if not activities:
            break

        for activity in activities:
            # Check if it's a guided run
            tags = activity.get("tags", {})
            guided_run_id = tags.get("com.nike.running.audioguidedrun")

            if guided_run_id:
                run_name = tags.get("com.nike.name", "Unknown")
                completed_runs.append({
                    "id": guided_run_id,
                    "name": run_name,
                    "activity_id": activity.get("id"),
                    "start_time": activity.get("start_epoch_ms")
                })

        # Check if there are more pages
        paging = data.get("paging", {})
        before_id = paging.get("before_id")

        if not before_id:
            break

    return completed_runs

def main():
    # Get auth token from command line args or prompt
    if len(sys.argv) > 1:
        auth_token = sys.argv[1]
    else:
        auth_token = input("Enter authorization token: ").strip()

    if not auth_token:
        print("Error: Authorization token is required", file=sys.stderr)
        sys.exit(1)

    try:
        completed_runs = get_completed_guided_runs(auth_token)

        print(f"\nFound {len(completed_runs)} completed guided runs:\n")

        for run in completed_runs:
            print(f"{run['id']}")

        print("\nCan paste above list as in the app to mark them as completed.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching activities: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
