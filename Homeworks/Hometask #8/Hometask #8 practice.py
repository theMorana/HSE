#Аудиторная работа на паре

'''
fruits = ["apple", "banana", "cherry"]
print("Фрукты в корзине:")
for number, fruit in enumerate(fruits, start = 1):
    print(f"{number}. {fruit}")
'''

'''
cats = {
    "вид": "котик",
    "кличка": "Пушистик",
    "возраст": 5,
    "любит": ["играть с мышкой", "сбрасывать вещи с полки"],
    "не любит": "шумных соседей",
    "питание": "корм purina",
}


cats2 = dict(вид="котик",кличка="Пушистик", возраст= 5, любит=["играть с мышкой", "сбрасывать вещи с полки"],не_любит="шумных соседей", питание="корм purina")
cats3 = dict([("вид","котик"), ("кличка", "Пушистик"), ("возраст", 5), ("любит", ["играть с мышкой", "сбрасывать вещи с полки"]),("не_любит", "шумных соседей"), ("питание", "корм purina")])


value1 = cats["вид"]           
value2 = cats.get("кличка")       
value3 = cats.get("номер_хозяина", "N/A")

print(value1)
print(value2)
print(value3)

cats["не_любит"] = "смотреть ужастики"
cats["питание"] = "pro plan"
cats["возраст"] += 1

cats["номер хозяина"] = 657892
age = cats.pop("возраст")      # Удаляет и возвращает значение   
del cats["номер хозяина"]
print(cats)
'''


'''
#task 0
import json

#открытие файла
with open('data.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Итерирация по ключам верхнего уровня
print("Ключи верхнего уровня:")
for key in config.keys():
    print(key)
    
#Итерирация по значениям словаря departments
print("Ключи по значениям словаря departments:")
for employees in config['departments'].values():
    print(employees)

print("Ключ-значение словаря departments:")
for key, value in config['departments'].items():
    print(f"{key}: {value}")

config['departments']['dev'].append('David')
print(config['departments'])

config["budget"] =  int(config["budget"] * 1.1)
print(config["budget"])

#Запись
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=4)
'''



#Домашнее задание

#task 1 
config = {
    "model_name": "bert-base-uncased",
    "batch_size": 32,
    "max_length": 128,
    "learning_rate": 2e-5,
    "epochs": 3,
    "labels": ["positive", "negative", "neutral"]
}

version1 = config["learning_rate"]  
version2 = config.get("learning_rate")

config["early_stopping"] = True
config["batch_size"] = 64

print("Параметры с числами: ")
for key, value in config.items():
    if type(value) == int:
        print(f"{key}: {value}")
        
        
#копия для тестирования

test_config = config.copy()
test_config["batch_size"] = 8
test_config["epochs"] = 1

print("Конфигурация для тестирования:")
for key, value in test_config.items():
    print(f"  {key}: {value}")



#task 2
api_response = {
    "text": "I really enjoyed the movie, the acting was amazing!",
    "sentiment": {
        "label": "positive",
        "score": 0.95,
        "confidence": "high"
    },
    "entities": [
        {"entity": "movie", "type": "ENTERTAINMENT", "confidence": 0.89},
        {"entity": "acting", "type": "SKILL", "confidence": 0.92}
    ],
    "language": "en",
    "processed_in": 0.45
}

score_data = {api_response["sentiment"]["score"]}
print(f"Оценка тональности: {score_data}")

print("Названия сущностей:")
for entity_info in api_response["entities"]:
    print(f"{entity_info['entity']}")

max_confidence_entity = max(api_response["entities"], 
                            key=lambda x: x["confidence"])
print(f"Сущность с max confidence ({max_confidence_entity['confidence']}): {max_confidence_entity['entity']}")

api_response["model_version"] = "2.1.0"
api_response["model_version"] = float()


print("Отфильтрованный список: ")
for key, value in api_response.items():
    if type(value) != str:
        print(f"{key}: {value}")
        

#task 3

pipeline_config = {
    "steps": {
        "tokenization": {"enabled": True, "method": "word"},
        "stopwords": {"enabled": True, "language": "english", "custom_words": []},
        "stemming": {"enabled": False, "algorithm": "porter"},
        "normalization": {"enabled": True, "lowercase": True, "remove_punct": True}
    },
    "input_encoding": "utf-8",
    "output_format": "tokens"
}

pipeline_config["steps"]["stemming"]["enabled"] = True
pipeline_config["steps"]["stemming"]["custom_words"] = "numbers"


enabled_steps = [step for step, config in pipeline_config["steps"].items() if config["enabled"] == True]
print(f"Включённые шаги: {enabled_steps}")
print()

#configuration

simplified_config = {
    "steps": {
    },
    "input_encoding": "utf-8",
    "output_format": "tokens"
}

for key, value in pipeline_config["steps"].items():
    if value["enabled"] == True: 
        simplified_config["steps"][key] = value
        
print("Упрощённая конфигурация (только включённые шаги):")
for key, value in simplified_config.items():
    print(f"  {key}: {value}")



#task 4
models_stats = {
    "bert-base": {
        "accuracy": 0.92,
        "f1_score": 0.91,
        "inference_time": 120,
        "size_mb": 440
    },
    "distilbert": {
        "accuracy": 0.89,
        "f1_score": 0.88,
        "inference_time": 65,
        "size_mb": 250
    },
    "roberta-large": {
        "accuracy": 0.94,
        "f1_score": 0.93,
        "inference_time": 210,
        "size_mb": 1600
    }
}


max_accuracy = max(models_stats.items(), key=lambda x: x[1]["accuracy"])
print(f"Лучшая точность ({max_accuracy[1]['accuracy']}): {max_accuracy[0]}.")

inference_times = [stats["inference_time"] for stats in models_stats.values()]
avg_inference_time = sum(inference_times) / len(inference_times)
print(f"Среднее время инференса: {avg_inference_time:.1f} мс")

metrics_only = {
    name: {
        "accuracy": data["accuracy"],
        "f1_score": data["f1_score"]
    }
    for name, data in models_stats.items()
}
print("Только метрики accuracy и f1_score:", metrics_only)

models_stats["albert-base"] = {
    "accuracy": 0.87,
    "f1_score": 0.86,
    "inference_time": 55,
    "size_mb": 180
}

small_models = {
    name: data for name, data in models_stats.items()
    if data["size_mb"] < 500
}
print("Модели меньше 500 МБ:", small_models)


#task 5

#открытие файла
with open('nlp_service_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)


config["models"]["summarization"] = {
    "path": "/models/summarization",
    "max_input_length": 2048,
    "supported_languages": ["en", "es", "fr"]
}
config["rate_limit"] += 50
config["models"]["sentiment"]["supported_languages"].append("ru")

server_settings = config["server"]

with open("nlp_service_config_updated.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

