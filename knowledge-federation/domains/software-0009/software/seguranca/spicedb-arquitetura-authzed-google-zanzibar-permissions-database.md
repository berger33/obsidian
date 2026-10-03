---
id: software.seguranca.tranche01.000071
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
fontes: ["https://raw.githubusercontent.com/authzed/spicedb/main/README.md", "https://authzed.com/docs/spicedb/concepts/schema", "https://github.com/authzed/spicedb"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SpiceDB: arquitetura do banco de dados de permissões distribuído inspirado no Google Zanzibar (`spicedb` e CLI `zed`)

## Em uma frase
O **SpiceDB** (`authzed/spicedb`, licenciado sob Apache 2.0) é um banco de dados de permissões distribuído e open-source inspirado no sistema **Google Zanzibar**, projetado para responder com latência na casa de ~5 ms (P95) e consistência configurável por requisição à pergunta central: **"o sujeito X pode executar a ação Y no recurso Z?"**.

## Por que importa
Conforme cita o README oficial do SpiceDB, *Broken Access Control* tornou-se a ameaça número 1 no OWASP Top 10; espalhar lógica de autorização em queries `JOIN` ad-hoc dentro de dezenas de microsserviços em linguagens diferentes torna impossível auditar e escalar permissões.

## Como funciona
De forma análoga a um banco de dados relacional: 1) os desenvolvedores definem um **Schema (`.zed`)** tipado; 2) as aplicações gravam dados na forma de **Relationships (tuplas)**; e 3) os serviços emitem consultas gRPC/HTTP (`CheckPermission`, `LookupResources`, `LookupSubjects`) através dos clientes oficiais ou da CLI **`zed`**.

## Exemplo
```bash
# Iniciando o SpiceDB em modo de desenvolvimento local (serve-testing) ou com chave pré-compartilhada:
spicedb serve --grpc-preshared-key "dev-secret-key" --datastore-engine memory

# Configurando o contexto da CLI zed e verificando a versão:
zed context set local localhost:50051 "dev-secret-key" --insecure
zed version
```

## Limites e trade-offs
O subcomando `spicedb serve-testing` sobe um servidor SpiceDB efêmero em memória onde cada chave pré-compartilhada diferente passada pelo cliente cria um banco isolado instantâneo — perfeito para rodar centenas de testes de integração em paralelo no CI!

## Como verificar
Execute `spicedb version` e `zed version` para validar a instalação do servidor e da CLI.

## Conexões
- [[spicedb-schema-language-zed-definitions-relations-permissions]] — Veja também: SpiceDB Schema Language (`.zed`): separação estrita entre `definition`, `relation` (substantivos) e `permission` (verbos computados).

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://authzed.com/docs/spicedb/concepts/schema) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
