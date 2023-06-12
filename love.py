import turtle

window = turtle.Screen()
window.bgcolor("pink")
window.title("Feliz dia dos namorados!")

pen = turtle.Turtle()  # Cria uma nova tartaruga para desenhar
pen.color("red")  # Define a cor da tartaruga para vermelho
pen.pensize(10)  # Define a espessura da caneta para 10 pixels
pen.speed(20)  # Define a velocidade de desenho da tartaruga

# Posiciona a tartaruga no centro da tela
pen.penup()  # Levanta a caneta para não deixar traços ao mover
pen.setpos(0, -100)  # Define a posição da tartaruga no centro da tela
pen.pendown()  # Abaixa a caneta para começar o desenho

pen.left(140)  # Vira a tartaruga à esquerda em um ângulo de 140 graus
pen.begin_fill()  # Inicia o preenchimento da forma desenhada

pen.forward(224)  # Move a tartaruga para frente desenhando a primeira parte do coração

for _ in range(200):  # Loop para desenhar a curva superior do coração
    pen.right(1)  # Vira a tartaruga à direita em 1 grau
    pen.forward(2)  # Move a tartaruga para frente desenhando a curva

pen.left(120)  # Vira a tartaruga à esquerda em um ângulo de 120 graus

for _ in range(200):  # Loop para desenhar a curva inferior do coração
    pen.right(1)  # Vira a tartaruga à direita em 1 grau
    pen.forward(2)  # Move a tartaruga para frente desenhando a curva

pen.forward(224)  # Move a tartaruga para frente desenhando a última parte do coração
pen.left(140)  # Vira a tartaruga à esquerda em um ângulo de 140 graus
pen.end_fill()  # Finaliza o preenchimento da forma desenhada

pen.penup()  # Levanta a caneta para não deixar traços ao mover
pen.setpos(0, -200)  # Define a posição da tartaruga para escrever a primeira mensagem
pen.pendown()  # Abaixa a caneta para começar a escrever

turtle.done() 
