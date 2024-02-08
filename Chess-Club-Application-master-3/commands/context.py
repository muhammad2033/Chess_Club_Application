class Context:
    """
    Represents a 'context' for the application.

    The context contains:
    - a screen 'name'
    - arguments
    - a boolean controlling whether the application should stop running
    """

    def __init__(self, screen=None, run=True, **kwargs):
        self.screen = screen
        self.run = run
        self.kwargs = kwargs

    def set_args(self, **kwargs):
        """Syntactic sugar to set the kwargs attribute using dictionary unpacking"""
        self.kwargs = kwargs

    def __str__(self):
        return f"<Context: {self.screen} | {self.kwargs}>"
