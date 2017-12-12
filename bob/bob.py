import re


def hey(phrase):
    phrase = phrase.strip()
    if phrase.isupper():
        return "Whoa, chill out!"
    elif re.search(r'\?$', phrase):
        return "Sure."
    elif phrase.isspace() or not phrase:
        return "Fine. Be that way!"
    else:
        return "Whatever."

# Bob

#Bob is a lackadaisical teenager. In conversation, his responses are very limited.

#Bob answers 'Sure.' if you ask him a question.

#He answers 'Whoa, chill out!' if you yell at him.

#He says 'Fine. Be that way!' if you address him without actually saying
#anything.

#He answers 'Whatever.' to anything else.