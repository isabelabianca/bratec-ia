import speech_recognition as sr

#Fun��o que ser� respons�vel por ouvir e reconhecer a fala

def reconhecer_fala():    
    microfone = sr.Recognizer() #Habilitar o microfone
    with sr.Microphone() as source:        
        microfone.adjust_for_ambient_noise(source)#Redu��o de ru�do disponivel na biblioteca speech_recognition        
        print("Diga alguma coisa: ")        
        audio = microfone.listen(source) # Guarda o �udio falado na variavel 'audio'
        try:
            frase = microfone.recognize_google(audio,language='pt-BR') # O �udio sera interpretado em portugu�s          
            print("Voc� disse: " + frase)        
        except:
            print("N�o entendi!")
        return frase

#Chama a fun��o para ouvir o �udio e transcrever
frase = reconhecer_fala()

if "sa�da de emerg�ncia" in frase:
    print("Siga em frente")
elif "lojas americanas" in frase:
    print("Vire � pr�xima esquerda")
elif "banheiro feminino" in frase:
    print("Siga em frente e vire a direita no final do corredor")
elif "loja da nike" in frase:
    print("vire a esquerda, em frente ao bebedouro")