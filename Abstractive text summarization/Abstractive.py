from transformers import pipeline
from bs4 import BeautifulSoup
import requests
import anvil.server
from bs4 import BeautifulSoup
import requests
import pdfplumber
import docx2txt
summarizer = pipeline("summarization")
anvil.server.connect('U5ZALWW3SL2TBJHC6BYXFCSL-7Q36I7VBIV4PEZDG')
@anvil.server.callable
def abstractive_summmary(user_input,percentage):
  max_chunk = 500
  user_input = user_input.replace('.', '.<eos>')
  user_input = user_input.replace('?', '?<eos>')
  user_input = user_input.replace('!', '!<eos>')
  sentences = user_input.split('<eos>')
  words = len(user_input.split(' '))
  current_chunk = 0 
  chunks = []

  for sentence in sentences:
    if len(chunks) == current_chunk + 1: 
        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
            chunks[current_chunk].extend(sentence.split(' '))
        else:
            current_chunk += 1
            chunks.append(sentence.split(' '))
    else:
        chunks.append(sentence.split(' '))

  for chunk_id in range(len(chunks)):
    chunks[chunk_id] = ' '.join(chunks[chunk_id])
  res = summarizer(chunks, max_length=words//len(chunks) , min_length=(words*percentage//100)//len(chunks), do_sample=False)
  text = ' '.join([summ['summary_text'] for summ in res])
  result = [text,len(user_input.split(' ')),len(text.split(' '))]
  return result
@anvil.server.callable
def web_page_summary(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  results = soup.find_all('p')
  text = [result.text for result in results]
  user_input = ' '.join(text)
  return user_input
@anvil.server.callable
def docx(media,a):
  with open(f"/tmp/{a}", "wb") as f:
      f.write(media.get_bytes())
  txt_file = docx2txt.process(f"/tmp/{a}")
  txt_file = txt_file.replace('\n','')  
  return txt_file
@anvil.server.callable
def pdf(media,a):
  with open(f"/tmp/{a}", "wb") as f:
      f.write(media.get_bytes())
  text = ""
  with pdfplumber.open(f"/tmp/{a}") as pdf:
    no_of_pages = len(pdf.pages)
    for i in range(no_of_pages):
      content = pdf.pages[i].extract_text()
      text += content
      text = text.replace("\n"," ")
    return text

