 Projeto Django - Cadastro de Jogadores

Este é um projeto simples desenvolvido com Django para cadastro e listagem de jogadores de futebol.

---

 Tecnologias utilizadas

* Python
* Django
* SQLite3
* HTML

---

 Estrutura do projeto

```
django/
│
├── futebol/
│   ├── core/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── lista.html
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── futebol/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── db.sqlite3
│   └── manage.py
```

---

## ⚙️ Como rodar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/pablohenriquejs/ativ.django.git
```

### 2. Entrar na pasta

```
cd django
cd futebol
```

### 3. Criar ambiente virtual

```
python -m venv venv
```

### 4. Ativar ambiente virtual (Windows)

```
venv\Scripts\activate
```

### 5. Instalar dependências

```
pip install django
```

### 6. Rodar migrações

```
python manage.py migrate
```

### 7. Iniciar servidor

```
python manage.py runserver
```

---

 Acessar o sistema

Abra no navegador:

```
http://127.0.0.1:8000/
```

---

 Acessar o admin

Crie um super usuário:

```
python manage.py createsuperuser
```

Depois acesse:

```
http://127.0.0.1:8000/admin/
```

---

 Funcionalidades

* Cadastro de jogadores
* Listagem de jogadores
* Painel administrativo (Django Admin)

---

 Licença

Este projeto é apenas para fins de estudo.
