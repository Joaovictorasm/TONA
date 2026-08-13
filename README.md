# TONA - The Only Nutrition App

Plataforma de acompanhamento físico e nutricional para profissionais de nutrição e educação física. Permite criar, gerenciar e personalizar protocolos de treino e alimentação para alunos, com funcionalidades de substituição inteligente de exercícios e alimentos mantendo os macronutrientes semelhantes.

## �� 🚀 Funcionalidades

- **Gestão de Protocolos**: Crie e organize planos de treino e alimentação para cada aluno.
- **Banco de Exercícios**: Cadastre exercícios com grupos musculares e equipamentos.
- **Banco de Alimentos**: Cadastre alimentos com valores nutricionais (calorias, proteína, carboidratos, gordura por 100g).
- **Substituição Inteligente**:
  - Substitua exercícios por outros que trabalhem o mesmo grupo muscular.
  - Substitua alimentos por outros com macros similares (dentro de uma tolerância configurável).
- **API RESTful**: Endpoints completos para integração com front-end ou outros sistemas.
- **Documentação Automática**: Swagger UI disponível em `/docs`.

## �� 🛠��️ Tecnologias Utilizadas

### Backend
- **Python 3.11**
- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para interação com o banco de dados
- **SQLite** - Banco de dados leve (ideal para desenvolvimento e testes)
- **Pydantic** - Validação de dados e geração de esquemas
- **Uvicorn** - Servidor ASGI

### Frontend
- **Next.js 13+** (App Router)
- **TypeScript**
- **React 18**

## �� 📂 Estrutura do Projeto

```
TONA/
├── backend/
│   ├── app/
│   │   ├── main.py              # Entrypoint da API
│   │   ├── models.py            # Modelos SQLAlchemy
│   │   ├── schemas.py           # Schemas Pydantic (validação)
│   │   ├── database.py          # Configuração do banco de dados
│   │   ├── services.py          # Lógica de negócio (substituição)
│   │   └── routers/
│   │       ├── protocols.py     # Endpoints de protocolos
│   │       ├── exercises.py     # Endpoints de exercícios
│   │       └── foods.py         # Endpoints de alimentos
│   ├── seed.py                  # Script para popular dados iniciais
│   └── run.py                   # Script para iniciar o servidor
�└── frontend/
    ├── app/
    │   └── page.tsx             # Página inicial (precisa de ajuste)
    ├── package.json
    └── next.config.js
```

## �� 🚦 Como Executar

### Pré-requisitos
- Python 3.11+
- Node.js 18+ e npm
- Git (opcional)

### Backend

1. Navegue até o diretório do backend:
   ```bash
   cd TONA/backend
   ```

2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
   > **Observação**: Se não houver `requirements.txt`, as dependências principais são:
   > `fastapi`, `uvicorn[standard]`, `sqlalchemy`, `pydantic[dotenv]`, `python-dotenv`, `passlib[bcrypt]`, `bcrypt`

4. Popule o banco com dados iniciais:
   ```bash
   python seed.py
   ```

5. Inicie o servidor:
   ```bash
   python run.py
   ```
   ou
   ```bash
   uvicorn app.main:app --reload
   ```

6. Acesse a API em: http://localhost:8000
   - Documentação interativa (Swagger): http://localhost:8000/docs
   - Documentação ReDoc: http://localhost:8000/redoc

### Frontend

1. Navegue até o diretório do frontend:
   ```bash
   cd TONA/frontend
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Corrija o erro do Link (necessário para o Next.js 13+):
   Edite `app/page.tsx` e remova a tag `<a>` interna ao `<Link>`, conforme o exemplo abaixo:
   ```tsx
   import Link from 'next/link'

   export default function Home() {
     return (
       <main style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
         <h1>FitNut Platform</h>
         <p>Plataforma de acompanhamento físico e nutricional para profissionais.</p>
         <div style={{ marginTop: '2rem' }}>
           <Link href="/protocols">
             Gerenciar Protocolos
           </Link>
         </div>
       </main>
     )
   }
   ```

4. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```

5. Acesse o front-end em: http://localhost:3000

## �� 📖 Uso da API

### Exemplos de requisições (usando curl)

**Criar um exercício:**
```bash
curl -X POST "http://localhost:8000/exercises/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Supino Reto", "muscle_group": "Peito", "equipment": "Barra"}'
```

**Listar exercícios:**
```bash
curl -X GET "http://localhost:8000/exercises/"
```

**Criar um alimento:**
```bash
curl -X POST "http://localhost:8000/foods/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Peito de Frango grelhado", "calories_per_100g": 165, "protein_per_100g": 31, "carbs_per_100g": 0, "fat_per_100g": 3.6}'
```

**Adicionar um exercício a um protocolo:**
```bash
curl -X POST "http://localhost:8000/protocols/1/exercises/1"
```

**Buscar exercícios similares (via serviço interno - exemplo de uso no código):**
```python
from app.services import find_similar_exercises
similar = find_similar_exercises(db, target_exercise)
```

## �� 🧠 Lógica de Substituição

### Exercícios
A função `find_similar_exercises` busca exercícios que possuírem o mesmo `muscle_group` do exercício alvo, excluindo o próprio exercício.

### Alimentos
A função `find_similar_foods_by_macros` calcula a distância euclidiana normalizada entre os macronutrientes (proteína, carboidrato, gordura) dos alimentos. Retorna aqueles cuja distância esteja dentro de uma tolerância (padrão: 0.1 = 10% de diferença relativa).

## �� 📝 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## �� 👥 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## �� 📞 Contato

Para dúvidas ou sugestões, abra uma issue neste repositório.

--- 
*TONA - The Only Nutrition App: Simplificando a prescrição de treino e alimentação para profissionais de saúde e fitness.*