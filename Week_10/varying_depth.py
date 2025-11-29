from ucimlrepo import fetch_ucirepo
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.metrics import precision_score, recall_score, classification_report, f1_score
# ------------------------------------------------------------------------------------------------
# Same code as before (from previous decision tree activity) in order to be able to graphs showing most important features and varying depths
# Load dataset
rice_cammeo_and_osmancik = fetch_ucirepo(id=545)
X = rice_cammeo_and_osmancik.data.features
y = rice_cammeo_and_osmancik.data.targets

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=77, stratify=y_encoded
)

# Train decision tree classifier
clf = DecisionTreeClassifier(random_state=77, max_depth=4)
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# --------------------------------------------------------------------------------------------
# Create graph to see how depth affects precision, recall and f1_score
depth_values = range(1, 16)  # depths from 1 to 15
precisions = []
recalls = []
f1_scores = []

for depth in depth_values:
    clf = DecisionTreeClassifier(random_state=77, max_depth=depth)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    
    precisions.append(precision_score(y_test, y_pred, average="binary"))
    recalls.append(recall_score(y_test, y_pred, average="binary"))
    f1_scores.append(f1_score(y_test, y_pred, average="binary"))

# Plotting 
col1, col2 = st.columns(2)

with col1:
    fig2, ax2 = plt.subplots(figsize=(10,6))
    ax2.plot(depth_values, precisions, marker='o', label='Precision')
    ax2.plot(depth_values, recalls, marker='s', label='Recall')
    ax2.plot(depth_values, f1_scores, marker='^', label='F1 Score')

    ax2.set_xlabel('Tree Depth')
    ax2.set_ylabel('Score')
    ax2.set_title('Precision, Recall, and F1 vs Decision Tree Depth')
    ax2.legend()
    ax2.grid(True)


    st.pyplot(fig2)
    plt.close(fig2)

# --------------------------------------------------------------------------------------------
# Create graph to see feature importances
# Get feature importances and feature names
importances = clf.feature_importances_

feature_names = X.columns

# Sort features by importance descending
indices = importances.argsort()[::-1]
sorted_importances = importances[indices]
sorted_features = [feature_names[i] for i in indices]

# Plot
with col2:
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3.barh(range(len(sorted_importances)), sorted_importances, align='center')
    ax3.set_yticks(range(len(sorted_importances)))
    ax3.set_yticklabels(sorted_features)
    ax3.invert_yaxis()  # largest on top
    ax3.set_xlabel("Feature Importance")
    ax3.set_title("Feature Importances from Decision Tree")

    st.pyplot(fig3)
    plt.close(fig3)