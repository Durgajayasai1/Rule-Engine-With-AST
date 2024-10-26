# Rule Engine with Django and AST
This project implements a 3-tier rule engine application using Django, SQLite, and HTML/CSS/JS. It allows the creation, combination, and evaluation of rules based on Abstract Syntax Trees (ASTs).

## Setup
### 1. Install the required dependencies:
```
pip install django

```
### 2. Apply migrations and run the Django server:
```
python manage.py migrate
python manage.py runserver
```
## Application Overview
The rule engine consists of two main components:
1. <b>Backend (Django):</b> Handles rule creation, combination, evaluation, and modification using Django models, views, and REST API.
2. <b>Frontend (HTML/CSS):</b> Provides a user interface for creating, combining, evaluating, and modifying rules.

## How to Use the Application
### App Components
1. <b>Create Rule:</b> Enter a rule in the input box `(e.g., age > 30 AND department = 'Sales')`. This will create a rule and return its ID.
2. <b>Combine Rules:</b> Provide rule IDs (comma-separated) to combine them into a "mega" rule, which will receive a new ID.
3. <b>Evaluate Rule:</b> Enter the ID of a "mega" rule and provide the data for evaluation in JSON format.
4. <b>Modify Rule:</b> Modify an existing rule by providing its ID and the new rule string.
5. <b>All Rules Page:</b> A page that displays all created rules with their IDs, rule strings, and corresponding ASTs.
   
### Frontend Pages
1. <b>Main Page:</b> Displays buttons for each action (create rule, combine rules, evaluate rule, modify rule, view all rules).
2. <b>Create Rule Page:</b> Form to create a new rule.
3. <b>Combine Rules Page:</b> Form to combine existing rules by their IDs.
4. <b>Evaluate Rule Page:</b> Form to evaluate a rule by providing its ID and the data in JSON format.
5. <b>Modify Rule Page:</b> Form to modify an existing rule by providing the rule ID and the new rule string.
6. <b>All Rules Page:</b> Displays a list of all the rules created, showing their IDs, rule strings.

## Summary
This README offers comprehensive instructions for setting up and running the Rule Engine application. 
Adhering to these guidelines will ensure the application operates as intended.

## Live Demo

Check out the live demo of the Rule Engine with AST: [Rule Engine with AST Live](https://rule-engine-with-ast-oozu.onrender.com)


