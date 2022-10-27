import tensorflow_hub as TensorFlowHub

def embedding_gen(title):
    model = TensorFlowHub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")
# embeddings = model(title)
# print(embedding)

amazon_title = "Fire TV Stick Lite | Streaming em Full HD com Alexa | Com Controle Remoto Lite por Voz com Alexa (sem controles de TV)"
embedding_gen(amazon_title)
