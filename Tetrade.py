notas = ("C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C","C#","D","D#","E","F","F#","G","G#","A","A#","B")

nota = input("Escreva sua nota para ver sua estrutura: ")

def campoHarmonico(nota):
    if nota in notas:
        for i in notas:
            if i == nota:
                local_t = notas.index(nota) 
                adapRel = local_t + 9
                relMeno = notas[adapRel]
                adapTer = local_t + 4
                adapQui = local_t + 7
                adapSep = local_t + 11
                ter = notas[adapTer]
                qui = notas[adapQui]
                sept = notas[adapSep]
                
    
    print(f"A tetrade de {nota} é: \nTônica: {nota}\nTerça: {ter}\nQuinta: {qui}\nSétima é: {sept}")            
    print(f"A relativa menor de {nota} é {relMeno}m")
               
            
campoHarmonico(nota)
