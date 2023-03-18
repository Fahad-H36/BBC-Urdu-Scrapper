# from tqdm import tqdm
from bs4 import BeautifulSoup
from statistics import mode
import numpy as np
import pandas
import requests
import os
import lxml




class Scraping:



	def ScrapeBBC(self):


		categories = ['cjgn7n9zzq7t', 'cw57v2pmll9t', 'c340q0p2585t', 'ckdxnx900n5t', 'c40379e2ymxt']

		labels = []
		stories = []
		headlines = []

		for category in categories:

			print("Processing Category "+str(categories.index(category)+1)+"...")
			page_url = "https://www.bbc.com/urdu/topics/"+category+"/page/"


			catHeadlines = []
			catStories = []
			catLabels = []


			for i in np.arange(1,100):
				# page_url = page_url+str(i)
				# print(page_url)
				page = requests.get(str(page_url+str(i))).text

				soup = BeautifulSoup(page, "lxml")

				articles = soup.findAll("article", attrs={'class': "qa-post gs-u-pb-alt+ lx-stream-post gs-u-pt-alt+ gs-u-align-left"})

				print("Scraping Articles from page "+str(i)+"...")
				for a in articles:
					# print("!!!")
					headline = a.find("span", attrs={'class':"lx-stream-post__header-text gs-u-align-middle"})
					# story = a.find("p", attrs={'class':"lx-stream-related-story--summary qa-story-summary"})
					# story = a.find("p", attrs={'class':"lx-stream-related-story--summary qa-story-summary"})



					# alternative "lx-stream-asset__gallery-cta-icon gel-icon"
					if not a.find('figure') and not a.find('div', attrs={'class':"lx-media-asset__image gs-o-responsive-image gs-o-responsive-image--16by9 qa-photogallery-image"}):
						anchor = a.find('a', href=True, attrs={'class':"qa-story-cta-link"})
						url = anchor['href']
						label = url.split('-')[0].split('/')[-1]
						label = label.capitalize()

						if(catLabels.count(label))<100:
							url = "https://www.bbc.com"+url


							fullStory = requests.get(url).text

							soup2 = BeautifulSoup(fullStory, 'lxml')

							story = soup2.findAll('div', attrs={'class':"bbc-4wucq3 e57qer20"})


							story = " ".join([str(a.getText()) for a in story])


							catHeadlines.append(headline.getText())
							catStories.append(story)
							catLabels.append(label)

				if(catLabels.count(mode(catLabels))>=100):
					break
				#
				# catLabelslice = catLabels[-10:]
				# catHeadlineslice = catHeadlines[-10:]
				# storySlice = catStories[-10:]


			print("Filtering Data...")
			c = 0
			for j in range(len(catLabels)):
				if catLabels[j-c] != mode(catLabels):
					catLabels.pop(j-c)
					catStories.pop(j-c)
					catHeadlines.pop(j-c)
					c+=1


			for entry in range(len(catLabels)):
				labels.append(catLabels[entry])
				stories.append(catStories[entry])
				headlines.append(catHeadlines[entry])

			print(catLabels[-1]+" news Saved")
			print("------------------------------------------------------")
			# if len(catLabels) >=100:
			# break

		# print(catHeadlines)
		# df = pd.DataFrame(catStories, catHeadlines)


		# print(len(catLabels))


		data_dict = {"Stories":stories, "Headlines":headlines, 'Labels':labels}
		df = pandas.DataFrame(data_dict)

		return df


# df.to_csv("D:/DS_Project2/data/finalResult.csv")

# print(catStories[1])
# print(catLabels)
# df.to_csv("D:/DS_Project2/data/results1.csv")
