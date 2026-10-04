---
id: software.seguranca.tranche01.000074
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
fontes: ["https://authzed.com/docs/spicedb/concepts/schema", "https://raw.githubusercontent.com/authzed/spicedb/main/README.md", "https://github.com/authzed/spicedb"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SpiceDB `Caveats`: combinando ReBAC e ABAC com relacionamentos condicionais avaliados em tempo de execução

## Em uma frase
Conforme documentado na referência oficial do Schema, **Caveats** são expressões tipadas (baseadas em Google CEL) declaradas no topo do schema `.zed` e anexadas a relações (`relation reader: user with ip_allowlist`), permitindo que um relacionamento só seja considerado válido no momento do `CheckPermission` se a expressão retornar `true`.

## Por que importa
Em cenários multi-paradigma (ReBAC + ABAC), você quer que um relacionamento no grafo exista apenas sob condições dinâmicas de atributos (ex.: o usuário está na faixa CIDR corporativa, o horário está dentro do turno de plantão ou o atributo `region` do usuário coincide com o recurso).

## Como funciona
No schema `.zed`, você declara `caveat ip_allowlist(user_ip ipaddress, cidr string) { user_ip.in_cidr(cidr) }`. Ao gravar a relação, você pode pré-vincular parte do contexto (como o `cidr` permitido da empresa) e, no momento do `CheckPermission`, a aplicação fornece o `user_ip` atual da requisição HTTP.

## Exemplo
```zed
caveat ip_allowlist(user_ip ipaddress, cidr string) {
  user_ip.in_cidr(cidr)
}

definition user {}

definition document {
  relation reader: user | user with ip_allowlist
  permission view = reader
}
```

## Limites e trade-offs
Se os parâmetros exigidos por uma `caveat` não forem fornecidos no contexto da chamada `CheckPermission`, o SpiceDB retorna um resultado parcial indicando quais parâmetros de contexto faltam para concluir a decisão.

## Como verificar
Teste um relacionamento com caveat via CLI passando `--caveat-context`: `zed permission check document:sec view user:alice --caveat-context '{"user_ip": "10.0.1.5"}'`.

## Conexões
- [[spicedb-operadores-permissao-union-intersection-exclusion-arrows-precedencia]] — Veja também: SpiceDB Operações de Permissão (`+`, `&`, `-` e `->`): travessia de hierarquias com Arrows e a armadilha de precedência do `+`.
- [[spicedb-consistencia-zedtoken-zookies-at-least-as-fresh-new-enemy]] — Veja também: SpiceDB Consistência Global e `ZedToken`: prevenção do *New Enemy Problem* com `at_least_as_fresh`, `minimize_latency` e `fully_consistent`.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://authzed.com/docs/spicedb/concepts/schema) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
