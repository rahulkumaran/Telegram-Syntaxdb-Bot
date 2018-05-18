import requests
import json

class Syntaxdb():
	def __init__(self, choice=0, search_query="",language=""):
		'''choice = 0 => concepts in any language'''
		'''choice = 1 => all concepts of particular language'''
		if(choice == 0):
			self.url = "https://syntaxdb.com/api/v1/concepts/search?q="+search_query
		else:
			self.url = "https://syntaxdb.com/api/v1/languages/"+language+"/concepts"

	def getResponse(self):
		'''Returns the reponse got from the url'''
		return requests.get(self.url)

	def getJson(self,response):
		'''Pass in the requests reponse and returns the json data'''
		return response.json()

	def getContent(self):
		'''Pass the json data and returns list'''
		'''if choice is concept, the summary will have only one item in list'''
		'''if choice is is 1, the summary will have multiple items in list'''
		response = self.getResponse()
		json_response = self.getJson(response)
		summary = []
		for data in json_response:
			concept = data['concept_search']
			syntax = data['syntax']
			description = data['description']
			notes = data['notes']
			example = data['example']
			summary+=["\nCONCEPT\n"+concept+"\n\nSYNTAX\n"+syntax+"\n\nDESCRIPTION\n"+ description+"\n\nNOTES\n"+notes+"\n\nEXAMPLE\n"+example]
		return summary

	def getAllConcepts(self):
		'''Pass the langauge and a list of all concepts are returned'''
		response = self.getResponse()
		json_response = self.getJson(response)
		return self.getContent(json_response)

