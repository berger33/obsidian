---
id: software.seguranca.tranche01.000081
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/cerbos/cerbos/main/README.md", "https://docs.cerbos.dev/cerbos/latest/policies/index.html", "https://github.com/cerbos/cerbos"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cerbos: arquitetura do Policy Decision Point (`PDP`) stateless para autorização PBAC/ABAC/RBAC declarativa em YAML

## Em uma frase
O **Cerbos** (`cerbos/cerbos`, licenciado sob Apache 2.0) é uma camada de autorização **stateless** (*Policy Decision Point — PDP*) escrita em Go que permite definir regras de controle de acesso ricas em contexto (**RBAC**, **ABAC** e **PBAC**) em arquivos YAML versionados via GitOps, expondo APIs HTTP (`:3592`) e gRPC (`:3593`) de baixíssima latência.

## Por que importa
Diferente de bancos de grafos Zanzibar que exigem replicar e sincronizar todas as relações de dados para um banco central, o Cerbos PDP é **100% stateless**: a aplicação envia no payload da requisição os atributos já conhecidos do **`Principal`** (usuário/serviço) e do **`Resource`** (objeto sendo acessado), e o Cerbos avalia as políticas localmente em sub-milissegundos.

## Como funciona
Por não armazenar estado de entidades de negócio, o Cerbos pode rodar como **sidecar container** ao lado de cada Pod no Kubernetes (zero latência de rede externa), como serviço de cluster compartilhado, daemon systemd ou função serverless, carregando políticas a partir de `disk`, `git`, `blob` (S3/GCS/MinIO) ou banco de dados (`sqlite3`, `postgres`, `mysql`).

## Exemplo
```bash
# Iniciando o Cerbos PDP apontando para um diretório local de políticas YAML:
docker run --rm -i -t -p 3592:3592 -p 3593:3593 \
  -v "$(pwd)/policies:/policies" \
  ghcr.io/cerbos/cerbos:latest server --config=/policies/.cerbos.yaml
```

## Limites e trade-offs
Como destaca a documentação oficial de políticas do Cerbos, ao acessar `http://localhost:3592/` em um navegador (ou `/schema/swagger.json`), a própria instância em execução exibe a documentação interativa da API e exemplos de requisições.

## Como verificar
Execute `curl -fsS http://localhost:3592/_cerbos/health` para verificar a saúde do Cerbos PDP.

## Conexões
- [[cerbos-seis-tipos-politicas-resource-derived-roles-principal-role-export]] — Veja também: Cerbos Taxonomia das 6 Políticas: `Resource Policies`, `Derived Roles`, `Principal Policies`, `Role Policies`, `Exported Variables` e `Constants`.

## Fontes
- [Cerbos GitHub — README.md (Stateless Policy Decision Point, CheckResources & PlanResources APIs, Derived Roles, Deployment Topologies & cerbos compile)](https://raw.githubusercontent.com/cerbos/cerbos/main/README.md) — README oficial do cerbos/cerbos documentando a arquitetura stateless do PDP, exemplos de políticas YAML, avaliação em lote, geração de Query Plan e execução via container/sidecar; consultado em 2026-10-03.
- [Cerbos Official Documentation — Policies Overview (Resource, Derived Roles, Principal, Role Policies, Exported Variables/Constants & Scoped Policies)](https://docs.cerbos.dev/cerbos/latest/policies/index.html) — Documentação oficial de políticas do Cerbos detalhando os 6 tipos de política YAML, escopos hierárquicos multi-tenant, condições CEL, schemas e auditoria de decisões; consultado em 2026-10-03.
- [Cerbos — Official GitHub Repository](https://github.com/cerbos/cerbos) — Repositório oficial Apache-2.0 do Cerbos PDP; consultado em 2026-10-03.
