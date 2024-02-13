## [Stuff] - Converting Swagger 2.0 YAML to openapi data model (fastapi)

1. You will get ability to use acunetix's API with fastapi (swagger/redoc)
2. Get YAML API model here: `https://YOUR_IP:13443/Acunetix-API-Documentation.yaml`
3. Convert it to **openapi yaml** [Here](https://editor-next.swagger.io/) and save as api.yaml
3. Highly recomended to use **python's venv**: `python3 -m venv .venv && . ./.venv/bin/activate`
4. `pip install -r requirements.txt`
5. `datamodel-codegen --input api.yaml --input-file-type yaml --output models.py`