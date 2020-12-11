import sqlite3

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")
cursor.execute("PRAGMA foreign_keys=1")

cursor.execute('''CREATE TABLE model_params (
               id INTEGER NOT NULL,
               desc TEXT,
               param_name TEXT NOT NULL,
               value FLOAT,
               PRIMARY KEY (id, param_name))''')

db.commit()  # Commit changes to the database

cursor.execute('''CREATE TABLE model_coefs (
          id INTEGER NOT NULL,
          desc TEXT,
          feature_name TEXT,
          value FLOAT,
          PRIMARY KEY (id, feature_name))''')

db.commit()

cursor.execute('''CREATE TABLE model_results (
          id INTEGER PRIMARY KEY NOT NULL,
          desc TEXT,
          train_score FLOAT,
          test_score FLOAT)''')

db.commit()

############ Part B ################
# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)


def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    # predict and get score
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    # insert into table
    cursor = db.cursor()
    model_params = model.get_params()
    model_coef = model.coef_

    # insert param
    for i in model_params:
        model_params_to_insert = (model_id, model_desc, i, model_params[i])
        cursor.execute('''INSERT INTO model_params
                      (id, desc, param_name, value)
                      VALUES (?, ?, ?, ?)''', model_params_to_insert)

    # insert intercept
    cursor.execute('''INSERT INTO model_coefs
                          (id, desc, feature_name, value)
                          VALUES (?, ?, ?, ?)''', (model_id, model_desc, "intercept", model.intercept_[0]))

    # insert coef
    for i in range(len(model_coef[0])):
        model_coef_to_insert = (model_id, model_desc, data.feature_names[i], model_coef[0][i])
        cursor.execute('''INSERT INTO model_coefs
                         (id, desc, feature_name, value)
                         VALUES (?, ?, ?, ?)''', model_coef_to_insert)

    # insert model results
    cursor.execute('''INSERT INTO model_results
                         (id, desc, train_score, test_score)
                         VALUES (?, ?, ?, ?)''', (model_id, model_desc, train_score, test_score))

    db.commit()


# Fit baseline model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)

save_to_database(1, 'Baseline model', db, baseline_model, X_train, X_test, y_train, y_test)

# reduced logistic model
feature_cols = ['mean radius',
                'texture error',
                'worst radius',
                'worst compactness',
                'worst concavity']

X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]

reduced_model = LogisticRegression(solver='liblinear')
reduced_model.fit(X_train_reduced, y_train)

save_to_database(2, 'Reduced model', db, reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

# Fit penalized  model
penalized_model = LogisticRegression(solver='liblinear', penalty='l1', random_state=87, max_iter=150)
penalized_model.fit(X_train, y_train)
save_to_database(3, 'L1 penalty model', db, penalized_model, X_train, X_test, y_train, y_test)


############ Part C ################
query = '''SELECT * FROM model_results ORDER BY test_score DESC LIMIT 1'''
best_model_record = cursor.execute(query).fetchall()
best_model_id = int(best_model_record[0][0])
print("Best model id: %i" % best_model_id)
print("Best validation score: %f" % best_model_record[0][3])


# print and store coef and intercept
best_model_coef = cursor.execute('''SELECT * FROM model_coefs WHERE id = ?''', (best_model_id,)).fetchall()
best_intercept = None
feature_sequence = list(data.feature_names)
best_coef = [None for i in range(len(feature_sequence))]

for row in best_model_coef:
    if row[2] == "intercept":
        best_intercept = float(row[3])
    else:
        # find the index of coef w.r.t its feature name
        idx = feature_sequence.index(row[2])
        best_coef[idx] = float(row[3])
    print(row[2] +": "+str(row[3]))


# dummy fit to reproduce the test score
test_model = LogisticRegression(solver='liblinear')
test_model.fit(X_train, y_train)

# Manually change fit parameters
test_model.coef_ = np.array([best_coef])
test_model.intercept_ = np.array([best_intercept])

test_score = test_model.score(X_test, y_test)
print(f'Reproduced best validation score: {test_score}')

# close db
db.close()