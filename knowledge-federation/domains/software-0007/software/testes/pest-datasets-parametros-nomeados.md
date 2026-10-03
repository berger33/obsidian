---
id: software.testes.tranche15.000880
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pestphp.com/docs/datasets", "https://pestphp.com/docs/writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: mapear datasets associativos por nome de parâmetro

## Em uma frase
Datasets nomeados permitem executar um mesmo corpo de teste com diversos inputs, e arrays associativos podem ser mapeados às variáveis do closure pelo nome.

## Por que importa
Esse mapeamento evita que a ordem das chaves no dataset se torne uma dependência oculta da posição dos argumentos; descrições com nome do dataset também deixam explícito qual cenário falhou no relatório.

## Como funciona
Para closures usados com datasets, os tipos dos parâmetros precisam estar declarados nos casos documentados.

## Exemplo
Defina uma lista de endereços e nomes em `dataset('users', [...])` e consuma `function (string $email, string $name)`; Pest associa as chaves correspondentes sem exigir a mesma ordem textual.

## Limites e trade-offs
Nome de dataset é parte do diagnóstico, mas não substitui uma expectativa específica; dados inválidos precisam representar limites deliberados, não combinações aleatórias sem explicação.

## Como verificar
Reordene as chaves de um registro e execute o dataset, depois provoque uma falha em uma linha nomeada para conferir se o output identifica o cenário.

## Conexões
- [[pest-dataset-bound-depois-de-beforeeach]] — Veja também: Pest 5: criar dataset bound depois do setup de cada teste.

## Fontes
- [Pest 5 — Datasets](https://pestphp.com/docs/datasets) — datasets inline/compartilhados, chaves, parâmetros nomeados e bound datasets; consultado em 2026-10-02.
- [Pest 5 — Writing tests](https://pestphp.com/docs/writing-tests) — definição de testes, closures e integração com expectativas; consultado em 2026-10-02.
