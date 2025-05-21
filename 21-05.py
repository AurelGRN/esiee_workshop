class dog:
    def __init__(self, color, eye_color, height, lenght, weight):
        self.color = color
        self.eye_color = eye_color
        self.height = height
        self.lenght = lenght
        self.weight = weight

    def sit(self):
        print("the dog sits")
    
    def lay_down(self):
        print("the dog lay downs")

    def shake(self):
        print("the dog shake")

    def come(self):
        print("the dog come next to you")

class cat:
    def __init__(self, color, eye_color, height, lenght, weight):
        self.color = color
        self.eye_color = eye_color
        self.height = height
        self.lenght = lenght
        self.weight = weight

John = dog("red","green", 10,12,15)
Didi = cat("puple","brown", 25,22,30)

