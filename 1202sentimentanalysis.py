#title: "Sentiment Analysis"
#author: "Kaitlyn Westra"
#date: "02 December 2020"


from transformers import pipeline
from pprint import pprint

sentiment_pipeline = pipeline("sentiment-analysis")

def text_to_sentiment(sentence):
  result = sentiment_pipeline(sentence)[0]
  if result['label'] == "POSITIVE": return result['score']
  if result['label'] == "NEGATIVE": return -result['score']
  raise ValueError("Unknown result label: " + result['label'])

print('hate'+str(text_to_sentiment("I hate you")))
print('love'+str(text_to_sentiment("I love you")))
print('bad'+str(text_to_sentiment("This is bad.")))
print('not bad'+str(text_to_sentiment("This is not that bad.")))
print('Italian'+str(text_to_sentiment("Let's go get Italian food")))
print('Chinese'+str(text_to_sentiment("Let's go get Chinese food")))
print('Mexican'+str(text_to_sentiment("Let's go get Mexican food")))

print('emily'+str(text_to_sentiment("My name is Emily")))
print('heather'+str(text_to_sentiment("My name is Heather")))
print('latisha'+str(text_to_sentiment("My name is Latisha")))
print('nour'+str(text_to_sentiment("My name is Nour")))


NAMES_BY_ETHNICITY = {
    # The first two lists are from the Caliskan et al. appendix describing the
    # Word Embedding Association Test.
    'White': [
        'Adam', 'Chip', 'Harry', 'Josh', 'Roger', 'Alan', 'Frank', 'Ian', 'Justin',
        'Ryan', 'Andrew', 'Fred', 'Jack', 'Matthew', 'Stephen', 'Brad', 'Greg', 'Jed',
        'Paul', 'Todd', 'Brandon', 'Hank', 'Jonathan', 'Peter', 'Wilbur', 'Amanda',
        'Courtney', 'Heather', 'Melanie', 'Sara', 'Amber', 'Crystal', 'Katie',
        'Meredith', 'Shannon', 'Betsy', 'Donna', 'Kristin', 'Nancy', 'Stephanie',
        'Bobbie-Sue', 'Ellen', 'Lauren', 'Peggy', 'Sue-Ellen', 'Colleen', 'Emily',
        'Megan', 'Rachel', 'Wendy'
    ],
    'Black': [
        'Alonzo', 'Jamel', 'Lerone', 'Percell', 'Theo', 'Alphonse', 'Jerome',
        'Leroy', 'Rasaan', 'Torrance', 'Darnell', 'Lamar', 'Lionel', 'Rashaun',
        'Tyree', 'Deion', 'Lamont', 'Malik', 'Terrence', 'Tyrone', 'Everol',
        'Lavon', 'Marcellus', 'Terryl', 'Wardell', 'Aiesha', 'Lashelle', 'Nichelle',
        'Shereen', 'Temeka', 'Ebony', 'Latisha', 'Shaniqua', 'Tameisha', 'Teretha',
        'Jasmine', 'Latonya', 'Shanise', 'Tanisha', 'Tia', 'Lakisha', 'Latoya',
        'Sharise', 'Tashika', 'Yolanda', 'Lashandra', 'Malika', 'Shavonn',
        'Tawanda', 'Yvette'
    ],
    # This list comes from statistics about common Hispanic-origin names in the US.
    'Hispanic': [
        'Juan', 'José', 'Miguel', 'Luís', 'Jorge', 'Santiago', 'Matías', 'Sebastián',
        'Mateo', 'Nicolás', 'Alejandro', 'Samuel', 'Diego', 'Daniel', 'Tomás',
        'Juana', 'Ana', 'Luisa', 'María', 'Elena', 'Sofía', 'Isabella', 'Valentina',
        'Camila', 'Valeria', 'Ximena', 'Luciana', 'Mariana', 'Victoria', 'Martina'
    ],
    # The following list conflates religion and ethnicity, I'm aware. So do given names.
    #
    # This list was cobbled together from searching baby-name sites for common Muslim names,
    # as spelled in English. I did not ultimately distinguish whether the origin of the name
    # is Arabic or Urdu or another language.
    #
    # I'd be happy to replace it with something more authoritative, given a source.
    'Arab/Muslim': [
        'Mohammed', 'Omar', 'Ahmed', 'Ali', 'Youssef', 'Abdullah', 'Yasin', 'Hamza',
        'Ayaan', 'Syed', 'Rishaan', 'Samar', 'Ahmad', 'Zikri', 'Rayyan', 'Mariam',
        'Jana', 'Malak', 'Salma', 'Nour', 'Lian', 'Fatima', 'Ayesha', 'Zahra', 'Sana',
        'Zara', 'Alya', 'Shaista', 'Zoya', 'Yasmin'
    ]
}

# >> cut to R for figures & analysis <<


# Q & A

## example 
qa_pipeline = pipeline("question-answering")
context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/question-answering/run_squad.py script.
"""
result = qa_pipeline(question="What is extractive question answering?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = qa_pipeline(question="What is a good example of a question answering dataset?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

## Named Entity Recognition 
ner_pipeline = pipeline("ner", grouped_entities = True)
sequence = ("Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very"
           "close to the Manhattan Bridge which is visible from the window.")
pprint(ner_pipeline(sequence))


## on Calvin wikipedia paragraph
calvin_sequence = ("The Christian Reformed Church in North America founded the school on August 4, 1876, as part of Calvin College and Theological Seminary (with the seminary becoming Calvin Theological Seminary) to train church ministers. The college and seminary began with seven students, in a rented upper room on Spring Street, in Grand Rapids, Michigan. The initial six-year curriculum included four years of literary studies and two years of theology. In 1892, the campus moved to the intersection of Madison Avenue and Franklin Street (Fifth Avenue) in Grand Rapids. In September 1894, the school expanded the curriculum for those who were not pre-theological students, effectually making the institution a preparatory school. In 1900, the curriculum further broadened, making it more attractive to students interested in teaching or preparing for professional courses at universities. In 1901, Calvin admitted the first women to the school.[6]")
pprint(ner_pipeline(calvin_sequence))

result = qa_pipeline(question="Where was the old campus?", context=calvin_sequence)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = qa_pipeline(question="When was Calvin started?", context=calvin_sequence)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = qa_pipeline(question="Where was Calvin's first campus?", context=calvin_sequence)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = qa_pipeline(question="Where was Calvin's second campus?", context=calvin_sequence)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = qa_pipeline(question="Where was Calvin's third campus?", context=calvin_sequence)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

result = qa_pipeline(question="Where was Calvin's fourth campus?", context=calvin_sequence)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")


