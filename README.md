# nlp-proj-LPD
 
 Hello,
The goal of this project was to identify LPD possible in sentences for hebrew

for example:
"היה לי לוחם ממש טוב" <=> "היה לי חלום ממש טוב",
"רוצה לבוא לאכול גדילה" <=> "רוצה לבוא לאכול גלידה"

In this project has several parts:

## Preparation of the information:
I downloaded form Mila site : http://www.mila.cs.technion.ac.il/resources_corpora_wikipedia_2013.html
Corpus for wikpdia 2013, And extracted as many sentences as I could (more 192000000 sentences)
It was not simple 
(prepareTheCorpus.py)

## create Vocabulary,Bigram Model, And LPD sentence
The next step was to create a vocabulary, a Bigram model and I test sentences with LPD
the test sentence is not import to train courps.

## tests:
### baseLine:
the baseLine is simple:
For each word I choose a random combinator, that exists in a dictionary. of all possible combinations.
The results were really bad: 0%
Almost all the words in the sentence were changed and no sentence came out as the desired sentence.

### unigram or other words Which appeared most often:
For each word I choose a the word that appeared most often.
The results were a bit nicer: 64%

### Bigram:
For each word I choose the word that its probability when known as the previous word and the next word is the highest.
The results in this case were really impressive:97%

# Play yourself:
for play yourself run test model bigram.

1. You can enter any sentence you want and test it.
2. You can choose a sentence between the test corpus.
3. You can select a sentence that has an error from the test corpus.
(It helped me check the errors, and improve the results)

Thanks
