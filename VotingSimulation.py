loop=0
while(loop!=100):
	loop+=1
	import matplotlib.pyplot as plt
	dataFile= open("output2.csv", 'a')
	dataFile.write("Total Amount of People,	Election Cycle Number,	Total Happiness,	Winner,	Tie or Not \n")  #Header
	import random as rand
	import time
	import numpy as np
	def Run(TimesRan,PersonCounter,Choices,Happy,happy,TimesRun):
		tieFlag = False
		Candidate1=0
		Candidate2=0
		Candidate3=0
		Candidate4=0
		Candidate5=0
		CandidateNumber=""
		if(Choices==[]*PersonCounter):
			Random=rand.triangular(.5,5.5)
			Random=round(Random,1)
			arraylimit=PersonCounter
			arrayelement=0
			while(arraylimit>0):
				Random=rand.uniform(.5,5.5)
				Random=round(Random,1)
				Choices.append(Random)
				arraylimit-=1
			arraylimit=PersonCounter
			# ~ #print("What's Next?")
		else:
			Choices=Choices
			# ~ #print(Choices)
			arrayelement=0
		while((Candidate1+Candidate2+Candidate3+Candidate4+Candidate5)!=PersonCounter):
			(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)=FPTP(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,Choices,arrayelement)
			arrayelement=arrayelement+1
		#print(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)
		if((Candidate1>Candidate2) and (Candidate1>Candidate3) and (Candidate1>Candidate4) and (Candidate1>Candidate5)):
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Happy=Happiness(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,CandidateNumber)
				arrayelement+=1		
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Choices=Choice(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,arrayelement)
				arrayelement+=1
			# ~ print("Winner is Candidate 1 with a total happiness of " + str(Happy))
			CandidateNumber=("Winner is Candidate 1")
			CandidateNumber=CandidateNumber[-1]
		elif((Candidate2>Candidate1) and (Candidate2>Candidate3) and (Candidate2>Candidate4) and (Candidate2>Candidate5)):
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Happy=Happiness(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,CandidateNumber)
				arrayelement+=1
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Choices=Choice(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,arrayelement)
				arrayelement+=1
			# ~ print("Winner is Candidate 2 with a total happiness of " + str(Happy))
			CandidateNumber=("Winner is Candidate 2")
			CandidateNumber=CandidateNumber[-1]
		elif((Candidate3>Candidate1) and (Candidate3>Candidate2) and (Candidate3>Candidate4) and (Candidate3>Candidate5)):
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Happy=Happiness(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,CandidateNumber)
				arrayelement+=1
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Choices=Choice(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,arrayelement)
				arrayelement+=1
			# ~ print("Winner is Candidate 3 with a total happiness of " + str(Happy))
			CandidateNumber=("Winner is Candidate 3")
			CandidateNumber=CandidateNumber[-1]
		elif((Candidate4>Candidate1) and (Candidate4>Candidate2) and (Candidate4>Candidate3) and (Candidate4>Candidate5)):
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Happy=Happiness(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,CandidateNumber)
				arrayelement+=1
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Choices=Choice(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,arrayelement)
				arrayelement+=1
			# ~ print("Winner is Candidate 4 with a total happiness of " + str(Happy))
			CandidateNumber=("Winner is Candidate 4")
			CandidateNumber=CandidateNumber[-1]
		elif((Candidate5>Candidate1) and (Candidate5>Candidate2) and (Candidate5>Candidate3) and (Candidate5>Candidate4)):
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Happy=Happiness(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,CandidateNumber)
				arrayelement+=1
			arrayelement=0
			while(arrayelement!=PersonCounter-1):
				Choices=Choice(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,arrayelement)
				arrayelement+=1
			# ~ print("Winner is Candidate 5 with a total happiness of " + str(Happy))
			CandidateNumber=("Winner is Candidate 5")
			CandidateNumber=CandidateNumber[-1]
		elif(((Candidate1==Candidate2)and(Candidate1==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate1==Candidate3)and(Candidate1==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate1==Candidate4)and(Candidate1==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate1==Candidate5)and(Candidate1==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate2==Candidate3)and(Candidate2==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate2==Candidate4)and(Candidate2==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate2==Candidate5)and(Candidate2==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate3==Candidate4)and(Candidate3==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate3==Candidate5)and(Candidate3==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))) or ((Candidate4==Candidate5)and(Candidate4==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)))):
			arrayelement=0
			# ~ print("There was a tie for first place.")
			canddict = {'names' : ['Candidate 1','Candidate 2','Candidate 3','Candidate 4','Candidate 5'],
						'votes' : np.array([Candidate1, Candidate2, Candidate3, Candidate4, Candidate5])}
			maxVotes=np.amax(canddict['votes'])
			ind = canddict['votes']==maxVotes
			tieCheck = np.array(range(5))
			tieCheck = tieCheck[ind]
			if( len(ind)>1):
				winInd=np.random.choice(tieCheck)
				tieFlag = True
			CandidateNumber=canddict['names'][winInd]
			CandidateNumber=CandidateNumber[-1]
			while(arrayelement!=PersonCounter-1):
				Choices=Choice(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,arrayelement)
				# ~ (Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)=FPTP(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,Choices,arrayelement)
				arrayelement+=1
			Happy=Happiness(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,CandidateNumber)
			# ~ print('Winner is '+str(canddict['names'][winInd])+ " with a total happiness of "+str(Happy))
		# ~ outstr = TimesRan + ", " + Happy + ", " + CandidateNumber + ", " + tieFlag
		dataFile.write('{}, {}, {}, {}, {}\n' .format(PersonCounter, TimesRan, Happy, CandidateNumber, tieFlag))
		people=PersonCounter
		# ~ happy=Happy/people
		happy=arrayofhappy(Happy,people,TimesRan,TimesRun)
		return(TimesRan)
	def arrayofhappy(Happy,people,TimesRan,TimesRun):
		values=Happy/people
		happy.append(values)
		# ~ print(happy)
		return(happy)
	def FPTP(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,Choices,arrayelement):
		Vote=Choices[arrayelement]
		if (Vote<=1.5):
			Candidate1+=1
		elif (Vote<=2.5):
			Candidate2=Candidate2+1
		elif (Vote<=3.5):
			Candidate3+=1
		elif (Vote<=4.5):
			Candidate4+=1
		elif (Vote<=5.5):
			Candidate5+=1
		# ~ #print(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)
		return(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)
	def Choice(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,arrayelement):
		Vote=Choices[arrayelement]
		if((Candidate1>Candidate2) and (Candidate1>Candidate3) and (Candidate1>Candidate4) and (Candidate1>Candidate5)):
			# ~ Vote=Choices[arrayelement]
			if (Vote<=1.5):
				Vote=int(rand.choice("121"))
			elif (Vote<=2.5):
				Vote=Vote+.1
			elif (Vote<=3.5):
				Vote=int(rand.choice("243"))
			elif (Vote<=4.5):
				Vote=Vote-.1
			elif (Vote<=5.5):
				Vote=Vote-.1
			# ~ Choices.pop(arrayelement)
			# ~ Vote=round(Vote,1)
			# ~ if(Vote>5.5):
				# ~ Vote=5.5
			# ~ elif(Vote<.5):
				# ~ Vote=.5
			# ~ Choices.append(Vote)
		elif((Candidate2>Candidate1) and (Candidate2>Candidate3) and (Candidate2>Candidate4) and (Candidate2>Candidate5)):
			# ~ Vote=Choices[arrayelement]
			if (Vote<=1.5):
				Vote=Vote+.1
			elif (Vote<=2.5):
				Vote=int(rand.choice("1232"))
			elif (Vote<=3.5):
				Vote=Vote+.1
			elif (Vote<=4.5):
				Vote=int(rand.choice("354"))
			elif (Vote<=5.5):
				Vote=Vote-.1
			# ~ Choices.pop(arrayelement)
			# ~ Vote=round(Vote,1)
			# ~ if(Vote>5.5):
				# ~ Vote=5.5
			# ~ elif(Vote<.5):
				# ~ Vote=.5
			# ~ Choices.append(Vote)
		elif((Candidate3>Candidate1) and (Candidate3>Candidate2) and (Candidate3>Candidate4) and (Candidate3>Candidate5)):
			# ~ Vote=Choices[arrayelement]
			if (Vote<=1.5):
				Vote=Vote-.1
			elif (Vote<=2.5):
				Vote=int(rand.choice("132"))
			elif (Vote<=3.5):
				Vote=int(rand.choice("2334"))
			elif (Vote<=4.5):
				Vote=int(rand.choice("345"))
			elif (Vote<=5.5):
				Vote=Vote-.1
			# ~ Choices.pop(arrayelement)
			# ~ Vote=round(Vote,1)
			# ~ if(Vote>5.5):
				# ~ Vote=5.5
			# ~ elif(Vote<.5):
				# ~ Vote=.5
			# ~ Choices.append(Vote)
		elif((Candidate4>Candidate1) and (Candidate4>Candidate2) and (Candidate4>Candidate3) and (Candidate4>Candidate5)):
			# ~ Vote=Choices[arrayelement]
			if (Vote<=1.5):
				Vote=Vote-.1
			elif (Vote<=2.5):
				Vote=int(rand.choice("123"))
			elif (Vote<=3.5):
				Vote=Vote+.1
			elif (Vote<=4.5):
				Vote=int(rand.choice("5443"))
			elif (Vote<=5.5):
				Vote=Vote+.1
			# ~ Choices.pop(arrayelement)
			# ~ Vote=round(Vote,1)
			# ~ if(Vote>5.5):
				# ~ Vote=5.5
			# ~ elif(Vote<.5):
				# ~ Vote=.5
			# ~ Choices.append(Vote)
		elif((Candidate5>Candidate1) and (Candidate5>Candidate2) and (Candidate5>Candidate3) and (Candidate5>Candidate4)):
			# ~ Vote=Choices[arrayelement]
			if (Vote<=1.5):
				Vote=Vote-.1
			elif (Vote<=2.5):
				Vote=Vote-.1
			elif (Vote<=3.5):
				Vote=int(rand.choice("234"))
			elif (Vote<=4.5):
				Vote=Vote+.1
			elif (Vote<=5.5):
				Vote=int(rand.choice("455"))
			# ~ Choices.pop(arrayelement)
			# ~ Vote=round(Vote,1)
			# ~ if(Vote>5.5):
				# ~ Vote=5.5
			# ~ elif(Vote<.5):
				# ~ Vote=.5
			# ~ Choices.append(Vote)
		elif((Candidate1==Candidate2) or (Candidate1==Candidate3) or (Candidate1==Candidate4) or (Candidate1==Candidate5) or (Candidate2==Candidate3) or (Candidate2==Candidate4) or (Candidate2==Candidate5) or (Candidate3==Candidate4) or (Candidate3==Candidate5) or (Candidate4==Candidate5)):
			# ~ Vote=Choices[arrayelement]
			if(Vote<=1.5):
				Vote=int(rand.choice("11122"))
			elif(Vote<=2.5):
				Vote=int(rand.choice("12223"))
			elif(Vote<=3.5):
				Vote=int(rand.choice("23334"))
			elif(Vote<=4.5):
				Vote=int(rand.choice("34445"))
			elif(Vote<=5.5):
				Vote=int(rand.choice("44555"))
			Choices.pop(arrayelement)
			Choices.append(Vote)
			return(Choices)
		Choices.pop(arrayelement)
		Vote=round(Vote,1)
		if(Vote>5.5):
			Vote=5.5
		elif(Vote<.5):
			Vote=.5
		Choices.append(Vote)
		return(Choices)
	def Happiness(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5,CandidateNumber):
		if(CandidateNumber==""):
			if((Candidate1==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate2!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate3!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate4!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate5!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))):
				Happy=((Candidate1*3)+(Candidate2)-((Candidate4)+(Candidate5*4)))
			elif((Candidate2==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate1!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate3!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate4!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate5!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))):
				Happy=((Candidate2*3)+(Candidate1+Candidate3)-(Candidate5))
			elif((Candidate3==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate2!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate1!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate4!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate5!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))):
				Happy=((Candidate3*3)+(Candidate4+Candidate2))
			elif((Candidate4==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate2!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate3!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate1!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate5!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))):
				Happy=((Candidate4*3)+(Candidate5+Candidate3)-(Candidate1))
			elif((Candidate5==max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate2!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate3!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate4!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5)) and (Candidate1!=max(Candidate1,Candidate2,Candidate3,Candidate4,Candidate5))):
				Happy=((Candidate5*3)+(Candidate4)-((Candidate2)+(Candidate1*4)))
		else:
			if(CandidateNumber=="1"):
				Happy=((Candidate1*3)+(Candidate2)-((Candidate4)+(Candidate5*4)))
			elif(CandidateNumber=="2"):
				Happy=((Candidate2*3)+(Candidate1+Candidate3)-(Candidate5))
			elif(CandidateNumber=="3"):
				Happy=((Candidate3*3)+(Candidate2+Candidate4))
			elif(CandidateNumber=="4"):
				Happy=((Candidate4*3)+(Candidate3+Candidate5)-(Candidate1))
			elif(CandidateNumber=="5"):
				Happy=((Candidate5*3)+(Candidate4)-((Candidate2)+(Candidate1*4)))
		return(Happy)
	# ~ print("What is the highest amount of elections you want to run with upto 100 people?")
	# ~ high=int(input())
	TimesRun=rand.randint(2,100)
	TimesRan=TimesRun
	PersonCounter=rand.randint(2,100)
	Choices=[]*PersonCounter
	happy=[]*PersonCounter
	while(TimesRan>0):
		Happy=0
		# ~ print(TimesRan)
		TimesRan=Run(TimesRan,PersonCounter,Choices,Happy,happy,TimesRun)
		TimesRan-=1
	dataFile.write("\n\n")
	dataFile.close()
	plt.plot(happy)
	plt.close()
	plt.show()
	print("Looped "+str(loop)+" Times")
