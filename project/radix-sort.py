import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radixSort(ar, length, at):
  times = 127*[None]
  final_array = len[ar] * [None]

  for i in ar:
    temp = 0
    if (length-len(i)+at) < 0:
      temp = i[at+length]+1
    times[temp] = times[temp]+1

  for j in range(len(times)-1):
    times[j+1] = times[j+1]+times[j]
  
  
  for k in range(len(ar)-1, -1, -1):
    temp1 = 0
    if (at+length-len(ar[k])) < 0:
      temp1 = ar[k][at+length]+1
    final_array[times[temp1]-1] = ar[k]
    times[temp1] = times[temp1]-1

  return final_array

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
  final_book = book_to_words(book_url)  
  maxLength = 0
  for i in final_book:
    if len(i)>=maxLength:
      maxLength = len(i)
  
  atEnd = -1
  while atEnd+maxLength>-1:
    final_book = radixSort(final_book, maxLength, atEnd)
    atEnd = atEnd-1
  for l in final_book:
    yield l.decode("ascii")
