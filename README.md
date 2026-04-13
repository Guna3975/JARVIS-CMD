# JARVIS-CMD

# app/core/jwt_handler.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        return {"user_id": int(user_id)}
    except JWTError:
        raise credentials_exception
    except Exception:
        raise credentials_exception

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 🔹 Dummy Student Data
data = {
    "attendance": [80, 60, 90, 50, 70, 85, 40, 95],
    "study_hours": [2, 1, 4, 1, 3, 4, 1, 5],
    "internal_marks": [75, 50, 85, 40, 65, 80, 35, 90],
    "result": [1, 0, 1, 0, 1, 1, 0, 1]  # 1 = pass, 0 = fail
}

df = pd.DataFrame(data)

X = df[["attendance", "study_hours", "internal_marks"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 🔹 Start MLflow
mlflow.start_run()

# 🔹 Model
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

# 🔹 Prediction
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# 🔹 Log everything
mlflow.log_param("model_type", "DecisionTree")
mlflow.log_param("max_depth", 3)
mlflow.log_metric("accuracy", accuracy)

# 🔹 Save model
mlflow.sklearn.log_model(model, "student_model")

mlflow.end_run()

print("Done! Accuracy:", accuracy)

<!DOCTYPE html>
<html>
<head>
    <title>Simple Login</title>
</head>
<body>

    <h2>Login Page</h2>

    <label>Username:</label>
    <input type="text" id="username"><br><br>

    <label>Password:</label>
    <input type="password" id="password"><br><br>

    <button onclick="login()">Login</button>

    <h3 id="result"></h3>

    <script>
        function login() {
            let user = document.getElementById("username").value;
            let pass = document.getElementById("password").value;

            // Hardcoded credentials
            let correctUser = "admin";
            let correctPass = "1234";

            if (user === "" || pass === "") {
                document.getElementById("result").innerHTML = "Enter all fields";
                return;
            }

            if (user === correctUser && pass === correctPass) {
                document.getElementById("result").innerHTML = "Login Successful";
            } else {
                document.getElementById("result").innerHTML = "Invalid Credentials";
            }
        }
    </script>

</body>
</html>

<!DOCTYPE html>
<html>
<head>
    <title>Percentage Calculator</title>
</head>
<body>

    <h2>Percentage Calculator</h2>

    <label>Marks Obtained:</label>
    <input type="number" id="marks"><br><br>

    <label>Total Marks:</label>
    <input type="number" id="total"><br><br>

    <button onclick="calculate()">Calculate</button>

    <h3 id="result"></h3>

    <script>
        function calculate() {
            let marks = document.getElementById("marks").value;
            let total = document.getElementById("total").value;

            if (marks === "" || total === "") {
                document.getElementById("result").innerHTML = "Please enter values";
                return;
            }

            let percentage = (marks / total) * 100;

            document.getElementById("result").innerHTML =
                "Percentage: " + percentage.toFixed(2) + "%";
        }
    </script>

</body>
</html>

stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Build stage running"

test-job:
  stage: test
  script:
    - echo "Test stage running"

deploy-job:
  stage: deploy
  script:
    - echo "Deploy stage running"


# MLFLOW EXPERIMENT TRACKING
# =====================================================

# -------------------------------
# STEP 1: INSTALL REQUIRED TOOLS
# -------------------------------
pip install mlflow scikit-learn numpy


# -------------------------------
# STEP 2: CREATE PYTHON FILE
# -------------------------------
# File name: mlflow_demo.py

import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Start MLflow Run
with mlflow.start_run():

    # Create Model
    model = LinearRegression()

    # Train Model
    model.fit(X, y)

    # Predictions
    predictions = model.predict(X)

    # Calculate Error (MSE)
    error = np.mean((predictions - y) ** 2)

    # Log Parameters
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_param("data_size", len(X))

    # Log Metrics
    mlflow.log_metric("mse", error)

    # Log Model
    mlflow.sklearn.log_model(model, "model")

print("Run Completed Successfully")


# -------------------------------
# STEP 3: RUN THE SCRIPT
# -------------------------------
python mlflow_demo.py


# -------------------------------
# STEP 4: START MLFLOW UI
# -------------------------------
mlflow ui

# Open browser:
# http://127.0.0.1:5000


# -------------------------------
# STEP 5: VERIFY OUTPUT
# -------------------------------
# In MLflow UI:
# - Check experiment runs
# - View parameters (model_type, data_size)
# - View metric (mse)
# - Compare multiple runs


# -------------------------------
# STEP 6: RUN MULTIPLE TIMES
# -------------------------------
# Modify code slightly or run again
# This creates multiple experiment runs


# -------------------------------
# STEP 7: ANALYSIS (WRITE IN RECORD)
# -------------------------------
# Observations:
# - Model trained successfully
# - Mean Squared Error is low

# Pattern:
# - Linear relationship between input (X) and output (y)

# Insight:
# - Linear Regression fits data well
# - Model performance is consistent


# -------------------------------
# STEP 8: DOCUMENTATION
# -------------------------------
# Include:
# - Screenshot of MLflow dashboard
# - Screenshot of experiment runs
# - Table of parameters and metrics

# Example Table:
# Run | Model Type       | Data Size | MSE
# 1   | LinearRegression | 5         | 0.0


# -------------------------------
# STEP 9: DEMO / DEFENSE
# -------------------------------
# Say this:

# - MLflow is used to track machine learning experiments
# - Logged parameters and metrics
# - Multiple runs are stored and compared
# - Dashboard shows experiment results visually


# -------------------------------
# PURPOSE OF MLFLOW
# -------------------------------
# - Track experiments
# - Log parameters and metrics
# - Compare multiple runs
# - Improve model performance

#optuna
# EXPERIMENT 8: OPTUNA HYPERPARAMETER TUNING
# =====================================================

# -------------------------------
# STEP 1: INSTALL LIBRARIES
# -------------------------------
pip install optuna scikit-learn numpy


# -------------------------------
# STEP 2: CREATE FILE
# -------------------------------
# File: optuna_demo.py

import optuna
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import numpy as np

# Sample Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# -------------------------------
# BASELINE MODEL (NO TUNING)
# -------------------------------
model = Ridge(alpha=1.0)
model.fit(X, y)
pred = model.predict(X)
baseline_error = mean_squared_error(y, pred)

print("Baseline MSE:", baseline_error)


# -------------------------------
# OPTUNA OPTIMIZATION FUNCTION
# -------------------------------
def objective(trial):
    alpha = trial.suggest_float("alpha", 0.01, 10.0)

    model = Ridge(alpha=alpha)
    model.fit(X, y)
    pred = model.predict(X)

    mse = mean_squared_error(y, pred)
    return mse


# -------------------------------
# RUN OPTUNA STUDY
# -------------------------------
study = optuna.create_study(direction="minimize")
study.optimize(objective, n_trials=10)


# -------------------------------
# BEST RESULT
# -------------------------------
print("Best Parameters:", study.best_params)
print("Best MSE:", study.best_value)


# 1. GO TO YOUR PROJECT FOLDER
# -------------------------------
cd path/to/your/project


# -------------------------------
# 2. INITIALIZE GIT
# -------------------------------
git init
# Creates local repository


# -------------------------------
# 3. ADD FILES
# -------------------------------
git add .
# Adds all files


# -------------------------------
# 4. COMMIT FILES
# -------------------------------
git commit -m "Initial commit"
# Saves your code


# -------------------------------
# 5. CONNECT TO GITLAB
# -------------------------------
git remote add origin https://gitlab.com/username/project.git
# Replace with your GitLab repo URL


# -------------------------------
# 6. PUSH CODE TO GITLAB
# -------------------------------
git push -u origin main
# Uploads code to GitLab


# -------------------------------
# 7. CREATE NEW BRANCH
# -------------------------------
git checkout -b feature-login
# Creates and switches branch


# -------------------------------
# 8. MAKE CHANGES → ADD → COMMIT
# -------------------------------
git add .
git commit -m "Added login feature"


# -------------------------------
# 9. PUSH BRANCH
# -------------------------------
git push origin feature-login


# -------------------------------
# 10. MERGE (OPTION 1: TERMINAL)
# -------------------------------
git checkout main
git merge feature-login


# -------------------------------
# 11. PULL LATEST CHANGES
# -------------------------------
git pull origin main


# -------------------------------
# 12. CHECK STATUS
# -------------------------------
git status


# -------------------------------
# 13. VIEW HISTORY
# -------------------------------
git log

# CI/CD PIPELINE SETUP (GITLAB)
# -------------------------------

1. Create a project in GitLab
   - Go to GitLab
   - Click "New Project"
   - Enter project name and create

2. Upload project files
   - Add index.html (or any simple file)
   - Commit changes

3. Create pipeline configuration file
   - Click "+" → New File
   - Name: .gitlab-ci.yml

4. Add pipeline code

stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Build stage running"

test-job:
  stage: test
  script:
    - echo "Test stage running"

deploy-job:
  stage: deploy
  script:
    - echo "Deploy stage running"

5. Commit the file
   - Add commit message
   - Click "Commit changes"

6. Pipeline execution
   - Go to CI/CD → Pipelines
   - Pipeline runs automatically after commit

7. Verify pipeline
   - Check build, test, deploy stages
   - Ensure all jobs are successful (green)

8. View logs
   - Click each job
   - Check output messages

9. If pipeline fails
   - Open failed job
   - Check error logs
   - Fix YAML or script
   - Commit again

10. Analysis
   - Pipeline executed successfully
   - All stages completed
   - Execution time is low
   - No errors observed

11. Limitations
   - No real testing
   - Deployment is simulated

12. Improvements
   - Add real test cases
   - Add deployment server
   - Use parallel jobs

# -------------------------------
# PURPOSE OF PIPELINE
# -------------------------------
- Automates build, test, deployment
- Detects errors early
- Ensures consistency
- Speeds up development

stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Build stage running"

test-job:
  stage: test
  script:
    - echo "Test stage running"

deploy-job:
  stage: deploy
  script:
    - echo "Deploy stage running"



