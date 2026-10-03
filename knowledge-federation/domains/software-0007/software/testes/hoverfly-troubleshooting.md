---
id: software.testes.tranche22.001647
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://docs.hoverfly.io/en/latest/index.html", "https://github.com/SpectoLabs/hoverfly/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hoverfly: os problemas que a doc já prevê

## Em uma frase
A página de troubleshooting oficial tem entradas fixas para as dores típicas: por que um request não casou, por que a melhor resposta aproximada não veio, onde ver logs, o campo deprecatedQuery na simulação, acesso remoto bloqueado e arquivos de simulação inchados por corpos de resposta.

## Por que importa
Debugar matcher de proxy sem guia é tentativa e erro com JSON gigante na mão; a doc cortando os seis casos mais comuns é metade do suporte de primeira linha.

## Como funciona
As duas primeiras entradas tratam exatamente do casamento de request — a causa número um de "a simulação existe mas não responde" — e há verbete próprio sobre por que o closest match não aparece.

## Exemplo
O item de arquivos enormes por response bodies denuncia uma armadilha real do capture: gravar payloads grandes demais para versionar; a doc orienta comprimir ou editar.

## Limites e trade-offs
A página lista problemas conhecidos, não todos os bugs: erro de matching fora do vocabulário documentado ainda é debug de código Go.

## Como verificar
Reproduza o não-match mais simples (url com query a mais) e compare seu sintoma com a primeira entrada do troubleshooting.

## Conexões
- [[hoverfly-concepts-map]] — Veja também: Hoverfly: o mapa dos Key Concepts.
- [[hoverfly-java-bindings]] — Veja também: Hoverfly: binding Java e middleware de qualquer linguagem.

## Fontes
- [Hoverfly — documentação inicial](https://docs.hoverfly.io/en/latest/index.html) — conceitos-chave, reference e troubleshooting do v1.12.15; consultado em 2026-10-03.
- [Hoverfly — README oficial](https://github.com/SpectoLabs/hoverfly/blob/master/README.md) — proposta, quickstart, build em Go e contribuição; consultado em 2026-10-03.
