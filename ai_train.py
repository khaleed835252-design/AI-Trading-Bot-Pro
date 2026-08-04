import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# قراءة البيانات
df = pd.read_csv("training_dataset.csv")

# حذف الصفوف الناقصة
df = df.dropna()

# تحويل Outcome إلى أرقام
df["Outcome"] = df["Outcome"].map({
    "WIN": 1,
    "LOSS": 0
})

# اختيار الخصائص
X = df[[
    "EMA20",
    "EMA50",
    "EMA200",
    "RSI",
    "MACD",
    "MACD_SIGNAL",
    "ATR",
    "Volume"
]]

# النتيجة
y = df["Outcome"]

# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# تدريب النموذج
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print(f"Accuracy: {accuracy:.2%}")

joblib.dump(
    model,
    "ai_model.pkl"
)

print("Model Saved")