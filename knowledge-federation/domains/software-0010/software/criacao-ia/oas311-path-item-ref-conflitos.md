---
id: software.criacao_ia.tranche03.000299
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#path-item-object", "https://spec.openapis.org/oas/v3.1.1.html#reference-object"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1 Path Item `$ref`: não sobrepor fields com o alvo

## Em uma frase
No Path Item Object do OAS 3.1.1, se um field também aparece no objeto local e no alvo de `$ref`, o comportamento é indefinido.

## Por que importa
Ferramentas podem implementar merge de maneira diferente, principalmente para operações, servers e parameters. O comportamento definido para o Reference Object — como summary e description que sobrepõem campos — não deve ser presumido para `$ref` dentro de um Path Item.

## Como funciona
Use `$ref` do Path Item para referenciar uma definição sem repetir localmente os mesmos fields. A especificação observa que a semântica de `$ref` com propriedades adjacentes pode mudar em versões futuras para se aproximar do Reference Object, mas OAS 3.1.1 ainda define conflito entre fields como indefinido.

## Exemplo
Se `components.pathItems.Shared` define `get` e `parameters`, evite escrever outro `get` ou `parameters` ao lado de `$ref: '#/components/pathItems/Shared'`. Para variação real, crie uma definição de Path Item explícita ou gere duas definições consistentes, em vez de depender de merge não especificado.

## Limites e trade-offs
Ferramentas podem aceitar esse padrão legado, mas o resultado não é interoperável nem garantido. Isso é diferente de Reference Object e também diferente de `$ref` dentro do Schema Object, que segue o modelo JSON Schema.

## Como verificar
Lint o grafo de referências para detectar propriedade repetida entre Path Item e seu alvo. Execute parser de pelo menos duas ferramentas somente para encontrar divergências; não considere compatibilidade observada como regra normativa.

## Conexões
- [[oas311-webhooks-versus-callbacks]] — OAS 3.1.1: escolher entre webhook top-level e callback de operação.
- [[oas311-readonly-writeonly-annotations]] — OAS 3.1.1: validar readOnly e writeOnly conforme direção da mensagem.

## Fontes
- [OpenAPI Specification v3.1.1 — Path Item Object](https://spec.openapis.org/oas/v3.1.1.html#path-item-object) — define conflito indefinido de fields entre Path Item local e referenciado Consulta: 2026-10-04.
- [OpenAPI Specification v3.1.1 — Reference Object](https://spec.openapis.org/oas/v3.1.1.html#reference-object) — permite contrastar os overrides definidos para Reference Object com a regra de Path Item Consulta: 2026-10-04.
