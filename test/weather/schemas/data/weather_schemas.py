import json
from typing import List, Dict

basic_weather_data: Dict[str, int] = {"temperature": 24}

basic_weather_data_json = json.dumps(basic_weather_data)

weather_schema_fields: List[str] = list(basic_weather_data.keys())
