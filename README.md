# Получение информации о тикерах с сайта CoinMarketCap
### С помощью данной программы можно получать информацию о криптовалюте, также можно вывести значение ранга криптовалюты в файл формата Excel

## Установка и запуск

 Для MacOs и Linux вместо python использовать python3

**1. Клонировать репозиторий:**
```
git clone https://https://github.com/ViktorovGO/get_cripto_ranks
```

**2. Перейти в папку проекта:**
```
cd /get_cripto_ranks/
```

**3. Cоздать и активировать виртуальное окружение:**
```
python -m venv venv
```

Для Windows:
```
venv\Scripts\activate.bat
```

Для MacOs/Linux:
```
source venv/bin/activate
```

**4. Установить зависимости из файла requirements.txt:**
- Обновить пакетный менеджер pip
```
python -m pip install --upgrade pip
```

- Установить зависимости
```
pip install -r requirements.txt
```
**5.Создать файл .env для хранения ключей:**
~~~
token=<coinmarketcap_token> # coinmarketcap token 
~~~
- ***[GET TOKEN](https://coinmarketcap.com/api/)***

**6. Запустить проект:**
```
python bitok.py
```
