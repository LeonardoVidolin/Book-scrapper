# coding: utf-8

# ## Import Libraries

# In[16]:


get_ipython().system('pip install selenium')


# In[2]:


get_ipython().system('pip install requests')


# In[38]:


import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time


# ## Get URL and send GET request

# In[39]:


url = "https://books.toscrape.com/"

response = requests.get(url) # Obter resposta do HTML
if response.status_code == 200: # Verificar se funcionou
    print("Sucesso")
else:
    print("Falha")


# ## Parse the HTLM Content

# In[40]:


# Criar um objeto SOUP para salvar o HTML
soup = BeautifulSoup(response.text, "html.parser") 
print(soup)


# ## Find books on page 1

# In[36]:


# Encontrar os livros na pagina 1
books = soup.find_all('h3')

start_time = time.time()
books_extracted = 0

# Percorrer por todos os livros e pegar os titulos
for book in books:
    book_url = book.find('a')['href']
    book_response = requests.get(url+book_url)
    book_soup = BeautifulSoup(book_response.content, "html.parser")
    
    title = book_soup.find('h1').text
    category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
    rating = book_soup.find('p', class_='star-rating')['class'][1]
    price = book_soup.find('p', class_='price_color').text.strip()
    
    books_extracted += 1
    
    end_time = time.time()
    total_time = (end_time-start_time)/60.0
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Available: {stock}")
    print('*********')


# ## Find books on all pages

# In[42]:


# Create a list to hold all the books
books_data = []
# loop
for page_num in range(1,51):
    url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = soup.find_all('h3')

    start_time = time.time()
    books_extracted = 0
    
    for book in books:
        book_url = book.find('a')['href']
        book_response = requests.get('http://books.toscrape.com/catalogue/'+book_url)
        book_soup = BeautifulSoup(book_response.content, "html.parser")

        title = book_soup.find('h1').text
        category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()
        rating = book_soup.find('p', class_='star-rating')['class'][1]
        price = book_soup.find('p', class_='price_color').text.strip()
        availability = book_soup.find('p', class_='availability').text.strip()

        end_time = time.time()
        total_time = (end_time-start_time)/60.0

        books_data.append([title, category, rating, price, availability])
        print(books_data)
        print('*******')
        print(f'total time: {total_time:.2f} minutes')
        print('*******')
        print(f'{page_num * len(books)} Books extrated so far...')
    
# Add extracted info to the list


# ## Export the data

# In[43]:


# Converter para DataFrame
df = pd.DataFrame(books_data, columns=['Title','Category','Rating','Price','Availability'])
#Display first 10 rows
print(df.head(10))


# In[50]:


#save data to csv
df.to_csv(r'C:\Users\Leonardo\Downloads\teste\books_scraped.csv',index=False, sep=';')
print("data saved")


# In[ ]:




