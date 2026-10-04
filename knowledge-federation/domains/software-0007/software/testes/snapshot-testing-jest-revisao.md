---
id: software.testes.snapshot-testing.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://jestjs.io/docs/snapshot-testing", "https://bazel.build/reference/test-encyclopedia"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Snapshot testing, Golden test, Teste de snapshot]
lote: software-testes-2000-0001
---

# Snapshot testing com Jest e revisão dos resultados

## Em uma frase
Snapshot testing guarda uma representação de saída aprovada e a compara em execuções posteriores para revelar mudanças observáveis.

## Por que importa
Snapshots podem tornar regressões de serialização, renderização ou saída textual visíveis sem escrever uma asserção para cada campo. Como o arquivo esperado passa a fazer parte dos insumos do teste, ele deve ser legível, versionado e revisado junto com a alteração que o atualiza. Atualizar um snapshot sem examinar a diferença pode converter defeito em nova expectativa.

## Como funciona
Na primeira execução, Jest gera o artefato de snapshot; execuções seguintes comparam a saída atual com a versão armazenada. A documentação recomenda snapshots focados e legíveis, commit junto do código e revisão como código. A Test Encyclopedia do Bazel também reconhece golden outputs versionados como dados que podem fazer parte das dependências de um teste. Mudança de snapshot indica diferença para investigar, não automaticamente regressão nem correção.

## Exemplo
Um teste de componente renderiza um botão com propriedades fixas e compara uma representação curta. Se texto, atributo acessível ou estrutura mudar, revise o diff contra a intenção da alteração. Para dados variáveis como horário, fixe a dependência ou use matchers apropriados para não gerar snapshots diferentes em cada execução.

## Limites e trade-offs
Snapshots extensos podem esconder o comportamento importante em um diff ruidoso e encorajar atualizações em massa. Saídas dependentes de plataforma, relógio, aleatoriedade ou ordem não determinística causam falhas espúrias. Um snapshot mostra igualdade com uma amostra aprovada, mas não expressa sempre por que aquela saída é correta.

## Como verificar
Mantenha cada snapshot pequeno, com nome e objetivo claros; examine o diff antes de atualizar. Execute repetidamente para verificar determinismo e confirme que a nova saída corresponde ao requisito ou decisão de design. Combine com asserts semânticos explícitos para propriedades críticas, como conteúdo, acessibilidade ou contrato serializado.

## Conexões
- [[testes-flaky-determinismo]] — valores variáveis tornam snapshots instáveis.
- [[fixtures-pytest-ciclo-vida-escopos]] — fixtures controlam ambiente e dados usados para produzir a saída esperada.
- [[piramide-testes-estrategia-contexto]] — snapshots são uma técnica, não um nível de escopo por si só.

## Fontes
- [Jest — Snapshot Testing](https://jestjs.io/docs/snapshot-testing) — criação, comparação, revisão e determinismo de snapshots; acesso em 2026-10-01.
- [Bazel — Test Encyclopedia](https://bazel.build/reference/test-encyclopedia) — arquivos de saída esperada versionados como dependências de teste; acesso em 2026-10-01.
