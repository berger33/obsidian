---
id: software.seguranca.tranche01.000073
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

# SpiceDB Operações de Permissão (`+`, `&`, `-` e `->`): travessia de hierarquias com Arrows e a armadilha de precedência do `+`

## Em uma frase
As expressões de `permission` no SpiceDB suportam quatro operadores fundamentais: **união (`+`)**, **interseção (`&`)**, **exclusão (`-`)** e **seta / arrow (`->`, ex.: `parent->view`)** — com uma regra crítica documentada na referência oficial: por razões históricas, **a união (`+`) tem precedência maior que a interseção (`&`) e a exclusão (`-`)**!

## Por que importa
Em quase todas as linguagens de programação e na álgebra booleana, o `AND` (`&`) tem precedência sobre o `OR` (`+`); porém no SpiceDB, a expressão `a + b & c` é avaliada da esquerda para a direita como **`(a + b) & c`**, e **não** como `a + (b & c)`!

## Como funciona
Por isso, sempre que combinar `+` com `&` ou `-` na mesma expressão de `permission`, utilize **parênteses explícitos** (ex.: `permission view = (reader + parent->view) - banned_user`) para tornar a intenção inequívoca e segura.

## Exemplo
```zed
definition folder {
  relation reader: user
  permission view = reader
}

definition document {
  relation parent: folder
  relation reader: user
  relation banned: user

  // Uso explícito de parênteses + seta (->) para herdar view da pasta pai exceto banidos:
  permission view = (reader + parent->view) - banned
}
```

## Limites e trade-offs
O operador **arrow (`parent->view`)** percorre todos os objetos ligados pela relação à esquerda (`parent`) e avalia a permissão/relação à direita (`view`) nesses objetos, permitindo herança hierárquica sem duplicar tuplas.

## Como verificar
Use `zed validate` com asserções para confirmar que expressões combinando `+`, `&` e `-` comportam-se exatamente como esperado.

## Conexões
- [[spicedb-schema-language-zed-definitions-relations-permissions]] — Veja também: SpiceDB Schema Language (`.zed`): separação estrita entre `definition`, `relation` (substantivos) e `permission` (verbos computados).
- [[spicedb-caveats-abac-relacoes-condicionais-cel-contexto]] — Veja também: SpiceDB `Caveats`: combinando ReBAC e ABAC com relacionamentos condicionais avaliados em tempo de execução.

## Fontes
- [AuthZed SpiceDB GitHub — README.md (Distributed Permissions Database, Zanzibar Architecture, Consistency Modes, Datastores & zed CLI)](https://authzed.com/docs/spicedb/concepts/schema) — README oficial do authzed/spicedb detalhando a arquitetura do banco de permissões, garantias de consistência por requisição, motores de armazenamento e execução em Kubernetes; consultado em 2026-10-03.
- [AuthZed SpiceDB Official Documentation — Schema Language Reference (Definitions, Relations vs Permissions, +, &, -, -> Operators, Precedence & Caveats)](https://raw.githubusercontent.com/authzed/spicedb/main/README.md) — Referência oficial da linguagem de schema do SpiceDB cobrindo definitions, subject relations, wildcards, operadores de conjunto, alerta de precedência do operador + e caveats CEL; consultado em 2026-10-03.
- [AuthZed SpiceDB — Official GitHub Repository](https://github.com/authzed/spicedb) — Repositório oficial Apache-2.0 do AuthZed SpiceDB; consultado em 2026-10-03.
