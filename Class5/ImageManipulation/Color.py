class Color(object):
    r = 0;
    g = 0;
    b = 0;

    def __init__(self, red = 0, green=0, blue=0):
        self.r = red;
        self.g = green;
        self.b = blue;

    def __str__(self):
        return "{} {} {} ".format(self.r, self.g, self.b);
