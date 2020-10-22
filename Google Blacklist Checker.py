#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from googlesearch import search


# In[10]:


search_terms = ["Tim Pool", "Timcast"]#put terms to search for in this list
search_results = ["https://www.youtube.com/channel/UCG749Dj4V2fKa143f8sE60Q"]#put URLs to check for in this list
results_number = 10#put number of results to check per search term here


# In[19]:


def fullSearch():
    global search_terms
    global search_results
    global results_number
    output = "GOOGLE SEARCH BLACKLIST RESULT FILE\nTotal Score: {}\n"
    tmp = ""
    tmp_score = 0
    total_score = 0
    test = 1
    for i in search_terms:
        output = output + "Test " + str(test) + " (" + search_terms[test - 1] + "): "
        for j in search(i, num=results_number, stop=results_number, pause=2):
            tmp = tmp + j +"\n"
            for k in search_results:
                if j == k:
                    tmp_score += 1
        output = output + str(tmp_score) + "\n"
        output = output + tmp
        tmp = ""
        total_score += tmp_score
        score = 0
        test += 1
    return output.format(total_score)


# In[23]:


window = tk.Tk()
ent = tk.Text()
var = tk.StringVar()
var.set(fullSearch())
ent.insert(tk.END, var.get())
ent.pack()
window.mainloop()


# In[ ]:




