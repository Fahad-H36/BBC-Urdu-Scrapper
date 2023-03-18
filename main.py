# from Scraping import Scraping
import pandas as pd
from tkinter import *
from tkinter import messagebox
# from DataProcessing import DataProcessing
import pandas as pd
# from bs4 import BeautifulSoup
from statistics import mode
import numpy as np
import pandas
# import requests
from tkinter.ttk import *
import threading

# scraper = Scraping()

# df = scraper.ScrapeBBC()

# df.to_csv("D:/DS_Project2/data/finalResult.csv")
# def ScrapeBBC():
#     categories = ['cjgn7n9zzq7t', 'cw57v2pmll9t', 'c340q0p2585t', 'ckdxnx900n5t', 'c40379e2ymxt']
#
#     labels = []
#     stories = []
#     headlines = []
#
#     for category in categories:
#
#         print("Processing Category " + str(categories.index(category) + 1) + "...")
#         # messagebox.showinfo("Processing Category " + str(categories.index(category) + 1) + "...")
#
#         page_url = "https://www.bbc.com/urdu/topics/" + category + "/page/"
#
#         catHeadlines = []
#         catStories = []
#         catLabels = []
#
#         for i in np.arange(1, 100):
#             # page_url = page_url+str(i)
#             # print(page_url)
#             page = requests.get(str(page_url + str(i))).text
#
#             soup = BeautifulSoup(page, "lxml")
#
#             articles = soup.findAll("article",
#                                     attrs={'class': "qa-post gs-u-pb-alt+ lx-stream-post gs-u-pt-alt+ gs-u-align-left"})
#
#             # label1.config(text="Scraping Articles from page " + str(i) + "...")
#             print("Scraping Articles from page " + str(i) + "...")
#             label1.config(text="Scraping Articles from page " + str(i) + "...")
#             root.update_idletasks()
#
#             # messagebox.showinfo("Scraping Articles from page " + str(i) + "...")
#
#             for a in articles:
#                 # print("!!!")
#                 headline = a.find("span", attrs={'class': "lx-stream-post__header-text gs-u-align-middle"})
#                 # story = a.find("p", attrs={'class':"lx-stream-related-story--summary qa-story-summary"})
#                 # story = a.find("p", attrs={'class':"lx-stream-related-story--summary qa-story-summary"})
#
#                 # alternative "lx-stream-asset__gallery-cta-icon gel-icon"
#                 if not a.find('figure') and not a.find('div', attrs={
#                     'class': "lx-media-asset__image gs-o-responsive-image gs-o-responsive-image--16by9 qa-photogallery-image"}):
#                     anchor = a.find('a', href=True, attrs={'class': "qa-story-cta-link"})
#                     url = anchor['href']
#                     label = url.split('-')[0].split('/')[-1]
#                     label = label.capitalize()
#
#                     if (catLabels.count(label)) < 100:
#                         url = "https://www.bbc.com" + url
#
#                         fullStory = requests.get(url).text
#
#                         soup2 = BeautifulSoup(fullStory, 'lxml')
#
#                         story = soup2.findAll('div', attrs={'class': "bbc-4wucq3 e57qer20"})
#
#                         story = " ".join([str(a.getText()) for a in story])
#
#                         catHeadlines.append(headline.getText())
#                         catStories.append(story)
#                         catLabels.append(label)
#
#             if (catLabels.count(mode(catLabels)) >= 100):
#                 break
#         #
#         # catLabelslice = catLabels[-10:]
#         # catHeadlineslice = catHeadlines[-10:]
#         # storySlice = catStories[-10:]
#
#         print("Filtering Data...")
#         c = 0
#         for j in range(len(catLabels)):
#             if catLabels[j - c] != mode(catLabels):
#                 catLabels.pop(j - c)
#                 catStories.pop(j - c)
#                 catHeadlines.pop(j - c)
#                 c += 1
#
#         for entry in range(len(catLabels)):
#             labels.append(catLabels[entry])
#             stories.append(catStories[entry])
#             headlines.append(catHeadlines[entry])
#
#         progress['value'] = categories.index(category)+1*20
#         frame1.update_idletasks()
#         root.update_idletasks()
#         print(catLabels[-1] + " news Saved")
#
#         print("------------------------------------------------------")
#     # if len(catLabels) >=100:
#     # break
#
#     # print(catHeadlines)
#     # df = pd.DataFrame(catStories, catHeadlines)
#
#     # print(len(catLabels))
#
#     data_dict = {"Stories": stories, "Headlines": headlines, 'Labels': labels}
#     df = pandas.DataFrame(data_dict)
#
#
#     return df


def onClick():

    # button1.destroy()
    # root.update_idletasks()
    root.destroy()

    root1 = Tk()

    root1.resizable(0,0)

    root1.geometry("600x600")
    frame3 = LabelFrame(root1, text="Log", height=250, width=500)
    label1 = Label(frame3,text="Please Wait...")
    label1.place(x=55,y=90)

    progress = Progressbar(frame3, length=400, orient=HORIZONTAL, mode='determinate')
    progress.place(x=55, y=60)
    frame3.place(x=50,y=50)

    frame2 = LabelFrame(root1, text="Results", height=250, width=500)
    data = pd.read_csv("D:/DS_Project2/data/finalResult.csv")
    label2 = Label(frame2,text="Waiting for Data...")
    label2.place(x=5,y=50)

    frame2.place(x=50,y=320)

    # root.destroy()

    # root1.mainloop()
    def task():
        def ScrapeBBC():
            global result
            categories = ['cjgn7n9zzq7t', 'cw57v2pmll9t', 'c340q0p2585t', 'ckdxnx900n5t', 'c40379e2ymxt']

            labels = []
            stories = []
            headlines = []

            for category in categories:

                print("Processing Category " + str(categories.index(category) + 1) + "...")
                # messagebox.showinfo("Processing Category " + str(categories.index(category) + 1) + "...")

                # page_url = "https://www.bbc.com/urdu/topics/" + category + "/page/"
                page_url = 'http://'+str(result)+'topics/' + category + '/page/'

                catHeadlines = []
                catStories = []
                catLabels = []

                for i in np.arange(1, 100):
                    # page_url = page_url+str(i)
                    # print(page_url)
                    page = requests.get(str(page_url + str(i))).text

                    soup = BeautifulSoup(page, "lxml")

                    articles = soup.findAll("article",
                                            attrs={
                                                'class': "qa-post gs-u-pb-alt+ lx-stream-post gs-u-pt-alt+ gs-u-align-left"})

                    # label1.config(text="Scraping Articles from page " + str(i) + "...")
                    print("Scraping Articles from page " + str(i) + "...")
                    label1.config(text="Scraping Articles from page " + str(i) + "...")
                    label1.update_idletasks()
                    root.update_idletasks()

                    # messagebox.showinfo("Scraping Articles from page " + str(i) + "...")

                    for a in articles:
                        # print("!!!")
                        headline = a.find("span", attrs={'class': "lx-stream-post__header-text gs-u-align-middle"})
                        # story = a.find("p", attrs={'class':"lx-stream-related-story--summary qa-story-summary"})
                        # story = a.find("p", attrs={'class':"lx-stream-related-story--summary qa-story-summary"})

                        # alternative "lx-stream-asset__gallery-cta-icon gel-icon"
                        if not a.find('figure') and not a.find('div', attrs={
                            'class': "lx-media-asset__image gs-o-responsive-image gs-o-responsive-image--16by9 qa-photogallery-image"}):
                            anchor = a.find('a', href=True, attrs={'class': "qa-story-cta-link"})
                            url = anchor['href']
                            label = url.split('-')[0].split('/')[-1]
                            label = label.capitalize()

                            if (catLabels.count(label)) < 100:
                                url = "https://www.bbc.com" + url

                                fullStory = requests.get(url).text

                                soup2 = BeautifulSoup(fullStory, 'lxml')

                                story = soup2.findAll('div', attrs={'class': "bbc-4wucq3 e57qer20"})

                                story = " ".join([str(a.getText()) for a in story])

                                catHeadlines.append(headline.getText())
                                catStories.append(story)
                                catLabels.append(label)

                    if (catLabels.count(mode(catLabels)) >= 100):
                        break
                #
                # catLabelslice = catLabels[-10:]
                # catHeadlineslice = catHeadlines[-10:]
                # storySlice = catStories[-10:]

                print("Filtering Data...")
                c = 0
                for j in range(len(catLabels)):
                    if catLabels[j - c] != mode(catLabels):
                        catLabels.pop(j - c)
                        catStories.pop(j - c)
                        catHeadlines.pop(j - c)
                        c += 1

                for entry in range(len(catLabels)):
                    labels.append(catLabels[entry])
                    stories.append(catStories[entry])
                    headlines.append(catHeadlines[entry])

                progress['value'] += 20
                # (categories.index(category) + 1) * 40
                frame1.update_idletasks()
                root1.update_idletasks()
                print(catLabels[-1] + " news Saved")

                print("------------------------------------------------------")
            # if len(catLabels) >=100:
            # break

            # print(catHeadlines)
            # df = pd.DataFrame(catStories, catHeadlines)

            # print(len(catLabels))
            label1.config(text = "Scraping is Done.")
            frame1.update_idletasks()
            root1.update_idletasks()

            data_dict = {"Stories": stories, "Headlines": headlines, 'Labels': labels}
            df = pandas.DataFrame(data_dict)

            df.to_csv("D:/DS_Project2/data/data.csv")

            processer = DataProcessing()
            VocabSize, mostFrequentWords, labelCountDict, longShortStories = processer.processCSV("D:/DS_Project2/data/data.csv")



            processedData = [[
                "Vocabulary Size", VocabSize,],
                ["Most Frequent Words", list(mostFrequentWords.items())],
                ["Label Cound Dict", list(labelCountDict.items())],
                ["LongShortStories", [longShortStories['Longest Story'],longShortStories['Shortest Story']]]
            ]

            processedDataFrame = pd.DataFrame(processedData)
            processedDataFrame.to_csv("D:/DS_Project2/data/finalResult.csv")


            # messagebox.showinfo("Vocabulary Size = " + str(VocabSize))
            # label1.config(text="Vocabulary Size = " + str(VocabSize))

            label2.config(text="Vocab Size = " + str(VocabSize) + "\n Most Frequent Words are  " + str(list(mostFrequentWords.items()))+
                           "\n Label Count is " + str(list(labelCountDict.items())) + "\n Length of Longest Story = " +
                               str(longShortStories['Longest Story'][1]) +"\n Length of Longest Story = " + str(longShortStories['Shortest Story'][1]) )





        t1 = threading.Thread(target=ScrapeBBC)


        t1.start()
        root1.mainloop()
        t1.join()
        # df.to_csv("D:/DS_Project2/data/data.csv")


        # processer = DataProcessing()
        # VocabSize, mostFrequentWords, labelCountDict, longShortStories = processer.processCSV("D:/DS_Project2/data/data.csv")
        #
        #
        #
        # processedData = [[
        #     "Vocabulary Size", VocabSize,],
        #     ["Most Frequent Words", list(mostFrequentWords.items())],
        #     ["Label Cound Dict", list(labelCountDict.items())],
        #     ["LongShortStories", [longShortStories['Longest Story'],longShortStories['Shortest Story']]]
        # ]
        #
        # processedDataFrame = pd.DataFrame(processedData)
        # processedDataFrame.to_csv("D:/DS_Project2/data/finalResult.csv")
        #
        #
        # # messagebox.showinfo("Vocabulary Size = " + str(VocabSize))
        # # label1.config(text="Vocabulary Size = " + str(VocabSize))
        #
        # label2.config(text="Vocab Size = " + str(VocabSize) + "\n Most Frequent Words are  " + str(list(mostFrequentWords.items()[:5]))+"\n      "
        #                    +str(list(mostFrequentWords.items()[5:]))
        #               + "\n Label Count is " + str(list(labelCountDict.items())) + "\n Length of Longest Story = " +
        #                    str(longShortStories['Longest Story'][1]) +"\n Length of Longest Story = " + str(longShortStories['Shortest Story'][1]) )

    root1.after(2000, task)

    root1.mainloop()

    # root1.mainloop()

    # label1.config(text="vocabSize = " + str(VocabSize) + "\n Most frequent words = " + str(mostFrequentWords))
    # print("most Frequent Words: ")
    # print(mostFrequentWords)
    # print("label Count:")
    # print(labelCountDict)
    # print("longest Story: ")
    # print(longShortStories['Longest Story'])

    # print("Shortest Story: ")
    # print(longShortStories['Shortest Story'])




# root1 = Tk()

# progress = Progressbar(root1, orient=HORIZONTAL,
#                        length=150, mode='determinate')

# progress.pack()


result = ''
root = Tk()

root.resizable(0,0)
root.geometry("400x250")

# frame = Frame(root)
# frame.pack()
button1 = Button(root, text="Scrap", command=onClick)
button1.pack()
def save():
    global result
    result = text1.get("1.0", 'end-1c')
    print(result)
    return result

frame1 = LabelFrame(root, text="data", height=100, width=360)
# frame1.geometry('100x100')
text1 = Text(frame1, height=1, width=40)
text1.place(x=5, y=10)
button2 = Button(frame1, text='Save', command=save)
button2.place(x=130, y=40)





frame1.place(x=20,y=60)


# # button1.place(x=70, y=70)





root.mainloop()
# root1.mainloop()

# processedDataFrame = processedDataFrame.T

# processedDataFrame.to_csv("D:/DS_Project2/data/processedData.csv")

# print("vocabSize = " + str(VocabSize))
# print("most Frequent Words: ")
# print(mostFrequentWords)
# print("label Count:")
# print(labelCountDict)
# print("longest Story: ")
# print(longShortStories['Longest Story'])
#
# print("Shortest Story: ")
# print(longShortStories['Shortest Story'])


