# Projeto:

## Jogo da cobrinha + Cadastro, Login, Logou e autentificação de usuários

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
- Separation of concerns

### Camadas do projeto

- Login, Registro, Autentificação e Logout: 
Uso a lib do Django, auth, para criar a tabela do banco de dados que recebe os registros e valida os mesmos na tela de login, redirecionando o usário para o jogo.  
O jogo só é acessado se o usuário estiver logado. A autenticação acontece por meio do do decorator *@login_required*

- O jogo: (em desenvolvimento)
Uso JavaScript para # TODO

---

Inspirações;
- [Filipe Deschamps -> Jogo multiplayer](https://www.youtube.com/watch?v=0sTfIZvjYJk&list=PLMdYygf53DP5SVQQrkKCVWDS0TwYLVitL&pp=iAQB)
- [Pythonando -> AUTENTICAÇÃO COM DJANGO | DJANGO AUTH](https://www.youtube.com/watch?v=gdhiA6wObw0)
