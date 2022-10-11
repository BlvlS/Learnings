import re

s = "Привет! Как дела? А у меня нормально."
result = re.findall(r"[цкнгшщзхфвпрлджчсмтбБТМСЧФВПРЛДЖХЗЩШГНКЦ]\w+", s)
print(result)