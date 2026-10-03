---
id: software.seguranca.tranche01.000075
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

# SpiceDB Consistência Global e `ZedToken`: prevenção do *New Enemy Problem* com `at_least_as_fresh`, `minimize_latency` e `fully_consistent`

## Em uma frase
Fiel ao artigo do Google Zanzibar, o SpiceDB retorna um token opaco de marca d'água temporal chamado **`ZedToken`** (equivalente ao *Zookie* do Zanzibar) em toda operação de escrita (`WriteRelationships`) e leitura, permitindo que o cliente escolha entre 4 modos de consistência por requisição: **`minimize_latency`**, **`at_least_as_fresh`**, **`at_exact_snapshot`** e **`fully_consistent`**.

## Por que importa
Se você usar sempre cache cego sem controle de versão, sofre o *New Enemy Problem* (acesso revogado continua funcionando durante a janela de cache); se desativar todo o cache (`fully_consistent` em 100% das chamadas), perde a performance e escalabilidade de cache distribuído.

## Como funciona
Ao armazenar o `ZedToken` retornado quando um recurso ou permissão foi modificado e passá-lo em **`at_least_as_fresh`** nas leituras daquele recurso, o SpiceDB usa seu cache em memória de ~5ms sempre que o cache for mais novo ou igual ao `ZedToken`, e só vai ao banco se o cache estiver atrasado em relação àquela mutação!

## Exemplo
```bash
# Gravando um relacionamento via zed (que retorna um ZedToken) e checando com consistência total:
zed relationship create document:roadmap reader user:anne
zed permission check document:roadmap view user:anne --consistency-full
```

## Limites e trade-offs
Para a maioria das aplicações, o padrão ideal é usar `at_least_as_fresh` (quando a entidade possui um `ZedToken` salvo junto ao registro no banco da aplicação) ou `minimize_latency` para leituras gerais, reservando `fully_consistent` para operações críticas de segurança.

## Como verificar
Use `--explain` no `zed permission check` para visualizar o caminho exato de resolução no grafo e o `ZedToken` avaliado.

## Conexões
- [[spicedb-caveats-abac-relacoes-condicionais-cel-contexto]] — Veja também: SpiceDB `Caveats`: combinando ReBAC e ABAC com relacionamentos condicionais avaliados em tempo de execução.
- [[spicedb-reverse-indexes-lookupresources-lookupsubjects-paginacao]] — Veja também: SpiceDB Índices Reversos (`LookupResources` e `LookupSubjects`): listagem eficiente de recursos acessíveis e auditoria de sujeitos.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://authzed.com/docs/spicedb/concepts/schema) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
