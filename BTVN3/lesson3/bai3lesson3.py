python_club ={"sv01", "sv02", "sv03"}
ai_club = {"sv02", "sv03", "sv04"}
eng_club ={"sv01", "sv03", "sv05"}

all_sv = python_club | ai_club | eng_club

print("only one: ", all_sv)
print("all: ", python_club & ai_club & eng_club)
print("only Python: ", python_club - ai_club - eng_club)

print("only one: ")
for sv in all_sv:
    if(sv in python_club) + (sv in ai_club) + (sv in eng_club) == 1:
        print(sv)

print("all: ")
for sv in all_sv:
    if(sv in python_club) + (sv in ai_club) + (sv in eng_club) == 3:
        print(sv)

print("only Python:")
for sv in all_sv:
    if(sv in python_club) == 1:
        print(sv)

code = input("SV id: ")
if code in python_club:
    print("python")
if code in ai_club:
    print("ai")
if code in eng_club:
    print("eng")
