

# ML Janitor

Библиотека для быстрой очистки данных в pandas DataFrame. Удаляет столбцы с большим количеством пропущенных значений.

## Установка

```bash
pip install git+https://github.com/EloanOnik/ml_janitor
```

Или установка из исходников:

```bash
git clone https://github.com/your-username/ml_janitor.git
cd ml_janitor
pip install -e .
```

## Быстрый старт

```python
import pandas as pd
from cleaner import drop_empty_columns

# Ваши данные
df = pd.DataFrame({
    'полезный_столбец': [1, 2, 3, 4, 5],
    'много_пустых': [None, None, None, None, 10],
    'сплошные_пустые': [None, None, None, None, None]
})

# Удаляем столбцы, где 70%+ пропусков (настройка по умолчанию)
clean_df = drop_empty_columns(df)
print(clean_df.columns)  # ['полезный_столбец']
```

## Как настроить под себя

### Хотите удалять столбцы с другим процентом пустых значений?

Просто передайте свой порог в параметре `threshold`:

```python
# Удаляем столбцы, где пустых 50% или больше
clean_df = drop_empty_columns(df, threshold=0.50)

# Удаляем столбцы, где пустых 90% или больше  
clean_df = drop_empty_columns(df, threshold=0.90)

# Удаляем столбцы, где есть ХОТЯ БЫ ОДНО пустое значение
clean_df = drop_empty_columns(df, threshold=0.01)
```

### Хотите просто узнать, какие столбцы будут удалены?

```python
from cleaner import find_empty_columns

# Узнать список "плохих" столбцов (где 70%+ пустых)
bad_columns = find_empty_columns(df)
print(f"Будут удалены: {bad_columns}")

# Узнать для другого порога
bad_columns = find_empty_columns(df, threshold=0.50)
print(f"При пороге 50% удалятся: {bad_columns}")
```

## Примеры использования

### Пример 1: Очистка данных опроса

```python
# В опросе много необязательных вопросов
survey_df = pd.read_csv('опрос.csv')

# Оставляем только вопросы, на которые ответило >80% респондентов
clean_survey = drop_empty_columns(survey_df, threshold=0.80)
```

### Пример 2: Предварительный анализ

```python
# Сначала смотрим, что удалится при разных порогах
for threshold in [0.30, 0.50, 0.70, 0.90]:
    bad = find_empty_columns(my_big_dataframe, threshold=threshold)
    print(f"Порог {threshold:.0%}: удалится {len(bad)} столбцов")
```

## Доступные функции

### `drop_empty_columns(df, threshold=0.70)`

**Что делает:** Возвращает НОВЫЙ DataFrame без столбцов с пустотами ≥ threshold

**Параметры:**
- `df` — ваш DataFrame (не изменится!)
- `threshold` — порог пустых значений (от 0 до 1, по умолчанию 0.70 = 70%)

**Возвращает:** Новый чистый DataFrame

### `find_empty_columns(df, threshold=0.70)`

**Что делает:** Находит столбцы для удаления

**Параметры:** Такие же, как у `drop_empty_columns`

**Возвращает:** Список названий столбцов

## Часто задаваемые вопросы

### Как изменить процент по умолчанию навсегда?

Создайте свою функцию-обёртку:

```python
def my_cleaner(df):
    return drop_empty_columns(df, threshold=0.50)
```

### Изменяет ли функция мои исходные данные?

Нет! Исходный DataFrame остаётся без изменений. Функция возвращает новый.

### Что считается "пустым значением"?

Всё, что pandas считает пустым: `None`, `NaN`, пустые строки (в зависимости от типа данных).

## Лицензия

MIT — делайте что хотите :)

## Нужна помощь?

tg:@onikeloyan
