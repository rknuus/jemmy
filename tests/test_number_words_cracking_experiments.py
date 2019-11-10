# -*- coding: utf-8 -*-

import jemmy.vigenere

# based on http://www1.ids-mannheim.de/fileadmin/kl/derewo/DeReChar-v-uni-030-b-l-2018-02-28-1.0.html
GERMAN_LETTER_FREQUENCIES = {
    'A': 0.060067477706 + 0.005489485951,  # include ae
    'B': 0.021480751076,
    'C': 0.026900980520,
    'D': 0.047182137047,
    'E': 0.160061266048 + 0.005489485951 + 0.002698198599 + 0.006835955398,  # include umlauts
    'F': 0.018323709896,
    'G': 0.030642574549,
    'H': 0.042497859499,
    'I': 0.077526004178,
    'J': 0.002978121104,
    'K': 0.015368289907,
    'L': 0.037871919697,
    'M': 0.027983071757,
    'N': 0.096608077356,
    'O': 0.026841202334 + 0.002698198599,  # include oe
    'P': 0.010497044240,
    'Q': 0.000282903133,
    'R': 0.077377610953,
    'S': 0.063439603408 + 0.001706185925,  # include sharp s
    'T': 0.063693071514,
    'U': 0.038209944546 + 0.006835955398,  # include ue
    'V': 0.009188013866,
    'W': 0.014275418694,
    'X': 0.000517091308,
    'Y': 0.001079873609,
    'Z': 0.012376156182
}
GERMAN_LETTER_PRIORITY = [l for l in sorted(GERMAN_LETTER_FREQUENCIES, key=GERMAN_LETTER_FREQUENCIES.get, reverse=True)]
TOP_TWELVE_GERMAN_LETTERS = GERMAN_LETTER_PRIORITY[0:12]
TOP_TWELVE_GERMAN_FREQUENCY = sum(GERMAN_LETTER_FREQUENCIES[l] for l in TOP_TWELVE_GERMAN_LETTERS)
BOTTOM_NINE_GERMAN_FREQUENCY = sum(GERMAN_LETTER_FREQUENCIES[l] for l in GERMAN_LETTER_PRIORITY[-9:-1])

GERMAN_HIGH_FREQUENCY_COMBINATIONS = {
    'A': dict(),
    'B': dict(),
    'C': dict(),
    'D': dict(),
    'E': dict(),
    'F': dict(),
    'G': dict(),
    'H': dict(),
    'I': dict(),
    'J': dict(),
    'K': dict(),
    'L': dict(),
    'M': dict(),
    'N': dict(),
    'O': dict(),
    'P': dict(),
    'Q': dict(),
    'R': dict(),
    'S': dict(),
    'T': dict(),
    'U': dict(),
    'V': dict(),
    'W': dict(),
    'X': dict(),
    'Y': dict(),
    'Z': dict()
}
v = jemmy.vigenere.Vigenere([])
for key in TOP_TWELVE_GERMAN_LETTERS:
    for plain in TOP_TWELVE_GERMAN_LETTERS:
        GERMAN_HIGH_FREQUENCY_COMBINATIONS[key][plain] = v.decrypt(ciphertext=plain, key=key)

print('top high frequency combinations:')
message = ' \t'
for key in TOP_TWELVE_GERMAN_LETTERS:
    message += key + '\t'
message += '\n'
for plain in TOP_TWELVE_GERMAN_LETTERS:
    message += plain + '\t'
    for key in TOP_TWELVE_GERMAN_LETTERS:
        message += GERMAN_HIGH_FREQUENCY_COMBINATIONS[key][plain] + '\t'
    message += '\n'
print(message)

GERMAN_NUMBER_WORDS = [
  'EINS'
, 'ZWEI'
, 'ZWO'
, 'DREI'
, 'VIER'
, 'FÜNF'
, 'FUENF'
, 'SECHS'
, 'SIEBEN'
, 'ACHT'
, 'NEUN'
, 'ZEHN'
, 'ZWANZIG'
, 'DREISSIG'
, 'ZIG'
, 'SECHZIG'
, 'SIEBZIG'
, 'HUNDERT'
, 'TAUSEND'
, 'MILLION'
]  # TODO(KNR): consider to build a markov chain to define valid combinations


trigrams = set()
bigrams = set()
letters = set()
for word in GERMAN_NUMBER_WORDS:
    if len(word) < 3:
        continue
    start = 0
    while start < len(word)-2:
        trigram = word[start : start+3]
        trigrams.add(trigram)
        bigram = word[start : start+2]
        bigrams.add(bigram)
        start += 1
    bigram = word[start : start+2]
    bigrams.add(bigram)
    for letter in word:
        letters.add(letter)

trigrams = list(trigrams)
trigrams.sort()
print('trigrams:')
print(trigrams)

bigrams = list(bigrams)
bigrams.sort()
print('\nbigrams:')
print(bigrams)

letters = list(letters)
letters.sort()
print('\nletters:')
print(letters)