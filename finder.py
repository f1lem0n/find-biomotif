# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:07:46 2022

@author: f1lem0n
"""

import sys

def openseq(file):
    
    '''Opens file containing analysed sequence and deletes all '\\n' signs. 
    Assigns header and sequence to two different variables and returns them. 
    
    (file) - Pathway (str) that is generated by filepath() in main.py module.'''
    
    try:
        seq = open(file)
        seq = seq.readlines()
        strseq = ''
        for line in seq:
            if '>' not in line:
                line = line.lower()
                strseq += line
            else:
                header = line
        seq = strseq.replace('\n', '')
    except FileNotFoundError:
        print('Specified file path does not exist.')
        sys.exit()
        
    return header, seq


def findmotif(seq, motif):
    
    '''Finds and returns indices of all motif appearances in seq.
    
    (seq) - String generated by openseq(). Contains sequence, does not contain 
    header.
    (motif) - String generated by specmotif() in main.py module.'''
    
    motif = motif.lower()
    temp_seq = seq
    prev_idx = 0
    idxs = []
    for i in range(temp_seq.count(motif)):
        temp_idx = temp_seq.index(motif)      
        temp_seq = temp_seq[temp_idx + 1:]       
        idxs.append(temp_idx + prev_idx)
        prev_idx += temp_idx + 1
    
    return idxs


def motifcaps(seq, idxs, motif):
    
    '''Capitalizes all motif apearances in seq and returns string with capped
    motif substrings. 
    
    (idxs) - List of indices of all motif appearances in seq.'''
    
    seq_capped = ''
    
    for idx, i in enumerate(seq):
        if idx in idxs:
            seq_capped += seq[idx:idx + len(motif)].upper()
        else:
            seq_capped += seq[idx]
            
    return seq_capped


def lnsep(lenght):
    
    '''Creates a line separator of given lenght. 
    
    (lenght) - Any integer.'''
    
    line = ''
    for i in range(lenght):
        line += '-'
    line += '\n'
    
    return line


def outwrapper(idxs, header, seq_capped):
    
    '''Creates formatted output.'''
    
    seq_lenght = f'sequence lenght:{len(seq_capped):24}\n'
    n_sites = f'motif sites found:{len(idxs):22}\n'
    if len(idxs) != 0:
        motif_sites = 'motif sites:\n'
        newln = 0
        for idx in idxs:
            motif_site = f'{idx}'
            motif_sites += f'{motif_site:12}'
            newln += 1
            if newln == 4:
                newln = 0
                motif_sites += '\n'
        if motif_sites[-1:] == '\n':
            motif_sites = motif_sites[:-1]
        motif_sites += '\n' + lnsep(40)
    else:
        motif_sites = ''
    
    header_lenght = len(header) - 1
    wrapped_seq = ''
    prev_lenght = 0
    for i in range(len(seq_capped)//header_lenght):
        wrapped_seq += seq_capped[prev_lenght:header_lenght + prev_lenght] + '\n'
        prev_lenght += header_lenght
    wrapped_seq += seq_capped[prev_lenght:] + '\n'
    
    wrapped_output = (lnsep(40), 
                      seq_lenght, 
                      n_sites, 
                      lnsep(40),
                      motif_sites,
                      header, 
                      wrapped_seq)
    
    return wrapped_output