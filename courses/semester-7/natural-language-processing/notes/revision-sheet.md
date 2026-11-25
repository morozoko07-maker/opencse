---
title: Revision sheet
---
# Revision sheet — Natural Language Processing

Natural Language Processing (BCA703A) is a CSE/AI course. The material covers five areas: introduction and grammar, word-level and syntactic analysis, Naive Bayes classification, information retrieval and lexical resources, and machine translation.

## Exam pattern

The internal-assessment paper is 40 marks and uses 4-mark, 6-mark and 10-mark questions, with OR choices.

## Module 1 — Introduction, knowledge and grammar

### Must know

- NLP versus natural language understanding; translation, retrieval, sentiment and summarisation.
- Types of knowledge needed: phonological, morphological, syntactic, semantic, pragmatic and world knowledge.
- Challenges: ambiguity, context dependence, variability, implicit knowledge, morphology, noisy input and multilingual issues.
- Grammar models: generative, hierarchical, Government and Binding, transformational grammar, X-bar theory and LFG.
- Karaka relations: karta, karma, karana, sampradana, apadana and adhikarana.

### Definitions to reproduce

**NLP** is the field of AI that enables computers to understand, interpret and generate human language. **Ambiguity** is the presence of more than one possible interpretation at a linguistic level. A **transformational rule** converts one phrase marker into another, for example active to passive. **X-bar theory** represents phrases as projections of a head: X′, X″. In **LFG**, c-structure is the phrase structure and f-structure is the functional representation of grammatical relations.

### Worked pattern

For the LFG question "I saw Abhishek in the market at night", draw the c-structure using S → NP VP, VP → V NP PP PP, PP → P NP. Then write the f-structure with PRED `see`, SUBJ `I`, OBJ `Abhishek`, and two ADJuncts.

## Module 2 — Word-level and syntactic analysis

### Must know

- Tokenisation and regular expressions; finite-state automata and transducers.
- Morphological parsing, inflection, derivation and compounding; stemming and lemmatisation.
- Spelling correction; minimum edit distance by dynamic programming.
- Part-of-speech tagging: rule-based, stochastic HMM with Viterbi, and Transformation-Based Learning.
- Context-free grammars, top-down and bottom-up parsing, and the CYK algorithm.
- N-gram language models and the chain rule with Markov assumptions.

### Definitions to reproduce

A **morpheme** is the smallest meaning-bearing unit. An **FST** maps one representation to another, such as surface form to stem plus features. **Minimum edit distance** is the least number of insertions, deletions and substitutions that turn one string into another. **POS tagging** assigns a grammatical category to each token. **CYK** is a bottom-up chart parser for grammars in Chomsky normal form.

### Worked pattern

For `flour` → `flower`, insert `w` after `o` and substitute `u` with `e`, giving two edits; show the matrix and trace the backpointers. For a bigram question, pad the sentence with `<s>` and `</s>`, count bigrams, and multiply conditional probabilities; smooth zero counts.

## Module 3 — Naive Bayes and text classification

### Must know

- Bayes rule and the classifier choice: maximum prior times likelihood.
- Conditional independence assumption; multinomial and binary variants.
- Training by counting class priors and word likelihoods; add-one or add-alpha smoothing.
- Evaluation: precision, recall, F-measure, macro and micro averaging, and the paired bootstrap test.

### Definitions to reproduce

The **prior** P(c) is the proportion of documents in class c. The **likelihood** P(w|c) is the probability of a word given the class. **Precision** is true positives divided by predicted positives. **Recall** is true positives divided by actual positives.

### Worked pattern

For a review, list the prior for each class, then the smoothed likelihood of each word. Compare in log space and report the predicted class. For evaluation, draw the confusion matrix first.

## Module 4 — Information retrieval and lexical resources

### Must know

- IR system design: indexing, stop-word removal, stemming, Zipf's law and inverted indexes.
- Classical models: Boolean, vector space and probabilistic.
- Term weighting with tf-idf; cosine similarity; document normalisation.
- Lexical resources: WordNet, FrameNet, stemmers, POS taggers and corpora.

### Definitions to reproduce

An **inverted index** maps each term to the documents containing it. **tf-idf** weights a term by its frequency in a document and its inverse document frequency. **Cosine similarity** is the cosine of the angle between query and document vectors. **WordNet** is a lexical database organised by synsets and semantic relations.

### Worked pattern

For tf-idf, build the term-document table, compute tf, compute idf as log(N/df), multiply, then normalise each document vector. For cosine similarity, take the dot product of the normalised vectors.

## Module 5 — Machine translation

### Must know

- Language divergence: word order, lexical, morphological and referential density.
- Encoder-decoder translation: encoder representation, decoder generation, cross-attention.
- Subword tokenisation: BPE, WordPiece and unigram.
- Parallel corpora, bitexts and sentence alignment.
- Evaluation: adequacy and fluency; human rating, post-editing, chrF and BLEU.
- Bias and ethical issues.

### Definitions to reproduce

**Machine translation** maps a source sentence to a target sentence. A **bitext** is a parallel text in two languages. **BPE** builds a shared subword vocabulary by merging frequent pairs. The **encoder** maps the source to hidden representations; the **decoder** generates target tokens. **Cross-attention** lets the decoder attend to encoder outputs. **BLEU** is precision-based n-gram overlap; **chrF** is character n-gram F-score.

### Worked pattern

For encoder-decoder, draw source tokens → encoder blocks → context representations → decoder with masked self-attention and cross-attention → target tokens. The decoder is autoregressive: each output token is conditioned on the source and the tokens already produced. Name one metric and one limitation, such as BLEU missing valid paraphrases.

## Last 24 hours

Revise the LFG notation, CYK table, edit-distance matrix, Naive Bayes formula and tf-idf/cosine steps. Rehearse one bigram calculation.

## Question bank

1. Model the role of transformational rules in transformational grammar with a suitable example. (4 marks)
2. Apply the annotated rules to generate the phrase structure and construct the f-structure for "I saw Abhishek in the market at night". (6 marks)
3. Make use of the different types of knowledge involved in language processing, with relevant real-world applications. (10 marks)
4. Summarise the challenges of processing natural language with suitable examples. (10 marks)
5. Illustrate X-bar theory with general phrase structure and sentential structure. (10 marks)
6. Apply the bigram model to calculate the probability of the phrase "Arabian knights are" for the given text. (10 marks)
7. Apply the CYK algorithm to parse "The sun rises in the east" and construct a table showing the parsing states; add suitable lexical rules. (10 marks)
8. Analyse the minimum edit distance algorithm and compute it for "flour" and "flower" with proper steps. (10 marks)

*Source: `NLP-IA1 Scheme.pdf`. `NLP IA2 SCHEME.pdf` is a scan with no usable text, so no IA2 question appears here; `NLP Module-01 N19.pdf` and `NLP notes.pdf` are also scans.*
