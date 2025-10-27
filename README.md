# Local Contest — run coding contests on your LAN (no internet, no drama)

**TL;DR:** Local Contest is a lightweight, local-first platform to host coding contests over a shared Wi-Fi/LAN. Organisers can create problems, participants submit solutions via the web UI, and the repo includes a plagiarism-checking helper to detect copy-paste shenanigans. Perfect for hackathons, college contests, and smugly offline vibes.

* * *

## What this is (short & honest)

*   A small Flask-ish web app (inferred) that serves contest pages from `templates/`.
    
*   Uploads (submissions) are saved in `uploads/`.
    
*   `plag.py` is a plagiarism utility that compares submissions and flags suspicious matches.
    
*   Minimal, local-first, easy to run — no cloud required. Great for when you want to host a contest but the internet wants a break.
    

* * *

## Features (smart)

*   Host contests over local network — participants connect to the organiser’s machine.
    
*   Upload and store submissions in `uploads/`.
    
*   Run a plagiarism check across submissions (scripted utility).
    
*   Simple HTML templates for quick customization.
    

## Why you’d use this (witty)

*   Because “everyone open your GitHub” is a terrible game to play with 50 students.
    
*   Because local > latency drama.
    
*   Because you like bragging rights for running a contest that survived a router tantrum.
    

* * *

## Tech stack (inferred)

*   Python 3.8+
    
*   Flask (or a micro web framework)
    
*   Jinja2 templates (in `templates/`)
    
*   Simple file-based storage (`uploads/`)
    
*   A plagiarism helper script (`plag.py`) — can be extended with more advanced comparators (JPlag, MOSS, difflib, Levenshtein, etc.)
    

* * *

## Quick start (assumptions)

> These commands assume a typical Flask-style app structure. Adjust if your code differs.

1.  Clone the repo
    

`git clone https://github.com/utkarshdabral/local_contest.git cd local_contest`

2.  Create & activate a virtualenv
    

`python3 -m venv venv source venv/bin/activate   # macOS / Linux venv\Scripts\activate      # Windows`

3.  Install dependencies (if you have a `requirements.txt` add it; otherwise install likely deps):
    

`pip install flask # optionally: # pip install python-Levenshtein difflib3`

4.  Create uploads folder if not present:
    

`mkdir -p uploads`

5.  Run the web app:
    

`python app.py # or FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000`

6.  Visit on LAN (organiser machine IP): `http://<organiser-ip>:5000`
    

* * *

## Plagiarism utility (what it likely does)

*   `plag.py` scans files in `uploads/` (or given paths) and compares them pairwise, printing similarity scores or flags.
    
*   You can extend it with:
    
    *   Tokenization, identifier renaming normalization
        
    *   Structural comparison (AST)
        
    *   Integrate with JPlag / MOSS for heavy lifting
        

**Run (example)**

`python plag.py uploads/sub1.py uploads/sub2.py # or to run a batch check: python plag.py --dir uploads/`

_(If actual CLI flags differ, I’ll update this once I can read the file.)_

* * *

## Project structure (observed)

`local_contest/ ├─ app.py         # main web app (routes, upload handling) ├─ plag.py        # plagiarism comparison utility ├─ templates/     # HTML templates for UI └─ uploads/       # where user submissions live`
