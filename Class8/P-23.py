# Add an element to tuple and set to list

language = ['c','c++','Python']
language_tuple=('JAVA','COBOL')
language_set={'.NET','C#'}
language.append(language_tuple)
print("New Language List : ",language)
language.extend(language_set)
print("Newest Language List : ",language)