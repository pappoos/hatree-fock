#hf energy closed shell molecule
import numpy as np
from no_of_electron import no_of_e
from distance import find_distance
from file_read import file_read

#import geometry
geom_input=open('geom.dat')
geom_content=geom_input.readlines()
geom_input.close()

#print(geom_content)

# storing input in list

temp_geom=[]
for line in geom_content:
    v_line=line.rstrip()
    if len(v_line)>0: # check for blank lines
     temp_geom.append(v_line.split())
#print(temp_geom)

#no of atoms

NATOM=int(temp_geom[0][0])
print('Total no of atom '+str(NATOM))
ATOM_SYMBOL=[] # this list contains the atom symbols
GEOM=[] # store cartesian coordinate


for i in range(1,NATOM+1): 
 ATOM_SYMBOL.append(temp_geom[i][0])
 GEOM.append(temp_geom[i][1:4])

#print('ATOM SYMBOLS')
#print(ATOM_SYMBOL)
#print('CARTESIAN COORDINATES IN a.u')
#print(GEOM)


#Number of electrons

NE=0
for i in range(len(ATOM_SYMBOL)):  
  k=no_of_e(ATOM_SYMBOL[i])
  NE=NE+k

#print('Total no of electrons is' +str(NE))

#Calculate nuclear nuclear repulsion term
E_nuc=0.0
for i in range(NATOM):
    for j in range(0,i):
       Z_a=no_of_e(ATOM_SYMBOL[i])
       Z_b=no_of_e(ATOM_SYMBOL[j])
       print(GEOM[i])
       R_ab=find_distance(GEOM[i],GEOM[j])
       E_nuc=0.5*Z_a*Z_b/R_ab
print('Nuclear Repulsion Energy= '+str(E_nuc)+'a.u')


nbasis=7
S=file_read('s.dat',nbasis)
V=file_read('v.dat',nbasis)
T=file_read('t.dat',nbasis)

#Constructuing Core Hamiltonian
H_core=np.zeros([nbasis,nbasis])
H_core=np.add(V,T)

print('HCore')
print(H_core)










