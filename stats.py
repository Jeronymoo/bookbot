def get_num_words(text):
  num_words = len(text.split())
  return num_words

def count_characters(text):
  my_dict = {}
  for i in text.lower():
    if str(i) not in my_dict:
      my_dict[str(i)] = 1
    else:
      my_dict[str(i)] += 1  
  return my_dict

def sort_on(d):
  return d["amount"]

def sort_dict(my_dict):
  lista = []
  for k, v in my_dict.items():
    lista.append({"char": k, "amount": v})
  lista.sort(reverse=True, key=sort_on)
  return lista