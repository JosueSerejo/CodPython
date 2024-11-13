
animals = {

('vertebrado', 'ave', 'carnivoro'): 'aguia',
('vertebrado', 'ave', 'onivoro'): 'pomba',
('vertebrado', 'mamifero', 'onivoro'): 'homem',
('vertebrado', 'mamifero', 'herbivoro'): 'vaca',
('invertebrado', 'inseto', 'hematofago'): 'pulga',
('invertebrado', 'inseto', 'herbivoro'): 'lagarta',
('invertebrado', 'anelideo', 'hematofago'): 'sanguessuga',
('invertebrado', 'anelideo', 'onivoro'): 'minhoca',

}

WordOne = input().strip()
WordTwo = input().strip()
WordThree = input().strip()

print(animals[(WordOne, WordTwo, WordThree)])