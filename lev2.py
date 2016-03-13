
       #level2

A=["    #      ","  #   #    "," # # # #   ","#       #  ","#       #  "]  #designing char to display corresponding letter
B=["# # # #    ","#       #  ","# # # #    ","#       #  ","# # # #    "]
C=["    # # #  ","  #        "," #         ","  #        ","    # # #  "]
D=["# # # #    ","#      #   ","#       #  ","#      #   ","# # # #    "]
E=["# # # # #  ","#          ","# # # # #  ","#          ","# # # # #  "]
F=["# # # # #  ","#          ","# # # #    ","#          ","#          "]
G=[" # # # #   ","#          ","#    # # # ","#      #   "," # # # #   "]
H=["#       #  ","#       #  ","# # # # #  ","#       #  ","#       #  "]
I=["# # # #    ","   #       ","   #       ","   #       ","# # # #    "]
J=["# # # # #  ","    #      ","    #      ","    #      ","#  #       "]
K=["#     #    ","#   #      ","# #        ","#   #      ","#     #    "]
L=["#          ","#          ","#          ","#          ","# # # #    "]
M=["#       #  ","# #   # #  ","#  # #  #  ","#   #   #  ","#       #  "]
N=["#       #  ","# #     #  ","#   #   #  ","#     # #  ","#       #  "]
O=["  # #      ","#     #    ","#     #    ","#     #    ","  # #      "]
P=["# # # #    ","#      #   ","# # # #    ","#          ","#          "]
Q=["  # # #    ","#       #  ","#       #  ","#     # #  "," # # # # # "]
R=["# # # #    ","#      #   ","# # # #    ","#  #       ","#    # #   "]
S=["  ### #    ","#          "," ## ##     ","      #    ","# ## #     "]
T=["# # # # #  ","    #      ","    #      ","    #      ","    #      "]
U=["#      #   ","#      #   ","#      #   ","#      #   "," # # #     "]
V=["#       #  "," #     #   ","  #   #    ","   # #     ","    #      "]
W=["#       #  ","#   #   #  ","#  # #  #  "," # # # #   ","  #   #    "]
X=["#       #  ","  #   #    ","    #      ","  #   #    ","#       #  "]
Y=["#      #   ","  #  #     ","   #       ","   #       ","   #       "]
Z=["# # # # #  ","      #    ","    #      ","  #        ","# # # # #  "]
show=["","","","",""]

text=raw_input("please input your name:")  #for users to input something

for i in range(len(text)):
    if (text[i]=='A' or text[i]=='a'):  #pick some letters from users' name
        for l in range(5):
            show[l]=show[l]+A[l]
    elif (text[i]=='B' or text[i]=='b'):
	for l in range(5):
            show[l]=show[l]+B[l]
    elif (text[i]=='C' or text[i]=='c'):
	for l in range(5):
            show[l]=show[l]+C[l]
    elif (text[i]=='D' or text[i]=='d'):
	for l in range(5):
            show[l]=show[l]+D[l]
    elif (text[i]=='E' or text[i]=='e'):
	for l in range(5):
            show[l]=show[l]+E[l]
    elif (text[i]=='F' or text[i]=='f'):
	for l in range(5):
            show[l]=show[l]+F[l]
    elif (text[i]=='G' or text[i]=='g'):
	for l in range(5):
            show[l]=show[l]+G[l]
    elif (text[i]=='H' or text[i]=='h'):
	for l in range(5):
            show[l]=show[l]+H[l]
    elif (text[i]=='I' or text[i]=='i'):
	for l in range(5):
            show[l]=show[l]+I[l]
    elif (text[i]=='J' or text[i]=='j'):
	for l in range(5):
            show[l]=show[l]+J[l]
    elif (text[i]=='K' or text[i]=='k'):
	for l in range(5):
            show[l]=show[l]+K[l]
    elif (text[i]=='L' or text[i]=='l'):
	for l in range(5):
            show[l]=show[l]+L[l]
    elif (text[i]=='M' or text[i]=='m'):
	for l in range(5):
            show[l]=show[l]+M[l]
    elif (text[i]=='N' or text[i]=='n'):
	for l in range(5):
            show[l]=show[l]+N[l]
    elif (text[i]=='O' or text[i]=='o'):
	for l in range(5):
            show[l]=show[l]+O[l]
    elif (text[i]=='P' or text[i]=='p'):
	for l in range(5):
            show[l]=show[l]+P[l]
    elif (text[i]=='Q' or text[i]=='q'):
	for l in range(5):
            show[l]=show[l]+Q[l]
    elif (text[i]=='R' or text[i]=='r'):
	for l in range(5):
            show[l]=show[l]+R[l]
    elif (text[i]=='S' or text[i]=='s'):
	for l in range(5):
            show[l]=show[l]+S[l]
    elif (text[i]=='T' or text[i]=='t'):
	for l in range(5):
            show[l]=show[l]+T[l]
    elif (text[i]=='U' or text[i]=='u'):
	for l in range(5):
            show[l]=show[l]+U[l]
    elif (text[i]=='V' or text[i]=='v'):
	for l in range(5):
            show[l]=show[l]+V[l]
    elif (text[i]=='W' or text[i]=='w'):
	for l in range(5):
            show[l]=show[l]+W[l]
    elif (text[i]=='X' or text[i]=='x'):
	for l in range(5):
            show[l]=show[l]+X[l]
    elif (text[i]=='Y' or text[i]=='y'):
	for l in range(5):
            show[l]=show[l]+Y[l]
    elif (text[i]=='Z' or text[i]=='z'):
	for l in range(5):
            show[l]=show[l]+Z[l]

for l in range(5):       #display these letters
    print show[l]
