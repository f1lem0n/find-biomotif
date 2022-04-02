# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:07:46 2022

@author: hajdy
"""

def openseq(file):
    
    '''Opens file containing analysed sequence and deletes all '\\n' signs. 
    Assigns header and sequence to two different variables and returns them.'''
    
    seq = open(file)
    seq = seq.readlines()
    seqstr = ''
    for line in seq:
        if '>' not in line:
            line = line.lower()#.replace('\n', '')
            seqstr += line
        else:
            header = line
    seqstr = seqstr.replace('\n', '')
    seq = seqstr
    return header, seq


def findmotif(seq, motif):
    
    '''Finds indices of all motif appearances in seq.'''
    
    motif = motif.lower()
    temp_seq = seq
    prev_idx = 0
    idxs = []
    for i in range(temp_seq.count(motif)):
        temp_idx = temp_seq.index(motif)      
        temp_seq = temp_seq[temp_idx+1:]       
        idxs.append(temp_idx + prev_idx)
        prev_idx += temp_idx + 1
    
    return idxs

motif = 'gat'
file = r'seq.fasta'
header, seq = openseq(file)
idxs = findmotif(seq, motif)

print(idxs)