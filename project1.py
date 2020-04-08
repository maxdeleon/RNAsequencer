


# too lazy to add a method to use a input file and convert it to a string since this was just for fun 
# may add that soon though
RNAsequence1 = "auuaaagguuuauaccuucccagguaacaaaccaaccaacuuucgaucucuuguagaucuguucucuaaacgaacuuuaaaaucuguguggcugucacucggcugcaugcuuagugcacucacgcaguauaauuaauaacuaauuacugucguugacaggacacgaguaacucgucuaucuucugcaggcugcuuacgguuucguccguguugcagccgaucaucagcacaucuagguuucguccgggugugaccgaaagguaag"

# RNA codon to amino acid dictionary 
RNA2AA ={
        #Phenylalanine
        "UUU":"Phe/F", "UUC":"Phe/F",        
        #Leucine
        "UUA":"Leu/L", "UUG":"Leu/L", "CUU":"Leu/L", "CUC":"Leu/L", "CUA":"Leu/L", "CUG":"Leu/L",
        #Isoleucine
        "AUU":"Ile/I", "AUC":"Ile/I", "AUA":"Ile/I",
        #Methionine
        "AUG":"Met/M",
        #Valine
        "GUU":"Val/V", "GUC":"Val/V", "GUA":"Val/V", "GUG":"Val/V",
        #Serine
        "UCU":"Ser/S", "UCC":"Ser/S", "UCA":"Ser/S", "UCG":"Ser/S", "AGU":"Ser/S", "AGC":"Ser/S",
        #Proline
        "CCU":"Pro/P", "CCC":"Pro/P", "CCA":"Pro/P", "CCG":"Pro/P",
        #Threonine
        "ACU":"Thr/T", "ACC":"Thr/T", "ACA":"Thr/T", "ACG":"Thr/T",
        #Alanine
        "GCU":"Ala/A", "GCC":"Ala/A", "GCA":"Ala/A", "GCG":"Ala/A",
        #Tyrosine
        "UAU":"Tyr/Y", "UAC":"Tyr/Y",
        #Stop Ochre, Amber, Opal
        "UAA":"STP/0", "UAG":"STP/0", "UGA":"STP/0",
        #Histidine
        "CAU":"His/H", "CAC":"His/H",      
        #Glutamine 
        "CAA":"Gln/Q", "CAG":"Gln/Q",
        #Asparagine
        "AAU":"Asn/N", "AAC":"Asn/N",
        #Lysine
        "AAA":"Lys/K", "AAG":"Lys/K",
        #Aspartic acid
        "GAU":"Asp/D", "GAC":"Asp/D",
        #Glutamic acid
        "GAA":"Glu/E", "GAG":"Glu/E",
        #Cytesine
        "UGU":"Cys/C", "UGC":"Cys/C",
        #Tryptophan
        "UGG":"Trp/W",
        #Arginine
        "CGU":"Arg/R", "CGC":"Arg/R", "CGA":"Arg/R", "CGG":"Arg/R","AGA":"Arg/R", "AGG":"Arg/R",
        #Glycine
        "GGU":"Gly/G", "GGC":"Gly/G", "GGA":"Gly/G", "GGG":"Gly/G" 
        }

def sequenceToAA(NA2AA,sequence, type):

   

    print("-----------INFO------------")
    print("input RNA size sequence size: " + str(len(sequence)))
    print("number of codons/amino acids: " + str(len(sequence)//3 ))
    print("number of remaining nucleotides/ error: " +  str(len(sequence)%3) )
    print("-----------------------------")
    print("==============================")
   
   # print(RNA2AA)
   

    AASequence =''
    codonSequence =''
    a = 0
    b = 3


    while b <= len(sequence):
        
        codon = sequence[a:b].upper()

        if codon in NA2AA:
            AA = NA2AA[codon][4]
            
            if AA == '0':


                AA = '\n'
                codon = '\n'
                


            codonSequence = codonSequence + codon 
            AASequence = AASequence + AA

        a = b
        b = b + 3
    
    if type == "AA":
        return AASequence
    if type == "RNA":
        return codonSequence
   
#old (origional) 
#just here for reference
def makeEasy(sequence):
    parsedSequence =''
    a = 0
    b = 3

    while b <= len(sequence):
        chunk = sequence[a:b]

        if chunk in ["UAA","UAG", "UGA"]:
            
            chunk = '\n'

        parsedSequence = parsedSequence + " " + chunk
        a = b
        b = b + 3
    
        
    return parsedSequence

 
for key, value in RNA2AA.items():
    print(key, ' : ', value)

print("-----------------------------")
print("RNA to Amino Acid dictionary")
print("==============================")

print("=============RNA=============")
print( sequenceToAA(RNA2AA,RNAsequence1, "RNA")) 
print("==============================")


print("=============AA=============")
print( sequenceToAA(RNA2AA,RNAsequence1, "AA")) 
print("==============================")





