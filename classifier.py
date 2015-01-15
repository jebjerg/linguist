# -*- coding: utf-8 -*-
import data
from nltk.classify import NaiveBayesClassifier

letters = []  # REDACTED

chars = "".join(letters)


def features(text):
    return {k: k in text for k in chars}


def predict(text):
    return nb.classify(features(text))

nb = NaiveBayesClassifier.train([
    (features(l), k) for k, v in data.training_set.iteritems() for l in v
])
