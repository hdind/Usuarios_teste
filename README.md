# Projeto:

## Jogo da cobrinha + Cadastro, Login, Logout e autentificação de usuários

### Linguagens usadas: 
- Python (Django) -> Back-end
- HTML -> Front-end estrutura
- CSS -> Front-end estilização
- JavaScript -> Lógica do jogo

### Ferramentas usadas:
- VS Code - IDE
- Git - Controle de versão
- GitPod - Testes com servidor público

### Paradigma de programação
- POO

---
### Arquitetura, Engenharia e Design de Software

- SOLID
- Clean code
- Separation of concerns -> "De quem é esse código?"

### Camadas do projeto

- Login, Registro, Autentificação e Logout: 
Uso a lib do Django, auth, para criar a tabela do banco de dados que recebe os registros e valida os mesmos na tela de login, redirecionando o usário para o jogo.  
O jogo só é acessado se o usuário estiver logado. A autenticação acontece por meio do do decorator *@login_required*

- O jogo: 
Com HTML crio um canvas branco na tela com 10px por 10px e renderizado para parecer 400px por 400px com CSS. Dentro do canvas, um player "quadrado" de 1px preto e uma fruta "quadrada" também de 1px verde. 
A lógica é dividida em camadas para melhor separar os conceitos e deixar um código com arquitetura mais limpa. 
Camadas do jogo:
    - Apresentação -> responsável pela renderização do jogo na tela
    - Jogo -> responsável por receber o input e executar ou não a movimentação do player de acordo com as regras do jogo
    - Input -> responsável por ouvir o teclado e anotar a tecla que foi pressionada
    - Regras do jogo -> responsável por validar a movimentação do player e identificar colisão entre player e fruta
    - Suporte -> cria randômicamente números para as posições e cores para as frutas

---

Inspirações;
- [Filipe Deschamps -> Jogo multiplayer](https://www.youtube.com/watch?v=0sTfIZvjYJk&list=PLMdYygf53DP5SVQQrkKCVWDS0TwYLVitL&pp=iAQB)
- [Pythonando -> AUTENTICAÇÃO COM DJANGO | DJANGO AUTH](https://www.youtube.com/watch?v=gdhiA6wObw0)
- [Manual do dev -> Snake Game com JS e HTML](https://www.youtube.com/watch?v=LyWSsZktVOg)
