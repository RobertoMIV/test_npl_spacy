# test_npl_spacy
Requirements:
spacy==3.7.1
flask==3.0.0
python 3.8.10

Para correr:

python3 api_spacy.py


Para probar el script:

curl -X POST -H "Content-Type: application/json" -d '{"oraciones": ["Apple busca comprar una startup del Reino Unido por mil millones de dolares.", "San Francisco busca prohibir los robots"]}' http://127.0.0.1:5000/process_text
