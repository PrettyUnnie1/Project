# SampleListenerImpl.py
from CompiledFiles.SampleListener import SampleListener

class SampleListenerImpl(SampleListener):
    def __init__(self):
        self.positive = False
        self.negative = False

    def enterWord(self, ctx):
        if ctx.POSITIVE():
            self.positive = True
        elif ctx.NEGATIVE():
            self.negative = True

    def get_sentiment(self):
        if self.positive and not self.negative:
            return "Positive"
        elif self.negative and not self.positive:
            return "Negative"
        elif self.positive and self.negative:
            return "Mixed"
        else:
            return "Neutral"

    def reset(self):
        """Resets the sentiment flags."""
        self.positive = False
        self.negative = False
