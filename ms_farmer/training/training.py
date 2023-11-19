import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# Carrega o conjunto de dados
data = pd.read_csv('D:\\Programas\\Microsoft-Rewards-Farmer-master\\training\\diabetes.csv')

# Divide o conjunto de dados em dados de treinamento e dados de teste
X_train, X_test, y_train, y_test = train_test_split(data.drop('Outcome', axis=1), data['Outcome'], test_size=0.2, random_state=42)

# Cria um modelo de regressão logística e ajusta aos dados de treinamento
model = LogisticRegression()
model.fit(X_train, y_train)

# Faz previsões com o modelo nos dados de teste
y_pred = model.predict(X_test)

# Avalia o desempenho do modelo usando os dados de teste
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)

print("Acurácia: {:.2f}%".format(accuracy*100))
print("Precisão: {:.2f}%".format(precision*100))
print("Revocação: {:.2f}%".format(recall*100))
print("Matriz de confusão:\n", confusion)
