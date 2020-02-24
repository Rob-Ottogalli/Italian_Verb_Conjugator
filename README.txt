
HOW TO USE THE PROGRAM:
1) Open the program in a Python editor, such as Spyder or Jupyter Notebook.
2) Run the program.
3) At the bottom of the code or in the next cell, enter the following statement: 
print(conjugate(verb, person, tense, mood))
4) Inside this function, replace the arguments with the options described in the list below.  All arguments must be entered as strings, in quotation marks.

The following arguments are required:

verb:  The verb to be conjugated in its infinitive form.  The verb may be regular, irregular, or reflexive. The infinitive must end in either "-are", "-ere", "-ire", "-rre", or "-rsi". 
person:  One of 7 subject pronouns in Italian.  (1st, 2nd, 3rd, singular, plural).  7 subject pronouns are currently supported: "io", "tu", "lui", "lei", "noi", "voi", "loro".  (Alternate forms of the 3rd person, such as egli, colui, or costui for lui ("he"), are currently not supported.)  
tense:  The desired tense or aspect of the verb.  "Present", "Imperfect", "Past Absolute" (also called the Preterite), "Future Simple", "Future Perfect", "Perfect", "Present Perfect", "Pluperfect", "Remote Pluperfect", and "Present Perfect".  
mood:  The mood ("indicative", "subjunctive", "conditional", "imperative") of the verb.

Example of how the function should look when ready to run:  
print(conjugate("darsi", "io", "present", "indicative"))


5) When complete, hit enter and run the program.
6) The function will print the verb in the desired conjugated form. 

Shortcut:  To print the full conjugation of a verb, use the contents of the "Test Criteria Model.txt" as a starting point.  Follow steps 1-6 described above, but in step 4, copy-paste the contents of "Test Criteria Model.txt" to the terminal, and run the function.  This will print all forms of the verb "darsi".  To print the full conjugation of another verb, open "Test Criteria Model.txt", click find and replace all, and change "darsi" with the desired verb.

Note on tenses/aspects: As not all tenses or aspects are present for all moods in Italian, the combinations of moods and tenses/aspects listed below are possible.  Additionally, as naming conventions of tenses vary across English textbooks, the tenses are given in the table below along with their corresponding name in Italian:

	Mood		Tense/Aspect			Name in Italian
01. 	Indicative	Present				Presente dell'Indicativo
02. 	Indicative	Imperfect			Imperfetto dell'Indicativo
03. 	Indicative	Past Absolute (Preterite)	Passato Remoto dell'Indicativo
04. 	Indicative	Future Simple			Futuro Semplice dell'Indicativo
05. 	Indicative	Future Perfect			Futuro Anteriore dell'Indicativo	
06. 	Indicative 	Present Perfect 		Passato Prossimo dell'Indicativo
07. 	Indicative	Pluperfect			Trapassato Prossimo dell'Indicativo
08. 	Indicative	Remote Pluperfect		Trapassato Remoto dell'Indicativo
09. 	Subjunctive	Present				Presente dell'Congiuntivo
10.	Subjunctive	Imperfect			Imperfetto dell'Congiuntivo
11.	Subjunctive	Present Perfect			Passato dell'Congiuntivo
12.	Subjunctive	Pluperfect			Trapassato dell'Congiuntivo
13.	Conditional	Present				Presente Condizionale
14.	Conditional	Perfect				Passato Condizionale
15.	Imperative 	Present				Imperativo	


Caveats:
1) The program does not include a spell-checker and does not recognize whether a verb entered is accepted in standard Italian.  It merely manipulates strings of text based on the final three letters, based on the rules of Italian phonetics and morphology. Thus, the program would conjugate a misspelled verb without correcting the misspelling.  If an irregular verb is misspelled, it could in theory be conjugated as if it were a regular verb.  Additionally, any random string of text ending in "-are", "-ere", "-ire", "-rre", or "-rsi" could be conjugated as if it were an actual verb.  

Example 1:  "pparlare" (instead of the regular verb "parlare") in the first person present indicative would yield "pparlo" instead of the expected "parlo".
Example 2:  "anndare" (instead of the irregular verb "andare") in the first person present indicative would yield "anndo" instead of the expected "vado".
Example 3:  "bidibidibombare" (a fictional word calqued from the verb in the phrase "All day long I'd biddy-biddy-bum" in the song "If I Were a Rich Man" from the musical Fiddler on the Roof) in the first person present conditional would yield "bidibidibomberei". 

Reference:
https://www.wordreference.com/conj/ItVerbs.aspx?v=

This project was developed in Python 3.6.