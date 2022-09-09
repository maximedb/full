import pytest
from collections import Counter
from full import FULL


def test_evaluate_turn():
    """ Test the evaluation returns the correct number """
    model = FULL()
    conversation = [
        'Hi!', 
        "Hi! What's up?", 
        'Nothing much, how about you', 
        'Not much either.', 
        'What are you doing', 
        'Playing Terraria. What about you?', 
        'Sitting in a meeting', 
        'What kind of meeting?', 
        "Can't say"
    ]
    response = "It's probably boring, isn't it?"
    evaluation = model.evaluate_turn(conversation, response)
    assert evaluation == pytest.approx(27.56904637813568)


def test_evaluate_dialog():
    """ Test the evaluation returns the correct number """
    model = FULL()
    conversation = [
        'Hi!', 
        "Hi! What's up?", 
        'Nothing much, how about you', 
        'Not much either.', 
        'What are you doing', 
        'Playing Terraria. What about you?', 
        'Sitting in a meeting', 
        'What kind of meeting?', 
        "Can't say"
    ]
    evaluation = model.evaluate_dialog(conversation)
    assert evaluation == pytest.approx(31.083410263061523)