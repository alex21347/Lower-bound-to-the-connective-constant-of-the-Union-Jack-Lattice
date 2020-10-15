#Kestons Method of Irreducible Bridges Applied to the Union Jack Lattice

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm 

def take_a_step_bridges(saws):
    
    #This function returns the bridges of a given length on the Union Jack Lattice
    
    if saws[0,0,0] == 0:
        x_0 = 0.5
    else:
        x_0 = 1
    
    new_saws = np.array([[[]]]);
    for i in tqdm(range(0,saws.shape[0])):
        if np.floor(saws[i,-1,0]) - saws[i,-1,0] == 0:
            steps = [[0,1],
                     [1,0],
                     [0,-1],
                     [-1,0],
                     [0.5,0.5],
                     [0.5,-0.5],
                     [-0.5,-0.5],
                     [-0.5,0.5]]
            for j in steps:
                new_pos_ij = np.array([saws[i,-1] + j])
                if np.any(np.all(saws[i,:]==new_pos_ij,axis=1)==True) or new_pos_ij[0][0]<x_0:
                    continue
                else:
                    new_walk_ij = np.append(saws[i,:], new_pos_ij,axis = 0)
                    new_walk_ij = np.array([new_walk_ij])
                    if new_saws.shape[2] == 0:
                        new_saws = new_walk_ij
                    else:
                       new_saws = np.append(new_saws, new_walk_ij,axis = 0)
        else:
            steps =  [[0.5,0.5],
                     [0.5,-0.5],
                     [-0.5,-0.5],
                     [-0.5,0.5]]
            
            for j in steps:
                new_pos_ij = np.array([saws[i,-1] + j])
                
                if np.any(np.all(saws[i,:]==new_pos_ij,axis=1)==True) or new_pos_ij[0][0]<x_0:
                    continue
                else:
                    new_walk_ij = np.append(saws[i,:], new_pos_ij,axis = 0)
                    new_walk_ij = np.array([new_walk_ij])
                    if new_saws.shape[2] == 0:
                        new_saws = new_walk_ij
                    else:
                        new_saws = np.append(new_saws, new_walk_ij,axis = 0)
    c_n = int(new_saws.shape[0])
    return new_saws,c_n

#%%
    
N = 4    #length of bridge
b_n = [] #array to store the number of brigdes of length n
b_n_l = np.zeros((N,2*N))

#enumarating brigdes beginning at vertex class 0
for n in range(1,N):
    new_saws = np.array([[[0,0],[1,0]]])
    for i in range(0,n):
        new_saws,c_n = take_a_step_bridges(new_saws)
    
    K = []
    new_bridges = new_saws
    for k in range(0,new_saws.shape[0]):
        if np.any(new_saws[k,:n+1,0] > new_saws[k,n+1,0]):
            K = np.append(K,k)
            
    new_bridges = np.delete(new_bridges,K,0)
    for i in range(0,new_bridges.shape[0]):
        b_n_l[n,int(2*new_bridges[i,n+1,0]-1)] = b_n_l[n,int(2*new_bridges[i,n+1,0])-1]+1
        
    b_n = np.append(b_n,new_bridges.shape[0])
    
b_n1 = []
b_n_l1 = np.zeros((N,2*N))

#enumarating brigdes beginning at vertex class 1
for n in range(1,N):
    new_saws1 = np.array([[[0,0],[0.5,0.5]]])
    for i in range(0,n):
        new_saws1,c_n1 = take_a_step_bridges(new_saws1)
    
    K1 = []
    new_bridges1 = new_saws1
    for k in range(0,new_saws1.shape[0]):
        if np.any(new_saws1[k,:n+1,0] > new_saws1[k,n+1,0]):
            K1 = np.append(K1,k)
            
    new_bridges1 = np.delete(new_bridges1,K1,0)  
    for i in range(0,new_bridges1.shape[0]):
        b_n_l1[n,int(2*new_bridges1[i,n+1,0])-1]=b_n_l1[n,int(2*new_bridges1[i,n+1,0])-1]+1
    b_n1 = np.append(b_n1,new_bridges1.shape[0])
    
    
b_n_l2 = b_n_l + b_n_l1
    
#summing the bridges of span l and similar length n
sums = np.zeros((b_n_l2.shape[0],1))
for i in range(b_n_l2.shape[0]):
    sums[i] = b_n_l2[i,:].sum()