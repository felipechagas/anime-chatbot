from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Metadata, Interpreter
import spacy

def train_nlu(data,configs,model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)

    model_directory = trainer.persist(model_dir, fixed_model_name='anime_nlu')

def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/anime_nlu')
    print(interpreter.parse(u"Olá, Tenho um cachorro e moro em Fortaleza"))

def run_nlp():
    nlp = spacy.load('pt')
    doc = nlp(u"Olá me chamo Newton e moro em Fortaleza")
    for i in doc.ents:
        print(str(i) + ',' + str(i.label_))

if __name__ == '__main__':
    train_nlu('./data/data_br.json', 'config_spacy.yml', './models/nlu')
    #run_nlu()
    #run_nlp()

#python -m rasa_nlu.server -c config_spacy.yml --path models/nlu
#curl -XPOST localhost:5000/parse -d '{"q":"Queria saber o temp em Fortaleza", "project":"default", "model":"anime_nlu"}'
