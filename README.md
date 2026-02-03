# NRC Guided Runs Tracker

A web-based tracker for Nike Run Club guided runs, hosted on GitHub Pages.

## Features

### Browse & Search
- Shows all NRC guided runs with images and details
- Search by run name or ID
- Sort by time (duration-based runs) or distance (distance-based runs)
- When sorting by time, only duration-based runs are shown (and vice versa)

### Track Progress
- Mark runs as completed or saved
- Filter runs by status:
  - Completed runs
  - Not completed runs
  - Saved runs
  - Not saved runs
- Filters use OR logic for flexible combinations
- All data stored in browser localStorage (no backend)

### Bulk Operations
- Bulk import completed runs by pasting run IDs
- Automatically handles old run IDs via `previousId` and `previousIds` mapping
- Python script available to fetch your completed runs from Nike's API

### Run Details
- Click any run card to view detailed information
- See overview, run details, and coach information
- Open runs directly in the Nike Run Club app (mobile only on card, always in modal)

### AI Recommendations
- "Ask ChatGPT" feature to get personalized run suggestions
- Sends your completed runs and available runs to ChatGPT
- Get 3-5 recommended runs based on your progression

### Responsive Design
- Mobile-optimized with smaller card images
- Touch-friendly interface
- All features work on mobile and desktop

## Getting Your Completed Runs

Use the included Python script to fetch your completed guided runs from Nike's API:

### How to get the auth token
1. Login to https://www.nike.com/
2. Open developer tools
3. Copy the `authorization` header (Bearer eyJXXX) from any API call to api.nike.com

### Run the script
```bash
python fetch_completed_runs.py "YOUR_AUTH_TOKEN"
```

The script will output a list of run IDs that you can paste into the bulk import feature.

## Tech Stack
- Pure HTML/CSS/JavaScript
- No build process or dependencies
- Client-side only (except for fetching run data)
- GitHub Pages hosting

## Links
- [Live Demo](https://snlagr.github.io/nrc-tracker/)
- [GitHub Repository](https://github.com/snlagr/nrc-tracker)
- [Python Script](https://github.com/snlagr/nrc-tracker/blob/main/fetch_completed_runs.py)