# Q9 – Student Marks Calculation

**Question-paper requirements:** calculate total and average for three subjects; push source to GitHub; build a Docker image; execute Selenium tests.

## A. Console program
```powershell
python marks.py
```
Enter a name and three marks (each from 0 to 100).

## B. GitHub
Create an empty repository, then run the general Git commands from the top-level README in this folder.

## C. Flask app (API for Docker/Selenium)
```powershell
pip install -r requirements.txt
python app.py
```
Test in a browser:
- `http://localhost:5000/`
- `http://localhost:5000/calculate?m1=80&m2=90&m3=70`

Expected result: total `240`, average `80.0`.

## D. Docker
```powershell
docker build -t student-marks .
docker run --rm -p 5000:5000 --name marks-container student-marks
```
Keep this terminal open. Test the URL above in another browser/terminal.

## E. Selenium
With the app/container still running, open a second PowerShell in this folder:
```powershell
pip install -r requirements.txt
python -m unittest test_marks_selenium.py -v
```
Chrome must be installed. Selenium Manager normally manages the matching driver.

Stop the container with Ctrl+C (foreground run), or `docker rm -f marks-container` if it was started detached.
