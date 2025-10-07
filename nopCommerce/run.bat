

@echo off
call /venv/scripts/activate
pytest -s -v -m "smoke" --html .\reports\test_report.html 
pause