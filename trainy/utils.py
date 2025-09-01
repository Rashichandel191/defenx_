# utils.py
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import roc_curve, auc

def plot_confusion_matrix(cm):
    fig = ff.create_annotated_heatmap(
        cm, x=["Safe","Fake"], y=["Safe","Fake"], colorscale="Teal", showscale=True
    )
    return fig

def plot_roc_curve(y_true, y_proba):
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    roc_auc = auc(fpr, tpr)
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, color="blue", lw=2, label=f"AUC={roc_auc:.2f}")
    ax.plot([0, 1], [0, 1], color="gray", linestyle="--")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.legend()
    return fig

def classification_report_df(y_true, y_pred):
    from sklearn.metrics import classification_report
    report = classification_report(y_true, y_pred, target_names=["Safe","Fake"], output_dict=True)
    return pd.DataFrame(report).transpose()

def plot_permission_bar(permissions_data):
    import matplotlib.pyplot as plt
    import seaborn as sns
    fig, ax = plt.subplots()
    sns.barplot(x=list(permissions_data.keys()), y=list(permissions_data.values()), ax=ax, palette="Reds_r")
    ax.set_ylabel("Frequency")
    ax.set_title("Risky Permissions in Fake Apps")
    return fig
