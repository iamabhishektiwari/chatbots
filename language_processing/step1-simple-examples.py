def Concordance(text,word):
	return text.concordance(word)

def Similer(text,word):
	return text.similer(word);

def similer_context(text,word):
	return text.common_contexts(word);

def generate_similer_para(text):
	return text.generate();

def lexical_diversity(text):
	return len(set(text))/len(text);


# #Test1
# exp1 = ['hello','world','test','reveal','blast'];
# print(lexical_diversity(exp1))