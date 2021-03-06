from gestion.elements_fichiers.section import Section

class Pays(Section):
	def __init__(self, num_pays, donnees):
		super().__init__(num_pays, donnees)
		
	def __lt__(self, autre_pays):
		return self.num_pays > autre_pays.num_pays

	def get_name(self):
		try:
			nom = self.contenu['Government']['Country name']['conventional short form']['text']
			if nom == 'none':
				raise KeyError
		except KeyError:
			try:
				nom = self.contenu['Government']['Country name']['conventional long form']['text']
			except KeyError:
				nom = None
		return nom

	def get_superficie(self):
		try:
			superficie = self.contenu['Geography']['Area']['total']['text']
		except KeyError:
			superficie = 'NA'
		return superficie

	def get_pop(self):
		try:
			pop = self.contenu['People and Society']['Population']['text']
		except KeyError:
			pop = 'NA'
		return pop

	def get_croissance_demo(self):
		try:
			croissance_demo = self.contenu['People and Society']['Population growth rate']['text']
		except KeyError:
			croissance_demo = 'NA'
		return croissance_demo

	def get_inflation(self):
		try:
			inflation = self.contenu['Economy']['Inflation rate (consumer prices)']['text']
		except KeyError:
			inflation = 'NA'
		return inflation

	def get_dette(self):
		try:
			dette = self.contenu['Economy']['Debt - external']['text']
		except KeyError:
			dette = 'NA'
		return dette

	def get_chomage(self):
		try:
			chomage = self.contenu['Economy']['Unemployment rate']['text']
		except KeyError:
			chomage = 'NA'
		return chomage

	def get_depenses_sante(self):
		try:
			depenses_sante = self.contenu['People and Society']['Health expenditures']['text']
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante

	def get_depenses_education(self):
		try:
			depenses_education = self.contenu['People and Society']['Education expenditures']['text']
		except KeyError:
			depenses_education = 'NA'
		return depenses_education

	def get_depenses_militaires(self):
		try:
			depenses_militaires = self.contenu['Military and Security']['Military expenditures']['text']
		except KeyError:
			depenses_militaires = 'NA'
		return depenses_militaires
	
	def get_classe_age1(self):
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["0-14 years"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_classe_age2(self):
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["15-24 years"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_classe_age3(self):
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["25-54 years"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_classe_age4(self):
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["55-64 years"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_classe_age5(self):
		try:
			depenses_sante = self.contenu['People and Society']['Age structure']["65 years and over"]["text"]
		except KeyError:
			depenses_sante = 'NA'
		return depenses_sante
	
	def get_critere(self, critere):
		if critere == 'superficie':
			txt = self.get_superficie()
		elif critere == 'population':
			txt = self.get_pop()
		elif critere == 'croissance démographique':
			txt = self.get_croissance_demo()
		elif critere == 'inflation':
			txt = self.get_inflation()   
		elif critere == 'dette':
			txt = self.get_dette()
		elif critere == 'chômage':
			txt = self.get_chomage()
		elif critere == 'dépenses santé':
			txt = self.get_depenses_sante()
		elif critere == 'dépenses éducation':
			txt = self.get_depenses_education()
		elif critere == 'dépenses militaires':
			txt = self.get_depenses_militaires()
		elif critere == '0-14':	
			txt = self.get_classe_age1()
		elif critere == '15-24':
			txt = self.get_classe_age2()
		elif critere == '25-54':
			txt = self.get_classe_age3()
		elif critere == '55-64':
			txt = self.get_classe_age4()
		elif critere == '>=65':
			txt = self.get_classe_age5()
		else:
			raise KeyError
		return txt

	def set_name(self, nom_pays):
		self.contenu.update({'Government' : {'Country name' : {'conventional short form' : {'text' : nom_pays}, 'conventional long form' : {'text' : nom_pays}}}})

	def set_long_name(self, long_name):
		self.contenu['Government']['Country name']['conventional long form'] = {'text' : long_name}

	def set_superficie(self, superficie):
		self.contenu.update({'Geography' : {'Area' : {'total' : {'text' : superficie+' sq km'}}}})

	def set_pop(self, pop):
		self.contenu.update({'People and Society' : {'Population' : {'text' : pop}}})

	def set_croissance_demo(self, croissance_demo):
		if 'People and Society' in self.contenu:
			self.contenu['People and Society']['Population growth rate'] = {'text' : croissance_demo+'%'}
		else:
			self.contenu['People and Society'] = {'Population growth rate' : {'text' : croissance_demo+'%'}}
		
	def set_inflation(self, inflation):
		self.contenu.update({'Economy' : {'Inflation rate (consumer prices)' : {'text' : inflation+'%'}}})
		
	def set_dette(self, dette):
		if 'Economy' in self.contenu:
			self.contenu['Economy']['Debt - external'] = {'text' : '$'+dette}
		else:
			self.contenu['Economy'] = {'Debt - external' : {'text' : '$'+dette}}
		
	def set_chomage(self, chomage):
		if 'Economy' in self.contenu:
			self.contenu['Economy']['Unemployment rate'] = {'text' : chomage+'%'}
		else:
			self.contenu['Economy'] = {'Unemployment rate' : {'text' : chomage+'%'}}
		
	def set_depenses_sante(self, depenses_sante):
		if 'People and Society' in self.contenu:
			self.contenu['People and Society']['Health expenditures'] = {'text' : depenses_sante+'% of GDP'}
		else:
			self.contenu['People and Society'] = {'Health expenditures' : {'text' : depenses_sante+'% of GDP'}}
		
	def set_depenses_education(self, depenses_education):
		if 'People and Society' in self.contenu:
			self.contenu['People and Society']['Education expenditures'] = {'text' : depenses_education+'% of GDP'}
		else:
			self.contenu['People and Society'] = {'Education expenditures' : {'text' : depenses_education+'% of GDP'}}
		
	def set_depenses_militaires(self, depenses_militaires):
		self.contenu.update({'Military and Security' : {'Military expenditures' : {'text' : depenses_militaires+'% of GDP'}}})

	def set_infos_de_base(self):
		ajout_infos = input('\nVoulez vous ajouter des informations de base sur le pays (O/N) ?\n> ')
		if ajout_infos in ["o","O"]:
			long_name = input("\nEntrez la version longue du nom du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if long_name != "pass":
				self.set_long_name(long_name)
				input("\nVotre réponse a bien été enregistrée")
			superficie = input("\nEntrez la superficie (en sq km) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if superficie != "pass":
				self.set_superficie(superficie)
				input("\nVotre réponse a bien été enregistrée")
			pop = input("\nEntrez la population du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if pop != "pass":
				self.set_pop(pop)
				input("\nVotre réponse a bien été enregistrée")
			croissance_demo = input("\nEntrez le taux de croissance démographique (en %) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if croissance_demo != "pass":
				self.set_croissance_demo(croissance_demo)
				input("\nVotre réponse a bien été enregistrée")
			inflation = input("\nEntrez le taux d'inflation (en %) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if inflation != "pass":
				self.set_inflation(inflation)
				input("\nVotre réponse a bien été enregistrée")
			dette = input("\nEntrez la dette (en $) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if dette != "pass":
				self.set_dette(dette)
				input("\nVotre réponse a bien été enregistrée")
			chomage = input("\nEntrez le taux de chômage (en %) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if chomage != "pass":
				self.set_chomage(chomage)
				input("\nVotre réponse a bien été enregistrée")
			depenses_sante = input("\nEntrez le taux de dépense en santé (en % of GDP) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if depenses_sante != "pass":
				self.set_depenses_sante(depenses_sante)
				input("\nVotre réponse a bien été enregistrée")
			depenses_education = input("\nEntrez le taux de dépense en éducation (en % of GDP) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if depenses_education != "pass":
				self.set_depenses_education(depenses_education)
				input("\nVotre réponse a bien été enregistrée")
			depenses_militaires = input("\nEntrez le taux de dépense militaires (en % of GDP) du pays.\nVous pouvez taper 'pass' pour passer la question.\n> ")
			if depenses_militaires != "pass":
				self.set_depenses_militaires(depenses_militaires)
				input("\nVotre réponse a bien été enregistrée")
