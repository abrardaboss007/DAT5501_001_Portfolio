from ucimlrepo import fetch_ucirepo
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, classification_report
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.metrics import precision_score, recall_score, classification_report, f1_score

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

# Evaluate metrics
precision = precision_score(y_test, y_pred, average="binary")
recall = recall_score(y_test, y_pred, average="binary")

report = classification_report(y_test, y_pred, target_names=le.classes_)
st.title("Classification Report")
st.code(report)    # <-- shows nicely aligned table with monospace font

# Plot the tree
fig1, ax1 = plt.subplots(figsize=(20, 10))
plot_tree(
    clf,
    filled=True,
    feature_names=rice_cammeo_and_osmancik.data.feature_names,
    class_names=le.classes_,
    ax=ax1,
    fontsize=12,
)
fig1.tight_layout()
st.pyplot(fig1)
plt.close(fig1)  # close figure to free memory

col1, col2 = st.columns(2)
with col1:
    st.write(f"### Precision: {precision:.4f}")

with col2:
    st.write(f"### Recall: {recall:.4f}")

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeClassifier

# # Pick first two features from your dataset
# X_two = X.iloc[:, :2].values  # if X is a DataFrame; use X[:, :2] if numpy array

# # Encode labels if needed
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y_encoded = le.fit_transform(y)  # convert 'c'/'o' to 0/1

# # Train decision tree with max_depth=1 (single split)
# clf = DecisionTreeClassifier(max_depth=1, random_state=42)
# clf.fit(X_two, y_encoded)

# # Create figure and axes - OO method
# fig2, ax2 = plt.subplots(figsize=(8,6))

# # Plot data points by class with markers and colors
# for label, marker, color in zip([0,1], ['s', '^'], ['orange', 'blue']):
#     ax2.scatter(X_two[y_encoded==label, 0], X_two[y_encoded==label, 1], 
#                 marker=marker, color=color, label=le.classes_[label])

# # Set axis labels and title
# st.write(rice_cammeo_and_osmancik.data.feature_names)
# ax2.set_xlabel(rice_cammeo_and_osmancik.data.feature_names[1])
# ax2.set_ylabel(rice_cammeo_and_osmancik.data.feature_names[2])
# ax2.set_title("Decision Tree Decision Boundary")

# # Draw the decision boundary line from the decision tree threshold
# threshold = clf.tree_.threshold[0]
# feature_index = clf.tree_.feature[0]

# if feature_index == 0:
#     # vertical line at threshold on feature 0
#     ax2.axvline(x=threshold, color='purple', linestyle='--')
# elif feature_index == 1:
#     # horizontal line at threshold on feature 1
#     ax2.axhline(y=threshold, color='purple', linestyle='--')

# ax2.legend()
# st.pyplot(fig2)

