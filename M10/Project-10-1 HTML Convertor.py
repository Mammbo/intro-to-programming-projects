#Project 10-1: HTML Convertor 
#Daniel Alvarez 
#3/12/24

def remove_html_tags(html):
    inside_tag = False
    result = ''
    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        else:
            if not inside_tag:
                result += char
              
    return result

path = 'groceries.html'
with open(path, 'r') as f: 
  html = f.read()
html_conversion = remove_html_tags(html).strip().replace(' ', '').replace("GroceryList", "Grocery List")
final_conversion = html_conversion.replace('\nE', '\n*E').replace('\nM', '\n*M').replace('\nB', '\n*B')

print("HTML Convertor\n")

print(final_conversion)