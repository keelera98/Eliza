import string
import re
import random

user_response = raw_input("Eliza: Hello I'm Eliza, how are you?\n")
eliza_response = ""
store = []

def cleanse(resp):
	answer = re.sub('[^A-Za-z0-9]+', ' ', resp)
	return answer.lower()

def find_word(word, s):
	return (' ' + word + ' ') in (' ' + s + ' ')

while True:

	clean_resp = cleanse(user_response)	

	random_phrase = random.randint(1,3)

	if(clean_resp.split(' ', 1)[0] == "yes"):
		print "Eliza: Are you certain?"
	elif (find_word("i", clean_resp) and find_word("am", clean_resp) or find_word("m", clean_resp)):
		word_list = clean_resp.split()
		if ("am" in word_list[-1] or "m" in word_list[-1] or "am." in word_list[-1]):
			print "Eliza: Why do you say that?"
		else:
			if (find_word("m", clean_resp)):	
				ran = random.randint(1,3)
				im_split = clean_resp.split("m")
				if(ran == 1):
					answer = "Did you come to me because your" + im_split[-1]
				else:
					answer = "Why do you say your" + im_split[-1]	
					#answer = clean_resp.replace("i m", "Why do you say your")
				store_sentence = clean_resp.split()
				store.insert(0, store_sentence[-1])
				print "Eliza: " + answer + "?"
			else:
				im_split = clean_resp.split("am")
				ran = random.randint(1,3)
				if(ran == 1):
					#answer = clean_resp.replace("i am", "Did you come to me because your")
					answer = "Did you come to me because your" + im_split[-1]
				else:
					#answer = clean_resp.replace("i am", "Why do you say your")
					answer = "Why do you say your" + im_split[-1]	
				store_sentence = clean_resp.split()
				store.insert(0, store_sentence[-1])
				print "Eliza: " + answer + "?"
	elif (find_word("no", clean_resp)):
		print "Eliza: You sound positive."
	elif (find_word("your", clean_resp)):
		splitted = clean_resp.split("your")
		print "Eliza: Why are concerned about my" + splitted[1] + "?"
	elif (find_word("perhaps", clean_resp) or find_word("maybe", clean_resp)):
		print "Eliza: Why the uncertain tone?"
	elif (find_word("you", clean_resp)):
		if(random_phrase == 1):
			print "Eliza: We are talking about you not me."
		else:
			print "Eliza: You're not really talking about me are you?"
	elif (find_word("sorry", clean_resp)):
		if(random_phrase == 1):
			print "Eliza: Please don't apologize."
		else:
			print "Eliza: Apologies are not necessary."
	elif (find_word("you", clean_resp) and find_word("are", clean_resp)):
		store_sen = clean_resp.split()
		if (random_phrase == 1):
			print "Eliza: Why are you interested in whether or not I am " + store_sen[-1] + "?"
		else:
			print "Eliza: What makes you think I'm " + store_sen[-1] + "?"
	elif (find_word("mother", clean_resp) or find_word("father", clean_resp) or find_word("brother", clean_resp) or find_word("sister", clean_resp)):
		print "Eliza: Tell me more about your family."
	elif (find_word("you", clean_resp) and find_word("are", clean_resp) and find_word("like", clean_resp)):
		print "Eliza: What resemblance do you see?"
	elif (find_word("is", clean_resp)):
		store_sen = clean_resp.split("is")
		print "Eliza: What else comes to your mind when you think of " + store_sen[0] + "?"
	elif (find_word("i", clean_resp) and find_word("don", clean_resp) or find_word("dont", clean_resp)):
		if (find_word("don", clean_resp)):
			store_sen = clean_resp.split("don")
		else:
			store_sen = clean_resp.split("dont")
		print "Eliza: Do you wish to" + store_sen[-1] + "?"
	elif (find_word("gosh", clean_resp) or find_word("darn", clean_resp)):
		print "Eliza: Does it make you feel strong to use that kind of language?"
	elif (find_word("yes", clean_resp) and find_word("no", clean_resp)):
		print "Eliza: You seem uncertain."
	elif (find_word("name", clean_resp) or find_word("names", clean_resp) or find_word("named", clean_resp)):
		print "Eliza: I'm not interested in names."
	elif ('?' in clean_resp):
		if (random_phrase == 1):
			print "Eliza: Have you asked such questions before?"
		else:
			print "Eliza: What is it you really wish to know?"
	elif (find_word("stop", clean_resp) and find_word("talking", clean_resp) or find_word("goodbye", clean_resp)):
		print "Eliza: Okay, goodbye."
		break
	elif (len(clean_resp) < 15):
		print "Eliza: Tell me more."
	else:
		ran = random.randint(1,4)
		if(len(store) != 0):
			if (ran == 1):
				print "Eliza: OK " + store[0] + " tell me more."
			elif (ran == 2):
				print "Eliza: Do go on " + store[0] + "."
			else:
				print "Eliza: Interesting " + store[0] + " do go on."
		else:
			if(ran == 1):
				print "Eliza: Do go on"
			elif (ran == 2):
				print "Eliza: How do you feel about that?"
			elif (ran == 3):
				print "Eliza: Please, please, elucidate your thoughts."

	user_response = raw_input()

