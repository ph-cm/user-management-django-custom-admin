#  Sistema de Gestão para Casa de Apoio

##  Sobre o Projeto

Este projeto tem como objetivo gerenciar pessoas, hospedagens e serviços de uma casa de apoio para pacientes em tratamento fora de sua cidade de origem.

O sistema permite registrar:

* Pessoas (pacientes, acompanhantes, profissionais e voluntários)
* Check-ins e check-outs
* Serviços prestados (internos e profissionais)

Os dados coletados auxiliam na geração de relatórios e prestação de contas.

---

##  Tecnologias Utilizadas

* Python 3.x
* Django
* Django REST Framework
* drf-spectacular (Swagger)
* SQLite (ambiente local)

---

## ⚙️ Como Rodar o Projeto

### 1. Clonar repositório

```bash
git clone https://github.com/ph-cm/user-management-django-custom-admin.git
cd user-management-django-custom-admin/danielle
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar migrations

```bash
python manage.py migrate
```

### 5. Criar superusuário

```bash
python manage.py createsuperuser
```

### 6. Popular banco com dados de teste

```bash
python manage.py seed_data
```

### 7. Rodar o servidor

```bash
python manage.py runserver
```

---

##  Acessos do Sistema

* Admin: http://127.0.0.1:8000/admin
* Swagger: http://127.0.0.1:8000/api/docs/
* Dashboard: http://127.0.0.1:8000/dashboard

---

## Dashboard

O dashboard foi desenvolvido utilizando a arquitetura MVT do Django, apresentando indicadores como:

* Total de pessoas por tipo
* Check-ins ativos e encerrados
* Check-outs realizados
* Serviços prestados

---

##  Melhorias Implementadas

### 1. Classificação de Pessoas

Adição de tipos de usuário (paciente, acompanhante, profissional e voluntário).

### 2. Controle de Check-in Ativo

Restrição para impedir múltiplos check-ins ativos para a mesma pessoa.

### 3. Encerramento Automático

Ao criar um check-out, o sistema automaticamente encerra o check-in associado.

---

##  Seed de Dados

Foi implementada uma management command (`seed_data`) para popular o banco com dados realistas para testes e demonstração.

---

##  Documentação da API

A API foi documentada utilizando **drf-spectacular**, disponível via Swagger.

---

##  Considerações Finais

O projeto foi refatorado a partir de uma base legada, tornando-se funcional, estruturado e preparado para evolução futura.
