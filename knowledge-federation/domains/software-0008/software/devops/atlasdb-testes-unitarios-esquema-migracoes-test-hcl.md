---
id: software.devops.tranche08.000767
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/ariga/atlas/master/README.md", "https://atlasgo.io/testing/schema", "https://github.com/ariga/atlas"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ariga Atlas: testes automatizados de esquemas e migrações (atlas schema test e atlas migrate test) com .test.hcl

## Em uma frase
O Atlas inclui um framework nativo de testes (`atlas schema test` e `atlas migrate test`) onde arquivos `*.test.hcl` declaram blocos `test "schema"` e `test "migrate"` com asserções `exec` e `catch` executadas contra o banco de desenvolvimento.

## Por que importa
Funções armazenadas, triggers, views complexas, constraints `CHECK` e transformações de dados durante migrações contêm lógica de negócio real dentro do banco de dados; sem uma ferramenta nativa de testes unitários de banco, erros nessa lógica só são descobertos quando a aplicação falha em homologação ou produção. A seção `Testing Schemas and Migrations` do README oficial do Atlas demonstra como escrever e rodar testes de banco.

## Como funciona
O desenvolvedor cria um arquivo `schema.test.hcl` (e referencia `test { schema { src = ["schema.test.hcl"] } }` no `atlas.hcl`). Dentro de um bloco `test "schema" "nome"`, o Atlas provisiona o esquema limpo no `--dev-url` e executa sequencialmente: (1) blocos **`exec`** com instruções SQL (`INSERT`, `SELECT`, `CALL`) e `output` esperado para validar que operações válidas funcionam e retornam o resultado exato; e (2) blocos **`catch`** com instruções SQL que **devem falhar** (por exemplo, inserir um `CHECK` inválido ou `NULL` proibido) verificando a mensagem de erro com `error = "CHECK constraint failed: positive_X"`. De modo análogo, `atlas migrate test` permite injetar dados de semente em uma versão específica da migração, avançar as migrações seguintes e testar se os dados existentes foram transformados corretamente.

## Exemplo
```hcl
# Exemplo de teste unitário de esquema no Atlas (schema.test.hcl) validando inserção válida e violação de constraint
test "schema" "indirection" {
  exec {
    sql = "INSERT INTO users (id, age) VALUES (1, 25)"
  }
  catch {
    sql   = "INSERT INTO users (id, age) VALUES (2, -5)"
    error = "CHECK constraint failed"
  }
}
```

## Limites e trade-offs
Como cada suíte `atlas schema test` e `atlas migrate test` executa instruções SQL reais contra a instância configurada em `dev-url` (como um container Docker Postgres ou MySQL), os testes validam o comportamento real do motor do SGBD (sem mocks falsos), mas exigem que o daemon Docker (ou serviço de banco local de desenvolvimento) esteja ativo no runner de CI.

## Como verificar
Execute `atlas schema test --env local` (ou `atlas migrate test --env local`) e confirme a saída `PASS` para todos os blocos `test` declarados nos arquivos `.test.hcl`.

## Conexões
- [[atlasdb-integracao-16-orms-go-ts-python-java-dotnet-php]] — Veja também: Ariga Atlas: carregamento automático de esquema a partir de 16 ORMs em Go, TypeScript, Python, Java, C#/.NET e PHP.
- [[atlasdb-seguranca-como-codigo-rbac-roles-permissions-rls]] — Veja também: Ariga Atlas: Security-as-Code para bancos de dados (roles, users, permissions e Row-Level Security em HCL).
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.
- [[atlasdb-fluxo-declarativo-schema-apply-diff-plan]] — Referência cruzada direta com atlasdb-fluxo-declarativo-schema-apply-diff-plan.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/testing/schema) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
