import wikipedia
query=input()
alphabets=[]
b=[]
result=wikipedia.WikipediaPage(query)
no_of_letters=0
a=result.content
print(a)
