registro = []
for i in range(int(input())):
    registro.append(input())

print(registro)


# as únicas mensagens que Sara envia são respostas a mensagens que ela recebeu.
# Sara envia no máximo uma mensagem como reposta a uma mensagem que recebeu.
# um amigo de Sara nunca envia uma nova mensagem para Sara até que tenha recebido resposta da mensagem que enviou anteriormente.

# R X indica que uma mensagem foi recebida do amigo X.
# E X indica que uma mensagem foi enviada ao amigo X.
# O aplicativo usa ainda um outro tipo de registro, para indicar o tempo que se passou entre dois eventos consecutivos, na forma
# T X indicando que X segundos se passaram entre o evento anterior e o evento posterior a esse registro.
# Se não há registro do tipo T X entre dois registros de eventos consecutivos significa que exatamente 1 segundo se passou entre esses dois eventos.:++