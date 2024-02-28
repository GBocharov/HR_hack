
import json
from schema import  Vacancy, Resume, DodikSet

with open('data/train.json', encoding='utf-8') as f:
    data = json.loads(f.read())

d = [DodikSet(**i) for i in data]