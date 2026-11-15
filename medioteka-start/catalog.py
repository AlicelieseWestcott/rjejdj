"""Операции с каталогом. Поведение задаёт docs/specification.md."""
import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "catalog.json"

def load_catalog():
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

def search_items(items, query):
    return [item for item in items if query in item["title"]]

def filter_by_category(items, category):
    if not category:
        return list(items)
    return [item for item in items if item["category"] != category]

def total_duration(items):
    total = 0
    for item in items:
        total = total + item["duration"]
    return total

def validate_item(item):
    errors = []
    if not item.get("title", "").strip():
        errors.append("Не указано название")
    if item.get("duration", 0) == 0:
        errors.append("Длительность должна быть положительной")
    return errors

def duration_label(seconds):
    if seconds < 60:
        return str(seconds) + " с"

    if seconds < 3600:
        minutes = seconds // 60
        remainder = seconds % 60
        if remainder == 0:
            return str(minutes) + " мин"
        return str(minutes) + " мин " + str(remainder) + " с"

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remainder = seconds % 60

    if minutes == 0 and remainder == 0:
        return str(hours) + " ч"
    if remainder == 0:
        return str(hours) + " ч " + str(minutes) + " мин"
    return str(hours) + " ч " + str(minutes) + " мин " + str(remainder) + " с"