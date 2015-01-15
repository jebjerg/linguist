# -*- coding: utf-8 -*-
from classifier import nb, predict
import os
PROMPT = os.getenv("PROMPT", "linguist # ")

if __name__ == "__main__":
    while True:
        try:
            text = raw_input(PROMPT)
        except EOFError:
            print "Exit"
            break
        except Exception as e:
            print("Error: {0:s}".format(e))
            break
        if text in ["stats", "info", "debug"]:
            print nb.most_informative_features()
        elif text in ["", "\r\n", "\n"]:
            pass
        else:
            print("{0:s} -> {1:s}".format(text, predict(text)))
