dictionary = {"href": "https://www.google.com", "target": "_blank"}

def props_to_html(self):
    sentence = ""
    for key, value in self.items():
        sentence += f" {key}=\"{value}\""
    print(sentence)

    

props_to_html(dictionary)