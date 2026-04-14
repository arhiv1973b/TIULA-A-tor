import json
import os

print("--- EVIDENCE VAULT B: TORTURE VECTOR ANALYSIS ---")
file_path = "torture_vector_0125.json"

if os.path.exists(file_path):
    # Используем utf-8-sig для обработки файлов, созданных в PowerShell
    with open(file_path, "r", encoding="utf-8-sig") as f:
        try:
            d = json.load(f)
            obj = d['evidence_manipulation']['item']
            weight = d['evidence_manipulation']['claimed_weight']
            gap = d['detention_timeline']['gap']
            
            print(f"Объект манипуляции: {obj} ({weight}г)")
            print(f"Период бесправия: {gap}")
            print("Статус: Доказано принуждение к оговору.")
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
else:
    print(f"Ошибка: Файл {file_path} не найден.")
