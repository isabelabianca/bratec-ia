import speech_recognition as sr

#Função que será responsável por ouvir e reconhecer a fala

def reconhecer_fala():    
    microfone = sr.Recognizer() #Habilitar o microfone
    with sr.Microphone() as source:        
        microfone.adjust_for_ambient_noise(source)#Redução de ruído disponivel na biblioteca speech_recognition        
        print("Diga alguma coisa: ")        
        audio = microfone.listen(source) # Guarda o áudio falado na variavel 'audio'
        try:
            frase = microfone.recognize_google(audio,language='pt-BR') # O áudio sera interpretado em português          
            print("Você disse: " + frase)        
        except:
            print("Não entendi!")
        return frase

#Chama a função para ouvir o áudio e transcrever
frase = reconhecer_fala()

if "saída de emergência" in frase:
    print("Siga em frente")
elif "lojas americanas" in frase:
    print("Vire à próxima esquerda")
elif "banheiro feminino" in frase:
    print("Siga em frente e vire a direita no final do corredor")
elif "loja da nike" in frase:
    print("vire a esquerda, em frente ao bebedouro")