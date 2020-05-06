# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:26:16 2020

@author: Robert Ottogalli
"""

#FULL CONJUGATION FUNCTION
def conjugate(verb, person, tense, mood):
   if tense == "present" and mood == "indicative":
       ConjugatedVerb = PresentIndicative(verb, person)
   if tense == "imperfect" and mood == "indicative":
       ConjugatedVerb = ImperfectIndicative(verb, person)
   if tense == "past absolute" and mood == "indicative":
       ConjugatedVerb = PreteriteIndicative(verb, person)
   if tense == "future simple" and mood == "indicative":
       ConjugatedVerb = FutureSimple(verb, person)
   if tense == "future perfect" and mood == "indicative":
       ConjugatedVerb = FuturePerfectInd(verb, person)
   if tense == "present" and mood == "conditional":
       ConjugatedVerb = PresentConditional(verb, person)
   if tense == "perfect" and mood == "conditional":
       ConjugatedVerb = PerfectConditional(verb, person)
   if tense == "present" and mood == "subjunctive":
       ConjugatedVerb = PresentSubjunctive(verb, person)
   if tense == "imperfect" and mood == "subjunctive":
       ConjugatedVerb = ImperfectSubjunctive(verb, person)
   if tense == "present perfect" and mood == "indicative":
       ConjugatedVerb = PresentPerfectInd(verb, person)
   if tense == "pluperfect" and mood == "indicative":
       ConjugatedVerb = PluperfectInd(verb, person)
   if tense == "remote pluperfect" and mood == "indicative":
       ConjugatedVerb = RemotePluperfectInd(verb, person)
   if tense == "present perfect" and mood == "subjunctive":
       ConjugatedVerb = PresentPerfectSubjunctive(verb, person)
   if tense == "pluperfect" and mood == "subjunctive":
       ConjugatedVerb = PluperfectSubjunctive(verb, person)
   if tense == "present" and mood == "imperative":
       ConjugatedVerb = Imperative(verb, person)
       return ConjugatedVerb
   #Reflexive Decoder (Generic):  After verb is parsed, adds appropriate reflexive pronouns to finite verb form. Works for all finite verb forms except Imperative.
   if verb[len(verb)-2:len(verb)] == "si":
       if person == "io":
          return "mi "+ConjugatedVerb
       elif person == "tu":
          return "ti "+ConjugatedVerb
       elif person == "lui" or person == "lei":
          return "si "+ConjugatedVerb
       elif person == "noi":
          return "ci "+ConjugatedVerb
       elif person == "voi":
          return "vi "+ConjugatedVerb
       elif person == "loro":
          return "si "+ConjugatedVerb
   else:
       return ConjugatedVerb 

        
   
#   person = ["io", "tu", "lui", "lei", "noi", "voi", "loro"]
#stem rules:
#   consonant = ["b", "c", "d", "f", "g", "h", "l", "m", "n", "p", "r", "s", "t", "v", "z"]
#   vowel = ["a", "e", "i", "o", "u"]

#REFLEXIVE VERB ENCODER/DECODERS
#Reflexive Encoder Function:  Converts reflexive verb infinitive to non-reflexive verb infinitive for parsing
def ReflexiveEncoder(verb):  
    if verb[len(verb)-2:len(verb)] == "si":
        if verb[len(verb)-5:len(verb)-2] == "dur" or verb[len(verb)-5:len(verb)-2] == "por" or verb[len(verb)-6:len(verb)-2] == "trar":
            WorkingVerb = verb[0:len(verb)-2]+"re"
        else:
            WorkingVerb = verb[0:len(verb)-2]+"e"
    else:
        WorkingVerb = verb
    return WorkingVerb

#PRESENT INDICATIVE FUNCTION
def PresentIndicative(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   if WorkingVerb == "andare" or WorkingVerb == "dare" or WorkingVerb == "fare" or WorkingVerb == "stare" or WorkingVerb == "avere" or WorkingVerb == "bere" or WorkingVerb == "cadere" or WorkingVerb == "dovere" or WorkingVerb == "essere" or WorkingVerb == "nuocere" or WorkingVerb == "potere" or WorkingVerb == "sapere" or WorkingVerb == "tenere" or WorkingVerb == "valere" or WorkingVerb == "volere" or WorkingVerb == "dire" or WorkingVerb == "morire" or WorkingVerb == "salire" or WorkingVerb == "udire" or WorkingVerb == "riudire" or WorkingVerb == "uscire" or WorkingVerb == "venire" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "ridare" or WorkingVerb == "affarsi" or WorkingVerb == "assuetare" or WorkingVerb == "confarsi" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "riavere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere" or WorkingVerb == "riessere" or WorkingVerb == "risapere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere" or WorkingVerb == "avvalersi" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalersi" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire" or WorkingVerb == "premorire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
       ConjugatedVerb = IrregPres(WorkingVerb, person)
   else:
       ConjugatedVerb = RegPres(WorkingVerb, person)
   return ConjugatedVerb

#Regular Present Indicative Stem Function
def PresStem(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   Stem = WorkingVerb[0:len(WorkingVerb)-3]
   StemEnding = Stem[len(Stem)-1]

   #-ARE verbs:
   if InfinitiveEnding == "are":
   #rule for stem in hard or soft "c" or "g": mancare, indagare
      if StemEnding == "c" or StemEnding == "g":
         if person == "tu" or person == "noi":
            return Stem+"h"
         else:
            return Stem
   #rule for stem in "i"
      if StemEnding == "i":
         #rule for verbs like sviare "tu svii"
         if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "vvi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "svi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "nvi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "bli" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "spi" or WorkingVerb == "desiare" or WorkingVerb == "deviare" or WorkingVerb == "forviare" or WorkingVerb == "fuorviare" or WorkingVerb == "piare" or WorkingVerb == "sciare" or WorkingVerb == "striare":
            return Stem
         #rule for verbs like lasciare, cambiare, mangiare
             #conjugational ending begins with 'i'
         elif person == "tu" or person == "noi":
            Stem = WorkingVerb[0:len(verb)-4]
            return Stem
             #conjugational ending does not begin with 'i'
         else:
            return Stem
   #rule for regular -are verbs, like parlare
      else:
         return Stem
   
   #-ERE verbs:
   if InfinitiveEnding == "ere":
   #rule for verbs like piacere
      if StemEnding == "c" and Stem[len(Stem)-2] == "a":
         if person == "io" or person == "loro":
            return Stem+"ci"
         elif person == "noi":
            return Stem+"c"
         else:
            return Stem
   #rule for verbs like cuocere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuoc":
         if person == "io" or person == "loro":
            return Stem+"i"
         else:
            return Stem
   #rule for verbs like rimanere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "an":
         if person == "io" or person == "loro":
            return Stem+"g"
         else:
            return Stem
   #rule for spegnere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "gn":
         if person == "io" or person == "loro":
            return WorkingVerb[0:len(WorkingVerb)-5]+"ng"
         else:
            return Stem
   #rule for verbs like sedere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "sed":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":         
            return WorkingVerb[0:len(WorkingVerb)-5]+"ied"
         else:
            return Stem
   #rule for verbs like scegliere, togliere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "gli":
         if person == "io" or person == "loro":
            return WorkingVerb[0:len(WorkingVerb)-6]+"lg"
         if person == "tu" or person == "noi":
            Stem = WorkingVerb[0:len(WorkingVerb)-4]
            return Stem
         else:
            return Stem
   #rule for all other verbs
      else:
         return Stem
   
   #-IRE verbs:
   if InfinitiveEnding == "ire":
      #rule for verbs like dormire, servire, offrire, aprire, pentire, seguire, fuggire
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "dorm" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pent" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "serv" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "part" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "apr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "copr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "soffr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "segu" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "fugg":
         return Stem
      #rule for cucire
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "cuc":
         if person == "io" or person == "loro":
            return Stem+"i"
         else:
            return Stem
      #rule for verbs like finire (-ISC- verbs)
      else:
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"isc"
         else:
            return Stem
   
   #-RRE verbs:
   if InfinitiveEnding == "rre":
      #rule for verbs like condurre
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "du":
         return Stem+"c"
      #rule for verbs like trarre
      elif WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "tra":
         if person == "io" or person == "loro":
            return Stem+"gg"
         else:
            return Stem
      #rule for verbs like porre
      elif WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "po":
         if person == "io" or person == "loro":
            return Stem+"ng"
         else:
            return Stem+"n"
        
#Regular Present Indicative Conjugator Function
def RegPres(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   ConjStem = PresStem(WorkingVerb, person)

   #present conjugations:
   if InfinitiveEnding == "are":
     if person == "io":
        return ConjStem+"o"
     elif person == "tu":
        return ConjStem+"i"
     elif person == "lui" or person == "lei":
        return ConjStem+"a"
     elif person == "noi":
        return ConjStem+"iamo"
     elif person == "voi":
        return ConjStem+"ate"
     elif person == "loro":
        return ConjStem+"ano"      
   if InfinitiveEnding == "ere" or InfinitiveEnding == "rre" or InfinitiveEnding == "ire":
     if person == "io":
        return ConjStem+"o"
     elif person == "tu":
        return ConjStem+"i"
     elif person == "lui" or person == "lei":
        return ConjStem+"e"
     elif person == "noi":
        return ConjStem+"iamo"
     elif person == "voi":
         if InfinitiveEnding == "ire":
            return ConjStem+"ite"
         else:
            return ConjStem+"ete"
     elif person == "loro":
        return ConjStem+"ono"  

#Irregular Present Indicative Conjugator Function
      #Note:  For code purposes, the "Stem" of Irregular verbs variable is defined so that Stem of main verb is "nil" and Stem of derivative verbs is the prefix of the derivative verb.
      #Examples:
      #Stem of "andare": ""
      #Stem of "riandare": "ri"
      #Stem of "dire":""
      #Stem of "disdire": "dis"

def IrregPres(WorkingVerb, person):
   #rule for forms of "andare"
   if WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare":
      Stem = WorkingVerb[0:len(WorkingVerb)-6]
      if person == "io":
         return Stem+"vado"
      elif person == "tu":
         return Stem+"vai"
      elif person == "lui" or person == "lei":
         return Stem+"va"
      elif person == "noi":
         return Stem+"andiamo"
      elif person == "voi":
         return Stem+"andate"
      elif person == "loro":
         return Stem+"vanno"
   #rule for forms of "dare"
   if WorkingVerb == "dare" or WorkingVerb == "ridare":
      Stem = WorkingVerb[0:len(WorkingVerb)-4]
      if person == "io":
         return Stem+"do"
      elif person == "tu":
         return Stem+"dai"
      elif person == "lui" or person == "lei":
         return Stem+"dà"
      elif person == "noi":
         return Stem+"diamo"
      elif person == "voi":
         return Stem+"date"
      elif person == "loro":
         return Stem+"danno"
   #rule for forms of "fare"
   if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare":
     Stem = WorkingVerb[0:len(WorkingVerb)-4]
     if person == "io":
        return Stem+"faccio"
     elif person == "tu":
        return Stem+"fai"
     elif person == "lui" or person == "lei":
        return Stem+"fa"
     elif person == "noi":
        return Stem+"facciamo"
     elif person == "voi":
        return Stem+"fate"
     elif person == "loro":
        return Stem+"fanno"
   #rule for forms of "stare"
   if WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare":
     Stem = WorkingVerb[0:len(WorkingVerb)-5]
     if person == "io":
        return Stem+"sto"
     elif person == "tu":
        return Stem+"stai"
     elif person == "lui" or person == "lei":
        return Stem+"sta"
     elif person == "noi":
        return Stem+"stiamo"
     elif person == "voi":
        return Stem+"state"
     elif person == "loro":
        return Stem+"stanno"
   #rule for forms of "avere"
   if WorkingVerb == "avere" or WorkingVerb == "riavere":
     Stem = WorkingVerb[0:len(WorkingVerb)-5]
     if person == "io":
        return Stem+"ho"
     elif person == "tu":
        return Stem+"hai"
     elif person == "lui" or person == "lei":
        return Stem+"ha"
     elif person == "noi":
        return Stem+"abbiamo"
     elif person == "voi":
        return Stem+"avete"
     elif person == "loro":
        return Stem+"hanno"
   #rule for forms of "bere"
   if WorkingVerb == "bere":
     if person == "io":
        return "bevo"
     elif person == "tu":
        return "bevi"
     elif person == "lui" or person == "lei":
        return "beve"
     elif person == "noi":
        return "beviamo"
     elif person == "voi":
        return "bevete"
     elif person == "loro":
        return "bevono"
   #rule for forms of "cadere"
   if WorkingVerb == "cadere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"cado"
     elif person == "tu":
        return Stem+"cadi"
     elif person == "lui" or person == "lei":
        return Stem+"cade"
     elif person == "noi":
        return Stem+"cadiamo"
     elif person == "voi":
        return Stem+"cadete"
     elif person == "loro":
        return Stem+"cadono"
   #rule for forms of "dovere"
   if WorkingVerb == "dovere":
     if person == "io":
        return "devo"
     elif person == "tu":
        return "devi"
     elif person == "lui" or person == "lei":
        return "deve"
     elif person == "noi":
        return "dobbiamo"
     elif person == "voi":
        return "dovete"
     elif person == "loro":
        return "devono"
   #rule for forms of "essere"
   if WorkingVerb == "essere" or WorkingVerb == "riessere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"sono"
     elif person == "tu":
        return Stem+"sei"
     elif person == "lui" or person == "lei":
        return Stem+"è"
     elif person == "noi":
        return Stem+"siamo"
     elif person == "voi":
        return Stem+"siete"
     elif person == "loro":
        return Stem+"sono"
   #rule for forms of "nuocere"
   if WorkingVerb == "nuocere":
     Stem = WorkingVerb[0:len(WorkingVerb)-7]
     if person == "io":
        return Stem+"nuoccio, "+Stem+"noccio"
     elif person == "tu":
        return Stem+"nuoci"
     elif person == "lui" or person == "lei":
        return Stem+"nuoce"
     elif person == "noi":
        return Stem+"nuociamo, "+Stem+"nociamo"
     elif person == "voi":
        return Stem+"nuocete, "+Stem+"nocete"
     elif person == "loro":
        return Stem+"nuocciono, "+Stem+"nocciono"
   #rule for forms of "potere"
   if WorkingVerb == "potere":
     if person == "io":
        return "posso"
     elif person == "tu":
        return "puoi"
     elif person == "lui" or person == "lei":
        return "può"
     elif person == "noi":
        return "possiamo"
     elif person == "voi":
        return "potete"
     elif person == "loro":
        return "possono"
   #rule for forms of "sapere"
   if WorkingVerb == "sapere" or WorkingVerb == "risapere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"so"
     elif person == "tu":
        return Stem+"sai"
     elif person == "lui" or person == "lei":
        return Stem+"sa"
     elif person == "noi":
        return Stem+"sappiamo"
     elif person == "voi":
        return Stem+"sapete"
     elif person == "loro":
        return Stem+"sanno"
   #rule for forms of "tenere":
   if WorkingVerb == "tenere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"tengo"
     elif person == "tu":
        return Stem+"tieni"
     elif person == "lui" or person == "lei":
        return Stem+"tiene"
     elif person == "noi":
        return Stem+"teniamo"
     elif person == "voi":
        return Stem+"tenete"
     elif person == "loro":
        return Stem+"tengono"  
   #rule for forms of "valere":
   if WorkingVerb == "valere" or WorkingVerb == "avvalere" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"valgo"
     elif person == "tu":
        return Stem+"vali"
     elif person == "lui" or person == "lei":
        return Stem+"vale"
     elif person == "noi":
        return Stem+"valiamo"
     elif person == "voi":
        return Stem+"valete"
     elif person == "loro":
        return Stem+"valgono"  
   #rule for forms of "volere"
   if WorkingVerb == "volere" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"voglio"
     elif person == "tu":
        return Stem+"vuoi"
     elif person == "lui" or person == "lei":
        return Stem+"vuole"
     elif person == "noi":
        return Stem+"vogliamo"
     elif person == "voi":
        return Stem+"volete"
     elif person == "loro":
        return Stem+"vogliono"
   #rule for forms of "dire"
   if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
     Stem = WorkingVerb[0:len(WorkingVerb)-4]
     if person == "io":
        return Stem+"dico"
     elif person == "tu":
        return Stem+"dici"
     elif person == "lui" or person == "lei":
        return Stem+"dice"
     elif person == "noi":
        return Stem+"diciamo"
     elif person == "voi":
        return Stem+"dite"
     elif person == "loro":
        return Stem+"dicono"
   #rule for forms of "morire"
   if WorkingVerb == "morire" or WorkingVerb == "premorire":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"muoio"
     elif person == "tu":
        return Stem+"muori"
     elif person == "lui" or person == "lei":
        return Stem+"muore"
     elif person == "noi":
        return Stem+"moriamo"
     elif person == "voi":
        return Stem+"morite"
     elif person == "loro":
        return Stem+"muoiono"
   #rule for forms of "salire"
   if WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"salgo"
     elif person == "tu":
        return Stem+"sali"
     elif person == "lui" or person == "lei":
        return Stem+"sale"
     elif person == "noi":
        return Stem+"saliamo"
     elif person == "voi":
        return Stem+"salite"
     elif person == "loro":
        return Stem+"salgono"
   #rule for forms of "udire"
   if WorkingVerb == "udire" or WorkingVerb == "riudire":
     Stem = WorkingVerb[0:len(WorkingVerb)-5]
     if person == "io":
        return Stem+"odo"
     elif person == "tu":
        return Stem+"odi"
     elif person == "lui" or person == "lei":
        return Stem+"ode"
     elif person == "noi":
        return Stem+"udiamo"
     elif person == "voi":
        return Stem+"udite"
     elif person == "loro":
        return Stem+"odono" 
   #rule for forms of "uscire"
   if WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"esco"
     elif person == "tu":
        return Stem+"esci"
     elif person == "lui" or person == "lei":
        return Stem+"esce"
     elif person == "noi":
        return Stem+"usciamo"
     elif person == "voi":
        return Stem+"uscite"
     elif person == "loro":
        return Stem+"escono" 
   #rule for forms of "venire"
   if WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"vengo"
     elif person == "tu":
        return Stem+"vieni"
     elif person == "lui" or person == "lei":
        return Stem+"viene"
     elif person == "noi":
        return Stem+"veniamo"
     elif person == "voi":
        return Stem+"venite"
     elif person == "loro":
        return Stem+"vengono" 

#IMPERFECT INDICATIVE FUNCTION
def ImperfectIndicative(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare" or WorkingVerb == "bere" or WorkingVerb == "essere" or WorkingVerb == "riessere" or WorkingVerb == "nuocere" or WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
       ConjVerb = IrregImperfectInd(WorkingVerb, person)
    else:
       ConjVerb = RegImperfectIndicative(WorkingVerb, person)
    return ConjVerb

#Imperfect Stem Function
def ImperfectIndStem(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   Stem = WorkingVerb[0:len(WorkingVerb)-3]
   #-ARE verbs.   
   if InfinitiveEnding == "are":
         return Stem
   #-ERE verbs:
   if InfinitiveEnding == "ere":
         return Stem
   #-IRE verbs:
   if InfinitiveEnding == "ire":
         return Stem
   #-RRE verbs:
   if InfinitiveEnding == "rre":
      #rule for verbs like indurre
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "du":
         return Stem+"c"
      #rule for verbs like trarre
      elif WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "tra":
         return Stem
      #rule for verbs like porre
      elif WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "po":
         return Stem+"n"

#Regular Imperfect Indicative Function
def RegImperfectIndicative(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   ConjStem = ImperfectIndStem(WorkingVerb, person)
   #Imperfect conjugations:
   if InfinitiveEnding == "are":
     if person == "io":
        return ConjStem+"avo"
     elif person == "tu":
        return ConjStem+"avi"
     elif person == "lui" or person == "lei":
        return ConjStem+"ava"
     elif person == "noi":
        return ConjStem+"avamo"
     elif person == "voi":
        return ConjStem+"avate"
     elif person == "loro":
        return ConjStem+"avano"      
   if InfinitiveEnding == "ere" or InfinitiveEnding == "rre":
     if person == "io":
        return ConjStem+"evo"
     elif person == "tu":
        return ConjStem+"evi"
     elif person == "lui" or person == "lei":
        return ConjStem+"eva"
     elif person == "noi":
        return ConjStem+"evamo"
     elif person == "voi":
        return ConjStem+"evate"
     elif person == "loro":
        return ConjStem+"evano"
   if InfinitiveEnding == "ire":
     if person == "io":
        return ConjStem+"ivo"
     elif person == "tu":
        return ConjStem+"ivi"
     elif person == "lui" or person == "lei":
        return ConjStem+"iva"
     elif person == "noi":
        return ConjStem+"ivamo"
     elif person == "voi":
        return ConjStem+"ivate"
     elif person == "loro":
        return ConjStem+"ivano"

#Irregular Imperfect Indicative Function
        #Note:  The following verbs are completely regular in the imperfect indicative and are not treated separately under the Irregular Imperfect function:
        #andare, dare, stare, avere, cadere, dovere, potere, sapere, tenere, valere, volere, morire, salire, udire, uscire, venire
def IrregImperfectInd(verb, person):
   #fare, bere, essere, nuocere, dire
   #rule for forms of "fare"
   WorkingVerb = ReflexiveEncoder(verb)
   if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare":
     Stem = WorkingVerb[0:len(WorkingVerb)-4]
     if person == "io":
        return Stem+"facevo"
     elif person == "tu":
        return Stem+"facevi"
     elif person == "lui" or person == "lei":
        return Stem+"faceva"
     elif person == "noi":
        return Stem+"facevamo"
     elif person == "voi":
        return Stem+"facevate"
     elif person == "loro":
        return Stem+"facevano"
   #rule for forms of "bere"
   if WorkingVerb == "bere":
     if person == "io":
        return "bevevo"
     elif person == "tu":
        return "bevevi"
     elif person == "lui" or person == "lei":
        return "beveva"
     elif person == "noi":
        return "bevevamo"
     elif person == "voi":
        return "bevevate"
     elif person == "loro":
        return "bevevano"
   #rule for forms of "essere"
   if WorkingVerb == "essere" or WorkingVerb == "riessere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"ero"
     elif person == "tu":
        return Stem+"eri"
     elif person == "lui" or person == "lei":
        return Stem+"era"
     elif person == "noi":
        return Stem+"eravamo"
     elif person == "voi":
        return Stem+"eravate"
     elif person == "loro":
        return Stem+"eravano"
   #rule for forms of "nuocere"
   if WorkingVerb == "nuocere":
     Stem = WorkingVerb[0:len(WorkingVerb)-7]
     if person == "io":
        return Stem+"nuocevo, "+Stem+"nocevo"
     elif person == "tu":
        return Stem+"nuocevi, "+Stem+"nocevi"
     elif person == "lui" or person == "lei":
        return Stem+"nuoceva, "+Stem+"noceva"
     elif person == "noi":
        return Stem+"nuocevamo, "+Stem+"nocevamo"
     elif person == "voi":
        return Stem+"nuocevate, "+Stem+"nocevate"
     elif person == "loro":
        return Stem+"nuocevano, "+Stem+"nocevano"
   #rule for forms of "dire"
   if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
     Stem = WorkingVerb[0:len(WorkingVerb)-4]
     if person == "io":
        return Stem+"dicevo"
     elif person == "tu":
        return Stem+"dicevi"
     elif person == "lui" or person == "lei":
        return Stem+"diceva"
     elif person == "noi":
        return Stem+"dicevamo"
     elif person == "voi":
        return Stem+"dicevate"
     elif person == "loro":
        return Stem+"dicevano"

#PRETERITE (PASSATO REMOTO) FUNCTION
def PreteriteIndicative(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if WorkingVerb == "dare" or WorkingVerb == "ridare" or WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare" or WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "avere" or WorkingVerb == "riavere" or WorkingVerb == "bere" or WorkingVerb == "essere" or WorkingVerb == "riessere" or WorkingVerb == "nuocere" or WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire" or WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
        ConjStem = IrregPreterite(WorkingVerb, person)
    else:
        ConjStem =  RegPreterite(WorkingVerb, person)
    return ConjStem

#Regular Verb Preterite Stem Function
def RegPreteriteStem(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   TuStem = WorkingVerb[0:len(WorkingVerb)-3]
   #-ARE verbs   
   if InfinitiveEnding == "are":
       return TuStem
   #-ERE verbs
   if InfinitiveEnding == "ere" or InfinitiveEnding == "rre":
   #rule for verbs like nascere, piacere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "nasc" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ac":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"cqu"
   #rule for verbs like conoscere and crescere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "osc" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "esc":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"bb"
   #rule for verbs like figgere, sconfiggere, struggere, leggere, reggere, crocifiggere and scindere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ugg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "egg" or verb == "figgere" or verb == "affliggere" or verb == "configgere" or verb == "confliggere" or verb == "defiggere" or verb == "defiggere" or verb == "friggere" or verb == "infliggere" or verb == "rifriggere" or verb == "sconfiggere" or verb == "soffriggere" or verb == "trafiggere" or verb == "crocifiggere" or verb == "affiggere" or verb == "crocefiggere" or verb == "infiggere" or verb == "prefiggere" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "scind":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"ss"
   #rule for verbs like rompere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "romp":
         IoStem = WorkingVerb[0:len(WorkingVerb)-6]+"upp"
   #rule for verbs like dirigere, negligere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ig":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"ess"
   #rule for spegnere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "gn":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"ns"
    #rule for verbs like distinguere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ngu":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"s"
   #rule for verbs like stringere
      if WorkingVerb[len(WorkingVerb)-9:len(WorkingVerb)-3] == "string":
         IoStem = WorkingVerb[0:len(WorkingVerb)-4]+"s"
   #rule for verbs like vincere, fingere, spingere, spandere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "nc" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ng" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pand":
         IoStem = WorkingVerb[0:len(WorkingVerb)-4]+"s"
   #rule for verbs like scegliere, togliere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "gli":
         IoStem = WorkingVerb[0:len(WorkingVerb)-6]+"ls"
   #rule for verbs like svolgere, risolvere, sorgere, torcere, emmergere, spargere, ardere, perdere, correre
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "lv" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "lg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "org" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "urg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "orc" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "erg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "arg" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "rd" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "corr":
         IoStem = WorkingVerb[0:len(WorkingVerb)-4]+"s"
   #rule for verbs like vedere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ved":
         IoStem = WorkingVerb[0:len(WorkingVerb)-6]+"vid"
   #rule for verbs like chiedere, rimanere, persuadere, invadere, ridere, esplodere, and concludere
      if WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "chied" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "an" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ad" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "id" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "od" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ud":
         IoStem = WorkingVerb[0:len(WorkingVerb)-4]+"s"
   #rule for verbs like concedere, discutere, scrivere, vivere
      if WorkingVerb == "concedere" or WorkingVerb == "retrocedere" or WorkingVerb == "succedere" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ut" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "scriv" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "viv":
         IoStem = WorkingVerb[0:len(WorkingVerb)-4]+"ss"
   #rule for verbs like muovere, scuotere, cuocere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuot" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "muov" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuoc":
         IoStem = WorkingVerb[0:len(WorkingVerb)-6]+"oss"
   #rule for verbs like esprimere, opprimere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "prim":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"ess"
   #rule for verbs like prendere, rendere, scendere, accendere, rispondere, nascondere, spendere, tendere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "rend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pond" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cond" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "spend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "tend":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"s"
   #rule for verbs like fondere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "fond":
         IoStem = WorkingVerb[0:len(WorkingVerb)-6]+"us"
   #rule for verbs like mettere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "mett":
         IoStem = WorkingVerb[0:len(WorkingVerb)-6]+"is"
   #rule for verbs like riflettere, connettere
      if WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "flett" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "nett":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"ss"
   #rule for verbs like espellere and avellere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pell" or WorkingVerb == "avellere":
         IoStem = WorkingVerb[0:len(WorkingVerb)-6]+"uls"
   #rule for svellere, divellere
      if WorkingVerb == "svellere" or WorkingVerb == "divellere" or WorkingVerb == "eccellere":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"ls"
   #rule for verbs like assumere and presumere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "sum":
         IoStem = WorkingVerb[0:len(WorkingVerb)-4]+"ns"
   #rule for verbs like redimere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "dim":
         IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"ens"
   #rule for forms of "cadere"
      if WorkingVerb == "cadere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere":
         IoStem = WorkingVerb[0:len(WorkingVerb)-3]+"d"
   #rule for forms of "sapere"
      if WorkingVerb == "sapere" or WorkingVerb == "risapere":
        IoStem = WorkingVerb[0:len(WorkingVerb)-5]+"epp"
   #rule for forms of "tenere":
      if WorkingVerb == "tenere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere":
         IoStem = WorkingVerb[0:len(WorkingVerb)-3]+"n"
   #rule for forms of "valere":
      if WorkingVerb == "valere" or WorkingVerb == "avvalere" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalere":
         IoStem = WorkingVerb[0:len(WorkingVerb)-3]+"s"
   #rule for forms of "volere"
      if WorkingVerb == "volere" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere":
         IoStem = WorkingVerb[0:len(WorkingVerb)-3]+"l"
   #-RRE verbs
   #rule for verbs like indurre
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "du":
          TuStem = WorkingVerb[0:len(WorkingVerb)-3]+"c"
          IoStem = WorkingVerb[0:len(WorkingVerb)-3]+"ss"
   #rule for verbs like trarre
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "tra":
          TuStem = WorkingVerb[0:len(WorkingVerb)-3]
          IoStem = WorkingVerb[0:len(WorkingVerb)-3]+"ss"
   #rule for verbs like porre
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "po":
          TuStem = WorkingVerb[0:len(WorkingVerb)-3]+"n"
          IoStem = WorkingVerb[0:len(WorkingVerb)-3]+"s"
   #rule for which stems to return      
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "nasc" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ac" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "sc" or InfinitiveEnding == "rre" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ugg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "egg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ugg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "egg" or verb == "figgere" or verb == "affliggere" or verb == "configgere" or verb == "confliggere" or verb == "defiggere" or verb == "defiggere" or verb == "friggere" or verb == "infliggere" or verb == "rifriggere" or verb == "sconfiggere" or verb == "soffriggere" or verb == "trafiggere" or verb == "crocifiggere" or verb == "affiggere" or verb == "crocefiggere" or verb == "infiggere" or verb == "prefiggere" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "scind" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "romp" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ig" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "gn" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ngu" or WorkingVerb[len(WorkingVerb)-9:len(WorkingVerb)-3] == "string" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "nc" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ng" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pand" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "gli" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "lv" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "lg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "org" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "urg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "orc" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "erg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "arg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ved" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "chied" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "an" or WorkingVerb == "concedere" or WorkingVerb == "retrocedere" or WorkingVerb == "succedere" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ut" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuot" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "muov" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuoc" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "scriv" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "prim" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ad" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "id" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "od" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ud" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "rd" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "rend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pond" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cond" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "fond" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "corr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "mett" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "flett" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "nett" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pell" or WorkingVerb == "avellere" or WorkingVerb == "svellere" or WorkingVerb == "divellere" or WorkingVerb == "eccellere" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "sum" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "dim" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "viv" or WorkingVerb == "cadere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere" or WorkingVerb == "sapere" or WorkingVerb == "risapere" or WorkingVerb == "tenere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere" or WorkingVerb == "valere" or WorkingVerb == "avvalere" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalere" or WorkingVerb == "volere" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "spend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "tend":
         if person == "io" or person == "lui" or person == "lei" or person == "loro":
             return IoStem
         else:
             return TuStem
      else:
         return TuStem
   #-IRE verbs   
   if InfinitiveEnding == "ire":
       return TuStem

#Regular Verb Preterite Finite Function
def RegPreterite(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   ConjStem = RegPreteriteStem(WorkingVerb, person)
   #present conjugations:
   if InfinitiveEnding == "are":
     if person == "io":
        return ConjStem+"ai"
     elif person == "tu":
        return ConjStem+"asti"
     elif person == "lui" or person == "lei":
        return ConjStem+"ò"
     elif person == "noi":
        return ConjStem+"ammo"
     elif person == "voi":
        return ConjStem+"aste"
     elif person == "loro":
        return ConjStem+"arono"      
   if InfinitiveEnding == "ere" or InfinitiveEnding == "rre":
     if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "nasc" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ac" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "sc" or InfinitiveEnding == "rre" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ugg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "egg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ugg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "egg" or verb == "figgere" or verb == "affliggere" or verb == "configgere" or verb == "confliggere" or verb == "defiggere" or verb == "defiggere" or verb == "friggere" or verb == "infliggere" or verb == "rifriggere" or verb == "sconfiggere" or verb == "soffriggere" or verb == "trafiggere" or verb == "crocifiggere" or verb == "affiggere" or verb == "crocefiggere" or verb == "infiggere" or verb == "prefiggere" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "scind" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "romp" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ig" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "gn" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ngu" or WorkingVerb[len(WorkingVerb)-9:len(WorkingVerb)-3] == "string" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "nc" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ng" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pand" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "gli" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "lv" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "lg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "org" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "urg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "orc" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "erg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "arg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ved" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "chied" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "an" or WorkingVerb == "concedere" or WorkingVerb == "retrocedere" or WorkingVerb == "succedere" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ut" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuot" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "muov" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuoc" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "scriv" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "prim" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ad" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "id" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "od" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ud" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "rd" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "rend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pond" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cond" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "fond" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "corr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "mett" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "flett" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "nett" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pell" or WorkingVerb == "avellere" or WorkingVerb == "svellere" or WorkingVerb == "divellere" or WorkingVerb == "eccellere" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "sum" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "dim" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "viv" or WorkingVerb == "cadere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere" or WorkingVerb == "sapere" or WorkingVerb == "risapere" or WorkingVerb == "tenere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere" or WorkingVerb == "valere" or WorkingVerb == "avvalere" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalere" or WorkingVerb == "volere" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "spend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "tend":
         if person == "io":
             return ConjStem+"i"
         if person == "tu":
             return ConjStem+"esti"
         if person == "lui" or person == "lei":
             return ConjStem+"e"
         if person == "noi":
             return ConjStem+"emmo"
         if person == "voi":
             return ConjStem+"este"
         if person == "loro":
             return ConjStem+"ero"
     else:
         if person == "io":
             return ConjStem+"ei"
         elif person == "tu":
             return ConjStem+"esti"
         elif person == "lui" or person == "lei":
             return ConjStem+"è"
         elif person == "noi":
             return ConjStem+"emmo"
         elif person == "voi":
             return ConjStem+"este"
         elif person == "loro":
             return ConjStem+"erono"  
   if InfinitiveEnding == "ire":
     if person == "io":
        return ConjStem+"ii"
     elif person == "tu":
        return ConjStem+"isti"
     elif person == "lui" or person == "lei":
        return ConjStem+"ì"
     elif person == "noi":
        return ConjStem+"immo"
     elif person == "voi":
        return ConjStem+"iste"
     elif person == "loro":
        return ConjStem+"irono"

#Irregular Verb Preterite Function
        #These  verbs are completely regular in the preterite and are not given special treatment.  They will default to the Regular Preterite Verb Function: 
        #andare, dovere, potere, morire, salire, udire, uscire
        
        #These verbs have irregular IoStems but regular TuStems and are treated as special categories under the Regular Preterite Verb Function:
        #cadere, sapere, tenere, valere volere
        
        #These verbs are completely irregular in the preterite and are given special treatment under the Irregular Verb Preterite Function:
        #dare, fare, stare, avere, bere, essere, nuocere, dire
        
        #venire is technically regular in the TuStem and irregular in the TuStem. However, since it is the only -IRE verb that acts this way, it is grouped here among the irregular verbs.
def IrregPreterite(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   #rule for forms of "dare"
   if WorkingVerb == "dare" or WorkingVerb == "ridare":
      Stem = WorkingVerb[0:len(WorkingVerb)-4]
      if person == "io":
         return Stem+"diedi"
      elif person == "tu":
         return Stem+"desti"
      elif person == "lui" or person == "lei":
         return Stem+"diede"
      elif person == "noi":
         return Stem+"demmo"
      elif person == "voi":
         return Stem+"deste"
      elif person == "loro":
         return Stem+"diedero"
   #rule for forms of "fare"
   if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare":
     Stem = WorkingVerb[0:len(WorkingVerb)-4]
     if person == "io":
        return Stem+"feci"
     elif person == "tu":
        return Stem+"facesti"
     elif person == "lui" or person == "lei":
        return Stem+"fece"
     elif person == "noi":
        return Stem+"facemmo"
     elif person == "voi":
        return Stem+"faceste"
     elif person == "loro":
        return Stem+"fecero"
   #rule for forms of "stare"
   if WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare":
     Stem = WorkingVerb[0:len(WorkingVerb)-5]
     if person == "io":
        return Stem+"stetti"
     elif person == "tu":
        return Stem+"stesti"
     elif person == "lui" or person == "lei":
        return Stem+"stette"
     elif person == "noi":
        return Stem+"stemmo"
     elif person == "voi":
        return Stem+"steste"
     elif person == "loro":
        return Stem+"stettero"
   #rule for forms of "avere"
   if WorkingVerb == "avere" or WorkingVerb == "riavere":
     Stem = WorkingVerb[0:len(WorkingVerb)-5]
     if person == "io":
        return Stem+"ebbi"
     elif person == "tu":
        return Stem+"avesti"
     elif person == "lui" or person == "lei":
        return Stem+"ebbe"
     elif person == "noi":
        return Stem+"avemmo"
     elif person == "voi":
        return Stem+"aveste"
     elif person == "loro":
        return Stem+"ebbero"
   #rule for forms of "bere"
   if WorkingVerb == "bere":
     if person == "io":
        return "bevvi"
     elif person == "tu":
        return "bevesti"
     elif person == "lui" or person == "lei":
        return "bevve"
     elif person == "noi":
        return "bevemmo"
     elif person == "voi":
        return "beveste"
     elif person == "loro":
        return "bevvero"
   #rule for forms of "essere"
   if WorkingVerb == "essere" or WorkingVerb == "riessere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"fui"
     elif person == "tu":
        return Stem+"fosti"
     elif person == "lui" or person == "lei":
        return Stem+"fu"
     elif person == "noi":
        return Stem+"fummo"
     elif person == "voi":
        return Stem+"foste"
     elif person == "loro":
        return Stem+"furono"
   #rule for forms of "nuocere"
   if WorkingVerb == "nuocere":
     Stem = WorkingVerb[0:len(WorkingVerb)-7]
     if person == "io":
        return Stem+"nocqui"
     elif person == "tu":
        return Stem+"nuocesti, nocesti"
     elif person == "lui" or person == "lei":
        return Stem+"nocque"
     elif person == "noi":
        return Stem+"nuocemmo, nocemmo"
     elif person == "voi":
        return Stem+"nuoceste, noceste"
     elif person == "loro":
        return Stem+"nocquero"
   #rule for forms of "dire"
   if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
     Stem = WorkingVerb[0:len(WorkingVerb)-4]
     if person == "io":
        return Stem+"dissi"
     elif person == "tu":
        return Stem+"dicesti"
     elif person == "lui" or person == "lei":
        return Stem+"disse"
     elif person == "noi":
        return Stem+"dicemmo"
     elif person == "voi":
        return Stem+"diceste"
     elif person == "loro":
        return Stem+"dissero"
   #rule for forms of "venire"
   if WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"venni"
     elif person == "tu":
        return Stem+"venisti"
     elif person == "lui" or person == "lei":
        return Stem+"venne"
     elif person == "noi":
        return Stem+"venimmo"
     elif person == "voi":
        return Stem+"veniste"
     elif person == "loro":
        return Stem+"vennero" 

#FUTURE SIMPLE AND PRESENT CONDITIONAL FUNCTIONS

#Future/Conditional Stem Function
def FutureStem(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if WorkingVerb == "andare" or WorkingVerb == "dare" or WorkingVerb == "fare" or WorkingVerb == "stare" or WorkingVerb == "avere" or WorkingVerb == "bere" or WorkingVerb == "cadere" or WorkingVerb == "dovere" or WorkingVerb == "essere" or WorkingVerb == "nuocere" or WorkingVerb == "potere" or WorkingVerb == "sapere" or WorkingVerb == "tenere" or WorkingVerb == "valere" or WorkingVerb == "volere" or WorkingVerb == "dire" or WorkingVerb == "morire" or WorkingVerb == "salire" or WorkingVerb == "uscire" or WorkingVerb == "venire" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "ridare" or WorkingVerb == "affarsi" or WorkingVerb == "assuetare" or WorkingVerb == "confarsi" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "riavere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere" or WorkingVerb == "riessere" or WorkingVerb == "risapere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere" or WorkingVerb == "avvalersi" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalersi" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire" or WorkingVerb == "premorire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire" or WorkingVerb == "udire" or WorkingVerb == "riudire" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ved" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "viv" or WorkingVerb == "rimanere" or WorkingVerb == "permanere":
        return IrregFutureStem(verb, person)
    else:
        return RegFutureStem(verb, person)

#Regular Future/Conditional Stem Finder    
def RegFutureStem(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
    if InfinitiveEnding == "are":
        #rule for stem in soft "ci" or "gi"
        if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ci" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "gi":
            Stem = WorkingVerb[0:len(WorkingVerb)-4]+"er"
        else:
            Stem = WorkingVerb[0:len(WorkingVerb)-3]+"er"
    elif InfinitiveEnding == "ere" or InfinitiveEnding == "rre" or InfinitiveEnding == "ire":
        Stem = WorkingVerb[0:len(WorkingVerb)-1]
    return Stem

#Irregular Future/Conditional Stem Finder
    #Note:  These verbs are regular in the future/conditional and are not treated under this function: salire, uscire

def IrregFutureStem(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    #rule for verbs like andare
    if WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for forms of "dare"
    if WorkingVerb == "dare" or WorkingVerb == "ridare":
       Stem = WorkingVerb[0:len(WorkingVerb)-1]
       return Stem
    #rule for forms of "fare"
    if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare":
       Stem = WorkingVerb[0:len(WorkingVerb)-1]
       return Stem
    #rule for forms of "stare"
    if WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare":
       Stem = WorkingVerb[0:len(WorkingVerb)-1]
       return Stem
    #rule for forms of "avere"
    if WorkingVerb == "avere" or WorkingVerb == "riavere":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for forms of "bere"
    if WorkingVerb == "bere":
       Stem = WorkingVerb[0:len(WorkingVerb)-2]+"rr"
       return Stem
    #rule for forms of "cadere"
    if WorkingVerb == "cadere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for forms of "dovere"
    if WorkingVerb == "dovere":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for forms of "essere"
    if WorkingVerb == "essere" or WorkingVerb == "riessere":
       Stem = WorkingVerb[0:len(WorkingVerb)-6]+"sar"
       return Stem
    #rule for forms of "nuocere"
    if WorkingVerb == "nuocere":
       Stem = WorkingVerb[0:len(WorkingVerb)-1]
       return Stem
    #rule for forms of "potere"
    if WorkingVerb == "potere":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for verbs like "rimanere"
    if WorkingVerb == "rimanere" or WorkingVerb == "permanere":
       Stem = WorkingVerb[0:len(WorkingVerb)-4]+"rr"
       return Stem
    #rule for forms of "sapere"
    if WorkingVerb == "sapere" or WorkingVerb == "risapere":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for forms of "tenere":
    if WorkingVerb == "tenere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere":
       Stem = WorkingVerb[0:len(WorkingVerb)-4]+"rr"
       return Stem
    #rule for forms of "valere":
    if WorkingVerb == "valere" or WorkingVerb == "avvalere" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalere":
       Stem = WorkingVerb[0:len(WorkingVerb)-4]+"rr"
       return Stem
    #rule for forms of "vedere"
    if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ved":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for verbs like vivere
    if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "viv":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for forms of "volere"
    if WorkingVerb == "volere" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere":
       Stem = WorkingVerb[0:len(WorkingVerb)-4]+"rr"
       return Stem
    #rule for forms of "dire"
    if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
       Stem = WorkingVerb[0:len(WorkingVerb)-1]
       return Stem
    #rule for forms of "morire"
    if WorkingVerb == "morire" or WorkingVerb == "premorire":
       Stem = WorkingVerb[0:len(WorkingVerb)-4]+"rr"
       return Stem
     #rule for forms of "udire"
    if WorkingVerb == "udire" or WorkingVerb == "riudire":
       Stem = WorkingVerb[0:len(WorkingVerb)-3]+"r"
       return Stem
    #rule for forms of "venire"
    if WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
       Stem = WorkingVerb[0:len(WorkingVerb)-4]+"rr"
       return Stem

#FUTURE SIMPLE FUNCTION
def FutureSimple(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    ConjStem = FutureStem(WorkingVerb, person)
    if person == "io":
       ConjVerb = ConjStem+"ò"
    elif person == "tu":
       ConjVerb = ConjStem+"ai"
    elif person == "lui" or person == "lei":
       ConjVerb = ConjStem+"à"
    elif person == "noi":
       ConjVerb = ConjStem+"emo"
    elif person == "voi":
       ConjVerb = ConjStem+"ete"
    elif person == "loro":
       ConjVerb = ConjStem+"anno"  
    return ConjVerb 

#PRESENT CONDITIONAL FUNCTION
def PresentConditional(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    ConjStem = FutureStem(WorkingVerb, person)
    if person == "io":
       ConjVerb = ConjStem+"ei"
    elif person == "tu":
       ConjVerb = ConjStem+"esti"
    elif person == "lui" or person == "lei":
       ConjVerb = ConjStem+"ebbe"
    elif person == "noi":
       ConjVerb = ConjStem+"emmo"
    elif person == "voi":
       ConjVerb = ConjStem+"este"
    elif person == "loro":
       ConjVerb = ConjStem+"ebbero"  
    return ConjVerb 

#PRESENT SUBJUNCTIVE FUNCTION
def PresentSubjunctive(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if WorkingVerb == "andare" or WorkingVerb == "dare" or WorkingVerb == "fare" or WorkingVerb == "stare" or WorkingVerb == "avere" or WorkingVerb == "bere" or WorkingVerb == "cadere" or WorkingVerb == "dovere" or WorkingVerb == "essere" or WorkingVerb == "potere" or WorkingVerb == "sapere" or WorkingVerb == "tenere" or WorkingVerb == "valere" or WorkingVerb == "volere" or WorkingVerb == "dire" or WorkingVerb == "morire" or WorkingVerb == "salire" or WorkingVerb == "uscire" or WorkingVerb == "venire" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "ridare" or WorkingVerb == "affarsi" or WorkingVerb == "assuetare" or WorkingVerb == "confarsi" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "riavere" or WorkingVerb == "riessere" or WorkingVerb == "risapere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere" or WorkingVerb == "avvalersi" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalersi" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire" or WorkingVerb == "premorire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
        ConjStem = IrregPresSubj(WorkingVerb, person)
    else:
        ConjStem =  RegPresSubj(WorkingVerb, person)
    return ConjStem

#Regular Present Subjunctive Stem Function
def RegPresSubjStem(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   Stem = WorkingVerb[0:len(WorkingVerb)-3]
   StemEnding = Stem[len(Stem)-1]
   #-ARE verbs   
   if InfinitiveEnding == "are":
   #rule for stem in hard or soft "c" or "g"
      if StemEnding == "c" or StemEnding == "g":
         return Stem+"h"
   #rule for stem in "i"
      if StemEnding == "i":
         #rule for verbs like sviare "tu svii"
         if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "vvi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "svi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "nvi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "bli" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "spi" or WorkingVerb == "desiare" or WorkingVerb == "deviare" or WorkingVerb == "forviare" or WorkingVerb == "fuorviare" or WorkingVerb == "piare" or WorkingVerb == "sciare" or WorkingVerb == "striare":
            return Stem
         #rule for verbs like lasciare, cambiare, mangiare
             #conjugational ending begins with 'i'
     #    elif person == "tu" or person == "noi":
     #       Stem = WorkingVerb[0:len(verb)-4]
     #       return Stem
         else:
            Stem = WorkingVerb[0:len(verb)-4]
            return Stem
   #rule for regular -are verbs, like parlare
      else:
         return Stem
   #-ERE verbs
   if InfinitiveEnding == "ere":
    #rule for verbs like piacere
      if StemEnding == "c" and Stem[len(Stem)-2] == "a":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"ci"
         else:
            return Stem+"c"
   #rule for verbs like cuocere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuoc":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"i"
         else:
            return Stem
   #rule for verbs like rimanere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "an":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"g"
         else:
            return Stem
   #rule for spegnere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "gn":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return WorkingVerb[0:len(WorkingVerb)-5]+"ng"
         else:
            return Stem
   #rule for verbs like sedere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "sed":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return WorkingVerb[0:len(WorkingVerb)-5]+"ied"
         else:
            return Stem
   #rule for verbs like scegliere, togliere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "gli":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return WorkingVerb[0:len(WorkingVerb)-6]+"lg"
         if person == "noi" or person == "voi":
            Stem = WorkingVerb[0:len(WorkingVerb)-4]
            return Stem
   #rule for all other verbs
      else:
         return Stem
   #-IRE verbs:
   if InfinitiveEnding == "ire":
      #rule for verbs like dormire, servire, offrire, aprire, pentire, seguire, fuggire
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "dorm" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pent" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "serv" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "part" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "apr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "copr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "soffr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "segu" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "fugg":
         return Stem
      #rule for cucire
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "cuc":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"i"
         else:
            return Stem
      #rule for verbs like finire (-ISC- verbs)
      else:
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"isc"
         else:
            return Stem
   #-RRE verbs:
   if InfinitiveEnding == "rre":
      #rule for verbs like condurre
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "du":
         return Stem+"c"
      #rule for verbs like trarre
      elif WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "tra":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"gg"
         else:
            return Stem
      #rule for verbs like porre
      elif WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "po":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"ng"
         else:
            return Stem+"n"

#Regular Present Subjunctive Conjugator Function
def RegPresSubj(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   ConjStem = RegPresSubjStem(WorkingVerb, person)
   #present conjugations:
   if InfinitiveEnding == "are":
     if person == "io":
        return ConjStem+"i"
     elif person == "tu":
        return ConjStem+"i"
     elif person == "lui" or person == "lei":
        return ConjStem+"i"
     elif person == "noi":
        return ConjStem+"iamo"
     elif person == "voi":
        return ConjStem+"iate"
     elif person == "loro":
        return ConjStem+"ino"      
   if InfinitiveEnding == "ere" or InfinitiveEnding == "rre" or InfinitiveEnding == "ire":
     if person == "io":
        return ConjStem+"a"
     elif person == "tu":
        return ConjStem+"a"
     elif person == "lui" or person == "lei":
        return ConjStem+"a"
     elif person == "noi":
        return ConjStem+"iamo"
     elif person == "voi":
        return ConjStem+"iate"
     elif person == "loro":
        return ConjStem+"ano"  

#Irregular Present Subjunctive Stem Function
def IrregPresSubjStem(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   #rule for forms of andare
   if WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "vad"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "and"
             return Stem
   #rule for forms of "dare"
   if WorkingVerb == "dare" or WorkingVerb == "ridare":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "di"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "d"
             return Stem
   #rule for forms of "fare"
   if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "facci"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "facc"
             return Stem
   #rule for forms of "stare"
   if WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "sti"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "st"
             return Stem
   #rule for forms of "avere"
   if WorkingVerb == "avere" or WorkingVerb == "riavere":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "abbi"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "abb"
             return Stem
   #rule for forms of "bere"
   if WorkingVerb == "bere":
         Stem = WorkingVerb[0:len(WorkingVerb)-4] + "bev"
         return Stem
   #rule for forms of "dovere"
   if WorkingVerb == "dovere":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "dev"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "dobb"
             return Stem
   #rule for forms of "essere"
   if WorkingVerb == "essere" or WorkingVerb == "riessere":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "si"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "s"
             return Stem
   #rule for forms of "nuocere"
   if WorkingVerb == "nuocere":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-7] + "nuocci"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-7] + "nuoc"
             return Stem
   #rule for forms of "potere"
   if WorkingVerb == "potere":
         Stem = WorkingVerb[0:len(WorkingVerb)-6] + "poss"
         return Stem
   #rule for forms of "sapere"
   if WorkingVerb == "sapere" or WorkingVerb == "risapere":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "sappi"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "sapp"
             return Stem
   #rule for forms of "tenere":
   if WorkingVerb == "tenere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "teng"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "ten"
             return Stem
   #rule for forms of "valere":
   if WorkingVerb == "valere" or WorkingVerb == "avvalere" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalere":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "valg"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "val"
             return Stem
   #rule for forms of "volere"
   if WorkingVerb == "volere" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "vogli"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "vogl"
             return Stem
   #rule for forms of "dire"
   if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
         Stem = WorkingVerb[0:len(WorkingVerb)-4] + "dic"
         return Stem
   #rule for forms of "morire"
   if WorkingVerb == "morire" or WorkingVerb == "premorire":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "muoi"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "mor"
             return Stem
   #rule for forms of "salire"
   if WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "salg"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "sal"
             return Stem
   #rule for forms of "udire"
   if WorkingVerb == "udire" or WorkingVerb == "riudire":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "od"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "ud"
             return Stem
   #rule for forms of "uscire"
   if WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "esc"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "usc"
             return Stem
   #rule for forms of "venire"
   if WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "veng"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "ven"
             return Stem
 
#Irregular Present Subjunctive Conjugator Function
def IrregPresSubj(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   ConjStem = IrregPresSubjStem(WorkingVerb, person)
   if person == "io":
      return ConjStem+"a"
   elif person == "tu":
      return ConjStem+"a"
   elif person == "lui" or person == "lei":
      return ConjStem+"a"
   elif person == "noi":
      return ConjStem+"iamo"
   elif person == "voi":
      return ConjStem+"iate"
   elif person == "loro":
      return ConjStem+"ano"  

#IMPERFECT SUBJUNCTIVE FUNCTION
def ImperfectSubjunctive(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare" or WorkingVerb == "bere" or WorkingVerb == "essere" or WorkingVerb == "riessere" or WorkingVerb == "nuocere" or WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
       ConjVerb = IrregImperfectSubjunctive(WorkingVerb, person)
    else:
       ConjVerb = RegImperfectSubjunctive(WorkingVerb, person)
    return ConjVerb    

#Imperfect Subjunctive Stem Function
def ImperfectSubStem(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   Stem = WorkingVerb[0:len(WorkingVerb)-3]
   #-ARE verbs.   
   if InfinitiveEnding == "are":
         return Stem
   #-ERE verbs:
   if InfinitiveEnding == "ere":
         return Stem
   #-IRE verbs:
   if InfinitiveEnding == "ire":
         return Stem
   #-RRE verbs:
   if InfinitiveEnding == "rre":
      #rule for verbs like indurre
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "du":
         return Stem+"c"
      #rule for verbs like trarre
      elif WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "tra":
         return Stem
      #rule for verbs like porre
      elif WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "po":
         return Stem+"n"

#Regular Imperfect Indicative Function
def RegImperfectSubjunctive(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   ConjStem = ImperfectSubStem(WorkingVerb, person)
   #Imperfect conjugations:
   if InfinitiveEnding == "are":
     if person == "io":
        return ConjStem+"assi"
     elif person == "tu":
        return ConjStem+"assi"
     elif person == "lui" or person == "lei":
        return ConjStem+"asse"
     elif person == "noi":
        return ConjStem+"assimo"
     elif person == "voi":
        return ConjStem+"aste"
     elif person == "loro":
        return ConjStem+"assero"      
   if InfinitiveEnding == "ere" or InfinitiveEnding == "rre":
     if person == "io":
        return ConjStem+"essi"
     elif person == "tu":
        return ConjStem+"essi"
     elif person == "lui" or person == "lei":
        return ConjStem+"esse"
     elif person == "noi":
        return ConjStem+"essimo"
     elif person == "voi":
        return ConjStem+"este"
     elif person == "loro":
        return ConjStem+"essero"
   if InfinitiveEnding == "ire":
     if person == "io":
        return ConjStem+"issi"
     elif person == "tu":
        return ConjStem+"issi"
     elif person == "lui" or person == "lei":
        return ConjStem+"isse"
     elif person == "noi":
        return ConjStem+"issimo"
     elif person == "voi":
        return ConjStem+"iste"
     elif person == "loro":
        return ConjStem+"issero"

#Irregular Imperfect Indicative Function
        #Note:  The following verbs are completely regular in the imperfect indicative and are not treated separately under the Irregular Imperfect function:
        #andare, avere, cadere, dovere, potere, sapere, tenere, valere, volere, morire, salire, udire, uscire, venire
def IrregImperfectSubjunctive(verb, person):
    #dare, fare, stare, bere, essere, nuocere, dire
   WorkingVerb = ReflexiveEncoder(verb)
   #rule for forms of "dare"
   if WorkingVerb == "dare" or WorkingVerb == "ridare":
      Stem = WorkingVerb[0:len(WorkingVerb)-4]
      if person == "io":
         return Stem+"dessi"
      elif person == "tu":
         return Stem+"dessi"
      elif person == "lui" or person == "lei":
         return Stem+"desse"
      elif person == "noi":
         return Stem+"dessimo"
      elif person == "voi":
         return Stem+"deste"
      elif person == "loro":
         return Stem+"dessero"
   #rule for forms of "fare"
   if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare":
     Stem = WorkingVerb[0:len(WorkingVerb)-4]
     if person == "io":
        return Stem+"facessi"
     elif person == "tu":
        return Stem+"facessi"
     elif person == "lui" or person == "lei":
        return Stem+"facesse"
     elif person == "noi":
        return Stem+"facessimo"
     elif person == "voi":
        return Stem+"faceste"
     elif person == "loro":
        return Stem+"facessero"
   #rule for forms of "stare"
   if WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare":
     Stem = WorkingVerb[0:len(WorkingVerb)-5]
     if person == "io":
        return Stem+"stessi"
     elif person == "tu":
        return Stem+"stessi"
     elif person == "lui" or person == "lei":
        return Stem+"stesse"
     elif person == "noi":
        return Stem+"stessimo"
     elif person == "voi":
        return Stem+"steste"
     elif person == "loro":
        return Stem+"stessero"
   #rule for forms of "bere"
   if WorkingVerb == "bere":
     if person == "io":
        return "bevessi"
     elif person == "tu":
        return "bevessi"
     elif person == "lui" or person == "lei":
        return "bevesse"
     elif person == "noi":
        return "bevessimo"
     elif person == "voi":
        return "beveste"
     elif person == "loro":
        return "bevessero"
   #rule for forms of "essere"
   if WorkingVerb == "essere" or WorkingVerb == "riessere":
     Stem = WorkingVerb[0:len(WorkingVerb)-6]
     if person == "io":
        return Stem+"fossi"
     elif person == "tu":
        return Stem+"fossi"
     elif person == "lui" or person == "lei":
        return Stem+"fosse"
     elif person == "noi":
        return Stem+"fossimo"
     elif person == "voi":
        return Stem+"foste"
     elif person == "loro":
        return Stem+"fossero"
   #rule for forms of "nuocere"
   if WorkingVerb == "nuocere":
     Stem = WorkingVerb[0:len(WorkingVerb)-7]
     if person == "io":
        return Stem+"nuocessi, "+Stem+"nocessi"
     elif person == "tu":
        return Stem+"nuocessi, "+Stem+"nocessi"
     elif person == "lui" or person == "lei":
        return Stem+"nuocesse, "+Stem+"nocesse"
     elif person == "noi":
        return Stem+"nuocessimo, "+Stem+"nocessimo"
     elif person == "voi":
        return Stem+"nuoceste, "+Stem+"noceste"
     elif person == "loro":
        return Stem+"nuocessero, "+Stem+"nocessero"
   #rule for forms of "dire"
   if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
     Stem = WorkingVerb[0:len(WorkingVerb)-4]
     if person == "io":
        return Stem+"dicessi"
     elif person == "tu":
        return Stem+"dicessi"
     elif person == "lui" or person == "lei":
        return Stem+"dicesse"
     elif person == "noi":
        return Stem+"dicessimo"
     elif person == "voi":
        return Stem+"diceste"
     elif person == "loro":
        return Stem+"dicessero"

#PAST PARTICIPLE FUNCTION
def PastParticiple(verb):
    WorkingVerb = ReflexiveEncoder(verb)
    if WorkingVerb == "andare" or WorkingVerb == "dare" or WorkingVerb == "fare" or WorkingVerb == "stare" or WorkingVerb == "avere" or WorkingVerb == "bere" or WorkingVerb == "cadere" or WorkingVerb == "dovere" or WorkingVerb == "essere" or WorkingVerb == "nuocere" or WorkingVerb == "potere" or WorkingVerb == "sapere" or WorkingVerb == "tenere" or WorkingVerb == "valere" or WorkingVerb == "volere" or WorkingVerb == "dire" or WorkingVerb == "morire" or WorkingVerb == "salire" or WorkingVerb == "uscire" or WorkingVerb == "venire" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "ridare" or WorkingVerb == "affarsi" or WorkingVerb == "assuetare" or WorkingVerb == "confarsi" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "riavere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere" or WorkingVerb == "riessere" or WorkingVerb == "risapere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere" or WorkingVerb == "avvalersi" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalersi" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire" or WorkingVerb == "premorire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire" or WorkingVerb == "udire" or WorkingVerb == "riudire":
        return IrregPastParticiple(verb)
    else:
        return RegPastParticiple(verb)

#Regular Verb Participle Function
def RegPastParticiple(verb):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   Stem = WorkingVerb[0:len(WorkingVerb)-3]
   #-ARE verbs   
   if InfinitiveEnding == "are":
       return Stem+"ato"
   #-ERE verbs
   if InfinitiveEnding == "ere":
   #rule for verbs like nascere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "nasc":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]
         return Stem+"to"
   #rule for verbs like piacere, conoscere, and crescere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ac" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "sc":
         return Stem+"iuto"
   #rule for verbs like figgere, sconfiggere, struggere, leggere, reggere, rompere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ugg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "egg" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "romp" or verb == "figgere" or verb == "affliggere" or verb == "configgere" or verb == "confliggere" or verb == "defiggere" or verb == "defiggere" or verb == "friggere" or verb == "infliggere" or verb == "rifriggere" or verb == "sconfiggere" or verb == "soffriggere" or verb == "trafiggere":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"tt"
         return Stem+"o"
   #rule for verbs like crocifiggere and scindere
      if verb == "crocifiggere" or verb == "affiggere" or verb == "crocefiggere" or verb == "infiggere" or verb == "prefiggere" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "scind":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"ss"
         return Stem+"o"
   #rule for verbs like dirigere, negligere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ig":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"ett"
         return Stem+"o"
   #rule for spegnere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "gn":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"n"
         return Stem+"to"
   #rule for verbs like distinguere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ngu":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]
         return Stem+"to"
   #rule for verbs like stringere
      if WorkingVerb[len(WorkingVerb)-9:len(WorkingVerb)-3] == "string":
         Stem = WorkingVerb[0:len(WorkingVerb)-6]+"ett"
         return Stem+"o"
   #rule for verbs like vincere, fingere, spingere, spandere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "nc" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ng" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pand":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]
         return Stem+"to"
   #rule for verbs like scegliere, togliere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "gli":
         Stem = WorkingVerb[0:len(WorkingVerb)-6]+"l"
         return Stem+"to"
   #rule for verbs like svolgere, solvere, sorgere, and torcere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "lv" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "lg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "org" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "urg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "orc":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]
         return Stem+"to"
   #rule for verbs like emergere and spargere, and eccellere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "erg" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "arg" or WorkingVerb == "eccellere":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]
         return Stem+"so"   
   #rule for verbs like vedere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "ved":
         Stem = WorkingVerb[0:len(WorkingVerb)-6]+"vis"
         return Stem+"to"
   #rule for verbs like chiedere and rimanere
      if WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "chied" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "an":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]+"s"
         return Stem+"to"
   #rule for verbs like concedere, discutere
         #note: "cedere" is completely regular, but prefixed forms follow the pattern below
      if WorkingVerb == "concedere" or WorkingVerb == "retrocedere" or WorkingVerb == "succedere" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ut":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]+"ss"
         return Stem+"o"
   #rule for verbs like muovere, scuotere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuot" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "muov":
         Stem = WorkingVerb[0:len(WorkingVerb)-6]+"oss"
         return Stem+"o"
   #rule for verbs like cuocere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuoc":
         Stem = WorkingVerb[0:len(WorkingVerb)-6]+"ott"
         return Stem+"o"
   #rule for verbs like esprimere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "prim":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"ess"
         return Stem+"o"
   #rule for verbs like scrivere
      if WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "scriv":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]+"tt"
         return Stem+"o"
   #rule for verbs like persuadere, invadere, ridere, esplodere, and concludere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ad" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "id" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "od" or WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "ud":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]+"s"
         return Stem+"o"             
   #rule for verbs like ardere, and perdere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "rd":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]+"s"
         return Stem+"o"
   #rule for verbs like prendere, rendere, scendere, accendere, spendere, tendere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "rend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cend" or WorkingVerb[len(WorkingVerb)-8:len(WorkingVerb)-3] == "spend" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "tend":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"s"
         return Stem+"o"
   #rule for verbs like rispondere and nascondere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pond" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cond":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"s"
         return Stem+"to"
   #rule for verbs like fondere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "fond":
         Stem = WorkingVerb[0:len(WorkingVerb)-6]+"us"
         return Stem+"o"
   #rule for verbs like correre
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "corr":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]+"s"
         return Stem+"o"
   #rule for verbs like mettere, riflettere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "tt":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"ss"
         return Stem+"o"
   #rule for verbs like assistere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "sist":
         Stem = WorkingVerb[0:len(WorkingVerb)-3]
         return Stem+"ito"
   #rule for verbs like espellere and avellere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pell" or WorkingVerb == "avellere":
         Stem = WorkingVerb[0:len(WorkingVerb)-6]+"uls"
         return Stem+"o"
   #rule for svellere, divellere
      if WorkingVerb == "svellere" or WorkingVerb == "divellere":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"lt"
         return Stem+"o"
   #rule for verbs like assumere and presumere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "sum":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]+"nt"
         return Stem+"o"
   #rule for verbs like redimere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "dim":
         Stem = WorkingVerb[0:len(WorkingVerb)-5]+"ent"
         return Stem+"o"
   #rule for verbs like vivere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "viv":
         Stem = WorkingVerb[0:len(WorkingVerb)-6]+"viss"
         return Stem+"uto"
   #rule for regular ere verbs:
      else:
         return Stem+"uto"
   #-IRE verbs
   if InfinitiveEnding == "ire":
   #rule for verbs like aprire, coprire, soffrire
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "apr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "copr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "offr":
         Stem = WorkingVerb[0:len(WorkingVerb)-4]
         return Stem+"erto"
   #rule for regular ire verbs
      else:
        return Stem+"ito"
   #-RRE verbs
   if InfinitiveEnding == "rre":
   #rule for verbs like indurre
       if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "du":
           Stem = WorkingVerb[0:len(WorkingVerb)-4]+"o"
           return Stem+"tto"
   #rule for verbs like trarre
       elif WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "tra":
           Stem = WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3]
           return Stem+"tto"
   #rule for verbs like porre
       elif WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "po":
           Stem = WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3]+"s"
           return Stem+"to"
       
#Irregular Verb Participle Function
def IrregPastParticiple(verb):
   WorkingVerb = ReflexiveEncoder(verb)
   #rule for verbs like andare
   if WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"ato"
   #rule for forms of "dare"
   if WorkingVerb == "dare" or WorkingVerb == "ridare":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"ato"
   #rule for forms of "fare"
   if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare":
      Stem = WorkingVerb[0:len(WorkingVerb)-4]+"fat"
      return Stem+"to"
   #rule for forms of "stare"
   if WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"ato"
   #rule for forms of "avere"
   if WorkingVerb == "avere" or WorkingVerb == "riavere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"uto"
   #rule for forms of "bere"
   if WorkingVerb == "bere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]+"ev"
      return Stem+"uto"
   #rule for forms of "cadere"
   if WorkingVerb == "cadere" or WorkingVerb == "accadere" or WorkingVerb == "decadere" or WorkingVerb == "ricadere" or WorkingVerb == "scadere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"uto"
   #rule for forms of "dovere"
   if WorkingVerb == "dovere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"uto"
  #rule for forms of "essere"
   if WorkingVerb == "essere" or WorkingVerb == "riessere":
      Stem = WorkingVerb[0:len(WorkingVerb)-6]+"st"
      return Stem+"ato"
   #rule for forms of "nuocere"
   if WorkingVerb == "nuocere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"iuto, nociuto"
   #rule for forms of "potere"
   if WorkingVerb == "potere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"uto"
   #rule for forms of "sapere"
   if WorkingVerb == "sapere" or WorkingVerb == "risapere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"uto"
   #rule for forms of "tenere":
   if WorkingVerb == "tenere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"uto"
   #rule for forms of "valere":
   if WorkingVerb == "valere" or WorkingVerb == "avvalere" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]+"s"
      return Stem+"o"
   #rule for forms of "volere"
   if WorkingVerb == "volere" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"uto"
   #rule for forms of "dire"
   if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
      Stem = WorkingVerb[0:len(WorkingVerb)-4]+"det"
      return Stem+"to"
   #rule for forms of "morire"
   if WorkingVerb == "morire" or WorkingVerb == "premorire":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"to"
   #rule for forms of "salire"
   if WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"ito"
   #rule for forms of "udire"
   if WorkingVerb == "udire" or WorkingVerb == "riudire":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"ito"
   #rule for forms of "uscire"
   if WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"ito"
   #rule for forms of "venire"
   if WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
      Stem = WorkingVerb[0:len(WorkingVerb)-3]
      return Stem+"uto"

#PRESENT PERFECT INDICATIVE (PASSATO PROSSIMO) FUNCTION
def PresentPerfectInd(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if verb[len(verb)-2:len(verb)] == "si" or WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "arrivare" or WorkingVerb == "entrare" or WorkingVerb == "rientrare" or WorkingVerb == "morire" or WorkingVerb == "nascere" or WorkingVerb == "partire" or WorkingVerb == "piacere" or WorkingVerb == "rimanere" or WorkingVerb == "scendere" or WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "tornare" or WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "pervenire" or WorkingVerb == "provenire" or WorkingVerb == "sconvenire" or WorkingVerb == "svenire":
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            ConjVerb = "sono "+Participle+"/a"
        elif person == "tu":
            ConjVerb = "sei "+Participle+"/a"
        elif person == "lui" or person == "lei":
            ConjVerb = "è "+Participle+"/a"
        elif person == "noi":
            ConjVerb = "siamo "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "voi":
            ConjVerb = "siete "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "loro":
            ConjVerb = "sono "+Participle[0:len(Participle)-1]+"i/e"
        return ConjVerb
    else:
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            return "ho "+Participle
        elif person == "tu":
            return "hai "+Participle
        elif person == "lui" or person == "lei":
            return "ha "+Participle
        elif person == "noi":
            return "abbiamo "+Participle
        elif person == "voi":
            return "avete "+Participle
        elif person == "loro":
            return "hanno "+Participle

#PLUPERFECT INDICATIVE (TRAPASSATO PROSSIMO) FUNCTION
def PluperfectInd(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if verb[len(verb)-2:len(verb)] == "si" or WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "arrivare" or WorkingVerb == "entrare" or WorkingVerb == "rientrare" or WorkingVerb == "morire" or WorkingVerb == "nascere" or WorkingVerb == "partire" or WorkingVerb == "piacere" or WorkingVerb == "rimanere" or WorkingVerb == "scendere" or WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "tornare" or WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "pervenire" or WorkingVerb == "provenire" or WorkingVerb == "sconvenire" or WorkingVerb == "svenire":
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            ConjVerb = "ero "+Participle+"/a"
        elif person == "tu":
            ConjVerb = "eri "+Participle+"/a"
        elif person == "lui" or person == "lei":
            ConjVerb = "era "+Participle+"/a"
        elif person == "noi":
            ConjVerb = "eravamo "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "voi":
            ConjVerb = "eravate "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "loro":
            ConjVerb = "erano "+Participle[0:len(Participle)-1]+"i/e"
        return ConjVerb
    else:
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            return "avevo "+Participle
        elif person == "tu":
            return "avevi "+Participle
        elif person == "lui" or person == "lei":
            return "aveva "+Participle
        elif person == "noi":
            return "avevamo "+Participle
        elif person == "voi":
            return "avevate "+Participle
        elif person == "loro":
            return "avevano "+Participle

#REMOTE PLUPERFECT INDICATIVE (TRAPASSATO REMOTO) FUNCTION
def RemotePluperfectInd(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if verb[len(verb)-2:len(verb)] == "si" or WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "arrivare" or WorkingVerb == "entrare" or WorkingVerb == "rientrare" or WorkingVerb == "morire" or WorkingVerb == "nascere" or WorkingVerb == "partire" or WorkingVerb == "piacere" or WorkingVerb == "rimanere" or WorkingVerb == "scendere" or WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "tornare" or WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "pervenire" or WorkingVerb == "provenire" or WorkingVerb == "sconvenire" or WorkingVerb == "svenire":
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            ConjVerb = "fui "+Participle+"/a"
        elif person == "tu":
            ConjVerb = "fosti "+Participle+"/a"
        elif person == "lui" or person == "lei":
            ConjVerb = "fu "+Participle+"/a"
        elif person == "noi":
            ConjVerb = "fummo "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "voi":
            ConjVerb = "foste "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "loro":
            ConjVerb = "furono "+Participle[0:len(Participle)-1]+"i/e"
        return ConjVerb
    else:
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            return "ebbi "+Participle
        elif person == "tu":
            return "avesti "+Participle
        elif person == "lui" or person == "lei":
            return "ebbe "+Participle
        elif person == "noi":
            return "avemmo "+Participle
        elif person == "voi":
            return "aveste "+Participle
        elif person == "loro":
            return "ebbero "+Participle

#PRESENT PERFECT SUBJUNCTIVE (PASSATO) FUNCTION
def PresentPerfectSubjunctive(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if verb[len(verb)-2:len(verb)] == "si" or WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "arrivare" or WorkingVerb == "entrare" or WorkingVerb == "rientrare" or WorkingVerb == "morire" or WorkingVerb == "nascere" or WorkingVerb == "partire" or WorkingVerb == "piacere" or WorkingVerb == "rimanere" or WorkingVerb == "scendere" or WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "tornare" or WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "pervenire" or WorkingVerb == "provenire" or WorkingVerb == "sconvenire" or WorkingVerb == "svenire":
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            ConjVerb = "sia "+Participle+"/a"
        elif person == "tu":
            ConjVerb = "sia "+Participle+"/a"
        elif person == "lui" or person == "lei":
            ConjVerb = "sia "+Participle+"/a"
        elif person == "noi":
            ConjVerb = "siamo "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "voi":
            ConjVerb = "siate "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "loro":
            ConjVerb = "siano "+Participle[0:len(Participle)-1]+"i/e"
        return ConjVerb
    else:
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            return "abbia "+Participle
        elif person == "tu":
            return "abbia "+Participle
        elif person == "lui" or person == "lei":
            return "abbia "+Participle
        elif person == "noi":
            return "abbiamo "+Participle
        elif person == "voi":
            return "abbiate "+Participle
        elif person == "loro":
            return "abbiano "+Participle

#PlUPERFECT SUBJUNCTIVE (TRAPASSATO) FUNCTION
def PluperfectSubjunctive(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if verb[len(verb)-2:len(verb)] == "si" or WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "arrivare" or WorkingVerb == "entrare" or WorkingVerb == "rientrare" or WorkingVerb == "morire" or WorkingVerb == "nascere" or WorkingVerb == "partire" or WorkingVerb == "piacere" or WorkingVerb == "rimanere" or WorkingVerb == "scendere" or WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "tornare" or WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "pervenire" or WorkingVerb == "provenire" or WorkingVerb == "sconvenire" or WorkingVerb == "svenire":
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            ConjVerb = "fossi "+Participle+"/a"
        elif person == "tu":
            ConjVerb = "fossi "+Participle+"/a"
        elif person == "lui" or person == "lei":
            ConjVerb = "fosse "+Participle+"/a"
        elif person == "noi":
            ConjVerb = "fossimo "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "voi":
            ConjVerb = "foste "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "loro":
            ConjVerb = "fossero "+Participle[0:len(Participle)-1]+"i/e"
        return ConjVerb
    else:
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            return "avessi "+Participle
        elif person == "tu":
            return "avessi "+Participle
        elif person == "lui" or person == "lei":
            return "avesse "+Participle
        elif person == "noi":
            return "avessimo "+Participle
        elif person == "voi":
            return "aveste "+Participle
        elif person == "loro":
            return "avessero "+Participle

#FUTURE PERFECT INDICATIVE (FUTURO ANTERIORE) FUNCTION
def FuturePerfectInd(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if verb[len(verb)-2:len(verb)] == "si" or WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "arrivare" or WorkingVerb == "entrare" or WorkingVerb == "rientrare" or WorkingVerb == "morire" or WorkingVerb == "nascere" or WorkingVerb == "partire" or WorkingVerb == "piacere" or WorkingVerb == "rimanere" or WorkingVerb == "scendere" or WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "tornare" or WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "pervenire" or WorkingVerb == "provenire" or WorkingVerb == "sconvenire" or WorkingVerb == "svenire":
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            ConjVerb = "sarò "+Participle+"/a"
        elif person == "tu":
            ConjVerb = "sarai "+Participle+"/a"
        elif person == "lui" or person == "lei":
            ConjVerb = "sarà "+Participle+"/a"
        elif person == "noi":
            ConjVerb = "saremo "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "voi":
            ConjVerb = "sarete "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "loro":
            ConjVerb = "saranno "+Participle[0:len(Participle)-1]+"i/e"
        return ConjVerb
    else:
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            return "avrò "+Participle
        elif person == "tu":
            return "avrai "+Participle
        elif person == "lui" or person == "lei":
            return "avrà "+Participle
        elif person == "noi":
            return "avremo "+Participle
        elif person == "voi":
            return "avrete "+Participle
        elif person == "loro":
            return "avranno "+Participle

#PERFECT CONDITIONAL (CONDITIONALE PASSATO) FUNCTION
def PerfectConditional(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if verb[len(verb)-2:len(verb)] == "si" or WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "arrivare" or WorkingVerb == "entrare" or WorkingVerb == "rientrare" or WorkingVerb == "morire" or WorkingVerb == "nascere" or WorkingVerb == "partire" or WorkingVerb == "piacere" or WorkingVerb == "rimanere" or WorkingVerb == "scendere" or WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "tornare" or WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "pervenire" or WorkingVerb == "provenire" or WorkingVerb == "sconvenire" or WorkingVerb == "svenire":
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            ConjVerb = "sarei "+Participle+"/a"
        elif person == "tu":
            ConjVerb = "saresti "+Participle+"/a"
        elif person == "lui" or person == "lei":
            ConjVerb = "sarebbe "+Participle+"/a"
        elif person == "noi":
            ConjVerb = "saremmo "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "voi":
            ConjVerb = "sareste "+Participle[0:len(Participle)-1]+"i/e"
        elif person == "loro":
            ConjVerb = "sarebbero "+Participle[0:len(Participle)-1]+"i/e"
        return ConjVerb
    else:
        Participle = PastParticiple(WorkingVerb)
        if person == "io":
            return "avrei "+Participle
        elif person == "tu":
            return "avresti "+Participle
        elif person == "lui" or person == "lei":
            return "avrebbe "+Participle
        elif person == "noi":
            return "avremmo "+Participle
        elif person == "voi":
            return "avreste "+Participle
        elif person == "loro":
            return "avrebbero "+Participle

#IMPERATIVE FUNCTION
def Imperative(verb, person):
    WorkingVerb = ReflexiveEncoder(verb)
    if WorkingVerb == "andare" or WorkingVerb == "dare" or WorkingVerb == "fare" or WorkingVerb == "stare" or WorkingVerb == "avere" or WorkingVerb == "bere" or WorkingVerb == "cadere" or WorkingVerb == "dovere" or WorkingVerb == "essere" or WorkingVerb == "potere" or WorkingVerb == "sapere" or WorkingVerb == "tenere" or WorkingVerb == "valere" or WorkingVerb == "volere" or WorkingVerb == "dire" or WorkingVerb == "morire" or WorkingVerb == "salire" or WorkingVerb == "uscire" or WorkingVerb == "venire" or WorkingVerb == "malandare" or WorkingVerb == "riandare" or WorkingVerb == "ridare" or WorkingVerb == "affarsi" or WorkingVerb == "assuetare" or WorkingVerb == "confarsi" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare" or WorkingVerb == "riavere" or WorkingVerb == "riessere" or WorkingVerb == "risapere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere" or WorkingVerb == "avvalersi" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalersi" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire" or WorkingVerb == "premorire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
      if person == "tu": 
          if verb[len(verb)-2:len(verb)] == "si":
              FinStem = IrregImperativeConj(verb, person)
          if verb[-1] == "e":
              FinStem = IrregImperativeConj(WorkingVerb, person)
      else:
          FinStem = IrregImperativeConj(WorkingVerb, person)
    else:
       FinStem = RegImperativeConj(WorkingVerb, person)
    #Imperative Reflexive Decoder (Enclitic):  After verb is parsed, adds enclitic reflexive pronouns to finite verb forms for imperative mood.
    if person == "io":
       return FinStem
    if person == "tu":
       return FinStem+"ti"
    if person == "lui" or person == "lei":
       return FinStem+"si"
    if person == "noi":
       return FinStem+"ci"
    if person == "voi":
       return FinStem+"vi"
    if person == "loro":
       return FinStem+"si"

#Regular Imperative Stem Function
def RegImperativeStem(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   Stem = WorkingVerb[0:len(WorkingVerb)-3]
   StemEnding = Stem[len(Stem)-1]
   #-ARE verbs:
   if InfinitiveEnding == "are":
   #rule for stem in hard or soft "c" or "g": mancare, indagare
      if StemEnding == "c" or StemEnding == "g":
         if person == "lui" or person == "lei" or person == "noi" or person == "loro":
            return Stem+"h"
         else:
            return Stem
   #rule for stem in "i"
      if StemEnding == "i":
         #rule for verbs like sviare "tu svii"
         if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "vvi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "svi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "nvi" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "bli" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "spi" or WorkingVerb == "desiare" or WorkingVerb == "deviare" or WorkingVerb == "forviare" or WorkingVerb == "fuorviare" or WorkingVerb == "piare" or WorkingVerb == "sciare" or WorkingVerb == "striare":
             if person == "noi":
                 Stem = WorkingVerb[0:len(verb)-4]
                 return Stem
             else:
                 return Stem
         #rule for verbs like lasciare, cambiare, mangiare
             #conjugational ending begins with 'i'
         elif person == "lui" or person == "lei" or person == "noi" or person == "loro":
            Stem = WorkingVerb[0:len(verb)-4]
            return Stem
             #conjugational ending does not begin with 'i'
         else:
            return Stem
   #rule for regular -are verbs, like parlare
      else:
         return Stem
   #-ERE verbs
   if InfinitiveEnding == "ere":
   #rule for verbs like piacere
      if StemEnding == "c" and Stem[len(Stem)-2] == "a":
         if person == "lui" or person == "lei" or person == "loro":
            return Stem+"ci"
         elif person == "noi":
            return Stem+"c"
         else:
            return Stem
   #rule for verbs like cuocere
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "cuoc":
         if person == "lui" or person == "lei" or person == "loro":
            return Stem+"i"
         else:
            return Stem
   #rule for verbs like rimanere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "an":
         if person == "lui" or person == "lei" or person == "loro":
            return Stem+"g"
         else:
            return Stem
   #rule for spegnere
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "gn":
         if person == "lui" or person == "lei" or person == "loro":
            return WorkingVerb[0:len(WorkingVerb)-5]+"ng"
         else:
            return Stem
   #rule for verbs like sedere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "sed":
         if person == "io" or person == "tu" or person == "lui" or person == "lei" or person == "loro":         
            return WorkingVerb[0:len(WorkingVerb)-5]+"ied"
         else:
            return Stem
   #rule for verbs like scegliere, togliere
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "gli":
         if person == "lui" or person == "lei" or person == "loro":
            return WorkingVerb[0:len(WorkingVerb)-6]+"lg"
         if person == "tu" or person == "noi":
            Stem = WorkingVerb[0:len(WorkingVerb)-4]
            return Stem
         else:
            return Stem
   #rule for regular verbs like credere
      else:
         return Stem
   #-IRE verbs:
   if InfinitiveEnding == "ire":
      #rule for verbs like dormire, servire, offrire, aprire, pentire, seguire, fuggire
      if WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "dorm" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "pent" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "serv" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "part" or WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "apr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "copr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "soffr" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "segu" or WorkingVerb[len(WorkingVerb)-7:len(WorkingVerb)-3] == "fugg":
         return Stem
      #rule for cucire
      if WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "cuc":
         if person == "lui" or person == "lei" or person == "loro":
            return Stem+"i"
         else:
            return Stem
      #rule for verbs like finire (-ISC- verbs)
      else:
         if person == "tu" or person == "lui" or person == "lei" or person == "loro":
            return Stem+"isc"
         else:
            return Stem
   #-RRE verbs:
   if InfinitiveEnding == "rre":
      #rule for verbs like condurre
      if WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "du":
         return Stem+"c"
      #rule for verbs like trarre
      elif WorkingVerb[len(WorkingVerb)-6:len(WorkingVerb)-3] == "tra":
         if person == "lui" or person == "lei" or person == "loro":
            return Stem+"gg"
         else:
            return Stem
      #rule for verbs like porre
      elif WorkingVerb[len(WorkingVerb)-5:len(WorkingVerb)-3] == "po":
         if person == "lui" or person == "lei" or person == "loro":
            return Stem+"ng"
         else:
            return Stem+"n"

#Regular Imperative Conjugator Function
def RegImperativeConj(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   ConjStem = RegImperativeStem(WorkingVerb, person)
   #Imperative conjugations:
   if InfinitiveEnding == "are":
     if person == "io":
        return "--"
     elif person == "tu":
        return ConjStem+"a"
     elif person == "lui" or person == "lei":
        return ConjStem+"i"
     elif person == "noi":
        return ConjStem+"iamo"
     elif person == "voi":
        return ConjStem+"ate"
     elif person == "loro":
        return ConjStem+"ino"      
   if InfinitiveEnding == "ere" or InfinitiveEnding == "rre" or InfinitiveEnding == "ire":
     if person == "io":
        return "--"
     elif person == "tu":
        return ConjStem+"i"
     elif person == "lui" or person == "lei":
        return ConjStem+"a"
     elif person == "noi":
        return ConjStem+"iamo"
     elif person == "voi":
         if InfinitiveEnding == "ire":
            return ConjStem+"ite"
         else:
            return ConjStem+"ete"
     elif person == "loro":
        return ConjStem+"ano"

#Irregular Imperative Stem Function
def IrregImperativeStem(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   #rule for forms of andare
   if WorkingVerb == "andare" or WorkingVerb == "malandare" or WorkingVerb == "riandare":
         if person == "tu":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "v"
             return Stem
         elif person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "vad"
             return Stem
         elif person == "noi" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "and"
             return Stem
   #rule for forms of "dare"
   if WorkingVerb == "dare" or WorkingVerb == "ridare":
         if person == "tu":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "d"
             return Stem
         elif person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "di"
             return Stem
         elif person == "noi" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "d"
             return Stem
   #rule for forms of "fare"
   if WorkingVerb == "fare" or WorkingVerb == "affare" or WorkingVerb == "assuetare" or WorkingVerb == "confare" or WorkingVerb == "contraffare" or WorkingVerb == "disfare" or WorkingVerb == "liquefare" or WorkingVerb == "mansuefare" or WorkingVerb == "putrefare" or WorkingVerb == "rarefare" or WorkingVerb == "rifare" or WorkingVerb == "sfare" or WorkingVerb == "soddisfare" or WorkingVerb == "sopraffare" or WorkingVerb == "strafare" or WorkingVerb == "stupefare" or WorkingVerb == "torrefare" or WorkingVerb == "tumefare":
         if person == "tu" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "f"
             return Stem
         elif person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "facci"
             return Stem
         elif person == "noi":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "facc"
             return Stem
   #rule for forms of "stare"
   if WorkingVerb == "stare" or WorkingVerb == "instare" or WorkingVerb == "soprastare" or WorkingVerb == "sottostare":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "sti"
             return Stem
         elif person == "tu" or person == "noi" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "st"
             return Stem
   #rule for forms of "avere"
   if WorkingVerb == "avere" or WorkingVerb == "riavere":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "abbi"
             return Stem
         elif person == "tu" or person == "noi":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "abb"
             return Stem
         elif person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "abbia"
             return Stem
   #rule for forms of "bere"
   if WorkingVerb == "bere":
         if person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "beve"
             return Stem
         else:
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "bev"
             return Stem
   #rule for forms of "essere"
   if WorkingVerb == "essere" or WorkingVerb == "riessere":
         if person == "noi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "s"
             return Stem
         elif person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "si"
             return Stem
         elif person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "sia"
             return Stem
   #rule for forms of "nuocere"
   if WorkingVerb == "nuocere":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-7] + "nuocci"
             return Stem
         elif person == "tu" or person == "noi":
             Stem = WorkingVerb[0:len(WorkingVerb)-7] + "nuoc"
             return Stem
         elif person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-7] + "nuoce"
             return Stem
   #rule for forms of "sapere"
   if WorkingVerb == "sapere" or WorkingVerb == "risapere":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "sappi"
             return Stem
         elif person == "tu" or person == "noi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "sapp"
             return Stem
         elif person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "sappia"
             return Stem
   #rule for forms of "tenere":
   if WorkingVerb == "tenere" or WorkingVerb == "appartenere" or WorkingVerb == "astenere" or WorkingVerb == "attenere" or WorkingVerb == "contenere" or WorkingVerb == "detenere" or WorkingVerb == "intrattenere" or WorkingVerb == "mantenere" or WorkingVerb == "ottenere" or WorkingVerb == "partenere" or WorkingVerb == "rattenere" or WorkingVerb == "riottenere" or WorkingVerb == "risostenere" or WorkingVerb == "ritenere" or WorkingVerb == "sostenere" or WorkingVerb == "trattenere":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "teng"
             return Stem
         elif person == "tu":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "tien"
             return Stem
         elif person == "noi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "ten"
             return Stem
         elif person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "tene"
             return Stem
   #rule for forms of "valere":
   if WorkingVerb == "valere" or WorkingVerb == "avvalere" or WorkingVerb == "calere" or WorkingVerb == "equivalere" or WorkingVerb == "invalere" or WorkingVerb == "prevalere" or WorkingVerb == "riavalere":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "valg"
             return Stem
         elif person == "tu" or person == "noi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "val"
             return Stem
         elif person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "vale"
             return Stem
   #rule for forms of "volere"
   if WorkingVerb == "volere" or WorkingVerb == "benvolere" or WorkingVerb == "disvolere" or WorkingVerb == "malvolere" or WorkingVerb == "rivolere":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "vogli"
             return Stem
         elif person == "tu" or person == "noi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "vogl"
             return Stem
         elif person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "voglia"
             return Stem
   #rule for forms of "dire"
   if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
         if person == "lui" or person == "lei" or person == "noi" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "dic"
             return Stem
         elif person == "tu" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-4] + "d"
             return Stem
   #rule for forms of "morire"
   if WorkingVerb == "morire" or WorkingVerb == "premorire":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "muoi"
             return Stem
         elif person == "noi" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "mor"
             return Stem
         elif person == "tu":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "muor"
             return Stem
   #rule for forms of "salire"
   if WorkingVerb == "salire" or WorkingVerb == "assalire" or WorkingVerb == "riassalire" or WorkingVerb == "risalire":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "salg"
             return Stem
         elif person == "tu" or person == "noi" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "sal"
             return Stem
   #rule for forms of "udire"
   if WorkingVerb == "udire" or WorkingVerb == "riudire":
         if person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "od"
             return Stem
         elif person == "noi" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-5] + "ud"
             return Stem
   #rule for forms of "uscire"
   if WorkingVerb == "uscire" or WorkingVerb == "fuoiriuscire" or WorkingVerb == "fuoruscire" or WorkingVerb == "riuscire":
         if person == "tu" or person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "esc"
             return Stem
         elif person == "noi" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "usc"
             return Stem
   #rule for forms of "venire"
   if WorkingVerb == "venire" or WorkingVerb == "addivenire" or WorkingVerb == "avvenire" or WorkingVerb == "circonvenire" or WorkingVerb == "contravvenire" or WorkingVerb == "convenire" or WorkingVerb == "divenire" or WorkingVerb == "intervenire" or WorkingVerb == "invenire" or WorkingVerb == "pervenire" or WorkingVerb == "prevenire" or WorkingVerb == "provenire" or WorkingVerb == "riconvenire" or WorkingVerb == "rinvenire" or WorkingVerb == "risovvenire" or WorkingVerb == "sconvenire" or WorkingVerb == "sopravvenire" or WorkingVerb == "sovenire" or WorkingVerb == "sovvenire" or WorkingVerb == "svenire":
         if person == "lui" or person == "lei" or person == "loro":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "veng"
             return Stem
         elif person == "noi" or person == "voi":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "ven"
             return Stem
         elif person == "tu":
             Stem = WorkingVerb[0:len(WorkingVerb)-6] + "vien"
             return Stem

#Irregular Imperative Conjugator Function
def IrregImperativeConj(verb, person):
   WorkingVerb = ReflexiveEncoder(verb)
   InfinitiveEnding = WorkingVerb[len(WorkingVerb)-3:len(WorkingVerb)]
   ConjStem = IrregImperativeStem(WorkingVerb, person)
   if InfinitiveEnding == "are":
       if person == "io":
           return "--"
       elif person == "tu":
           if verb[len(verb)-2:len(verb)] == "si":
               return ConjStem+"at"
           if verb[-1] == "e":
               return ConjStem+"ai, "+ConjStem+"a'"
       elif person == "lui" or person == "lei":
           return ConjStem+"a"
       elif person == "noi":
           return ConjStem+"iamo"
       elif person == "voi":
           return ConjStem+"ate"
       elif person == "loro":
           return ConjStem+"ano"
   if InfinitiveEnding == "ere":
     if WorkingVerb == "dovere" or WorkingVerb == "potere":
         return "--"
     elif person == "io":
        return "--"
     elif person == "tu":
        return ConjStem+"i"
     elif person == "lui" or person == "lei":
        return ConjStem+"a"
     elif person == "noi":
        return ConjStem+"iamo"
     elif person == "voi":
        return ConjStem+"te"
     elif person == "loro":
        return ConjStem+"ano"
   if InfinitiveEnding == "ere" or InfinitiveEnding == "rre" or InfinitiveEnding == "ire":
     if person == "io":
        return "--"
     elif person == "tu":
            if WorkingVerb == "dire" or WorkingVerb == "addire" or WorkingVerb == "benedire" or WorkingVerb == "contraddire" or WorkingVerb == "disdire" or WorkingVerb == "indire" or WorkingVerb == "interdire" or WorkingVerb == "maledire" or WorkingVerb == "predire" or WorkingVerb == "ridire" or WorkingVerb == "stramaledire":
                if verb[len(verb)-2:len(verb)] == "si":
                    return ConjStem+"it"
                else:
                    return ConjStem+"i'"
            else:
                return ConjStem+"i"
     elif person == "lui" or person == "lei":
        return ConjStem+"a"
     elif person == "noi":
        return ConjStem+"iamo"
     elif person == "voi":
        return ConjStem+"ite"
     elif person == "loro":
        return ConjStem+"ano"