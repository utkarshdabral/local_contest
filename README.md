#   

# Local Contest

# 

**Runing coding contests locally**

* * *

## What is this?

# 

**Local Contest** is a lightweight platform to **host coding competitions over a shared LAN/Wi-Fi network**.  
Organisers can create problems, participants submit code, and a built-in plagiarism checker ensures fair play.

It’s perfect for **college events, hackathons, or LAN-based coding battles** when Wi-Fi betrays you .

* * *

## Features

# 

*   **Local hosting:** Runs completely offline — participants connect via the same Wi-Fi/LAN.
    
*   **Simple UI:** Clean and minimal HTML templates for easy use.
    
*   **File uploads:** Participants can submit their solutions directly.
    
*   **Plagiarism check:** Detects code similarity using `plag.py`.
    
*   **Lightweight & Fast:** No heavy dependencies or database needed.
    

* * *

## Tech Stack

# 

*   **Backend:** Python (Flask)
    
*   **Frontend:** HTML, CSS (templates-based)
    
*   **Storage:** Local file system (`uploads/` folder)
    
*   **Utility:** Custom plagiarism checker (`plag.py`)
    

* * *

## Project Structure

# 

`local_contest/ ├── app.py           # Main web app (routes, uploads, and serving pages) ├── plag.py          # Code similarity checker ├── templates/       # HTML templates (organiser, participant, results) └── uploads/         # Submissions folder`

* * *

## How It Works

# 

1.  The organiser runs `app.py` on their machine.
    
2.  Participants connect using the organiser’s local IP (e.g., `192.168.x.x:5000`).
    
3.  They submit their code via the web interface.
    
4.  The organiser runs `plag.py` to check for suspiciously similar submissions.
    
5.    
    

* * *

## Setup & Usage

# 

`# Clone the repo git clone https://github.com/utkarshdabral/local_contest.git cd local_contest  # Create a virtual environment python -m venv venv source venv/bin/activate  # (Windows: venv\Scripts\activate)  # Install dependencies pip install flask  # Run the app python app.py`

Now open your browser and visit →  
👉 `http://localhost:5000` _(for organiser)_  
👉 `http://<your-local-ip>:5000` _(for participants)_

* * *

## Plagiarism Check

# 

To compare submissions in the `uploads/` folder:

`python plag.py`

It will detect and report similarity between files, saving you from copy-paste crimes.
