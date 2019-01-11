import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    training_data_file = './data/stories.md'
    model_path = './models/dialogue'

    agent = Agent('anime_domain.yml', policies=[MemoizationPolicy(), KerasPolicy(max_history=2, epochs=500, batch_size=10, validation_split=0.2, augmentation_factor=50)])

    data = agent.load_data(training_data_file)

    agent.train(
        data #,
        #augmentation_factor = 50, #Especifica o numero de stories que o rasa cria para auxiliar no treinamento do modelo
        #max_history = 2,#numero de estados que o modelo armazena. Deve aumentar conforme o tamanho do dataset
        #epochs = 500,
        #batch_size = 10,
        #validation_split = 0.2
    )

    agent.persist(model_path)