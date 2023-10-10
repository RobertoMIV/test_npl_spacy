from flask import Flask, request, jsonify
import spacy

# Load your spaCy model
nlp = spacy.load("es_core_news_sm")

# Load your spaCy model
nlp = spacy.load("es_core_news_sm")
app = Flask(__name__)

@app.route('/process_text', methods=['POST'])
def process_text():
    # Get JSON data from the request
    data = request.get_json()

    # Check if 'text' key exists in the JSON data
    if 'oraciones' not in data:
        return jsonify({'error': 'Missing "text" parameter'}), 400

    entities_list = list()
    # extract sentences
    for text in data['oraciones']:
        # Process the text using spaCy
        doc = nlp(text)
        entities = {'oracion':text,'entidades':[{str(ent.text):ent.label_} for ent in doc.ents]}
        #append for each sentence
        entities_list.append(entities)

    # Return the results as JSON
    return jsonify({'resultado': entities_list})

if __name__ == '__main__':
    app.run(debug=True)