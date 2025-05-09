🐾 Projeto Petshop

Bem-vindo ao Projeto Petshop, um sistema completo para gerenciamento de um petshop, desenvolvido com foco em escalabilidade,
performance e boas práticas de desenvolvimento Back-End com Python e Django.
Este projeto demonstra minha capacidade de construir APIs robustas, integradas e prontas para atender demandas reais do mercado.

🚀 Tecnologias Utilizadas

Python 3

Django

Django REST Framework

SQLite 

HTML e CSS (para visualização básica/admin)


🎯 Funcionalidades

📋 Cadastro, atualização e exclusão de clientes, pets e serviços

📆 Agendamento de serviços com controle de datas e horários

🧾 Geração de histórico de atendimentos por cliente ou pet

🔍 Filtros inteligentes e pesquisa por nome, raça, tipo de serviço, etc.

🔒 Sistema de autenticação (login/logout)

⚙️ Painel administrativo com interface do Django Admin

📈 Estrutura pronta para escalar e integrar com outras ferramentas (ex: iFood, impressão de pedidos)

📁 Estrutura do Projeto


Projeto-Petshop/
│
├── petshop/              # App principal
│   ├── models.py         # Modelos do banco de dados
│   ├── views.py          # Lógicas de negócio (CRUD/API)
│   ├── serializers.py    # Serializadores para API REST
│   └── urls.py           # Rotas da aplicação
│
├── manage.py             # Gerenciador do Django
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto


⚙️ Como Executar Localmente

Clone o repositório:

git clone https://github.com/henriquelopescavalcante/Projeto-Petshop.git
cd Projeto-Petshop
Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as dependências:

pip install -r requirements.txt
Rode as migrações e o servidor:

python manage.py migrate
python manage.py runserver


Acesse a aplicação:

Painel Admin: http://127.0.0.1:8000/admin

Endpoints da API: http://127.0.0.1:8000/api/

🧪 Testes
Você pode testar a API com ferramentas como Postman.

Os principais endpoints incluem:

GET /api/clientes/

POST /api/pets/

PUT /api/servicos/{id}/

DELETE /api/agendamentos/{id}/


💡 Diferenciais Técnicos

Código modular e com separação clara de responsabilidades

Boas práticas RESTful e uso de serializers

Preparado para autenticação com Token ou JWT

Estrutura ideal para evolução futura (ex: frontend com React ou Vue)

🧠 Aprendizados e Objetivos

Este projeto foi desenvolvido para consolidar conhecimentos em Back-End com Django e demonstrar habilidades práticas em:

Modelagem de dados realista

Criação de APIs REST eficientes

Organização de código limpo e reutilizável

Pensamento orientado a objetos e componentização


🤝 Contribuição


Sugestões, feedbacks e melhorias são bem-vindos. Sinta-se livre para abrir issues ou pull requests!


📌 Contato
Github: https://github.com/henriquelopescavalcante | Linkedin: https://www.linkedin.com/in/henriquelopescs/
Email: henriquelopescavalcante@gmail.com


⭐ Curtiu o projeto?
Deixe uma ⭐ no repositório para apoiar este e futuros projetos! Obrigado por visitar! 😄
