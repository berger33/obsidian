---
id: software.testes.tranche21.001480
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://www.chaijs.com/api/bdd/", "https://www.chaijs.com/guide/styles/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Chai: três estilos, um núcleo

## Em uma frase
O Chai oferece expect e should, que compartilham a mesma linguagem encadeável, mais o estilo assert clássico com argumentos posicionais.

## Por que importa
Times diferentes assimilam estilos diferentes: a liberdade de escolher expect, should ou assert remove um atrito que travaria a adoção de asserções ricas.

## Como funciona
Adote um estilo por projeto, importe a lib correspondente e nunca misture os três no mesmo arquivo só por conveniência momentânea.

## Exemplo
Uma suíte que usa expect para comportamentos e assert dentro de utilitários de teste permanece coerente se o guia interno ditar a regra.

## Limites e trade-offs
should exige ativar o protótipo global e pode incomodar linters; a comparação oficial entre os estilos existe exatamente para decidir informado.

## Como verificar
Escreva a mesma verificação nos três estilos e confirme que a falha produz mensagens equivalentes na informação essencial.

## Conexões
- [[chai-language-chains]] — Veja também: Chai: correntes de linguagem de leitura.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — Guia de estilos](https://www.chaijs.com/guide/styles/) — comparação entre expect, should e assert; consultado em 2026-10-03.
