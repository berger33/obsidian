---
id: software.testes.tranche20.001369
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://behave.readthedocs.io/en/stable/gherkin/", "https://behave.readthedocs.io/en/stable/tutorial/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Behave: escrever arquivos de funcionalidade

## Em uma frase
Cada funcionalidade é descrita em arquivo com estrutura de Gherkin: contexto opcional, cenários e passos com palavras-chave.

## Por que importa
O texto compartilhado com o negócio descreve o comportamento esperado e ancora a discussão antes da implementação.

## Como funciona
Escreva um cenário por regra de negócio, use a estrutura dada quando e então e reserve o contexto para a preparação comum.

## Exemplo
A funcionalidade de carrinho pode descrever o cenário de adicionar item e o de aplicar desconto com os mesmos pressupostos.

## Limites e trade-offs
Cenários com muitos passos misturam verificações distintas, e passos com detalhes técnicos perdem valor para quem lê apenas a funcionalidade.

## Como verificar
Leia cada cenário isoladamente e confirme que ele descreve um comportamento verificável sem depender dos demais.

## Conexões
- [[behave-step-definitions]] — Veja também: Behave: implementar definições de passo.

## Fontes
- [Behave — Estrutura de testes](https://behave.readthedocs.io/en/stable/gherkin/) — layout do projeto e linguagem Gherkin; consultado em 2026-10-03.
- [Behave — Tutorial](https://behave.readthedocs.io/en/stable/tutorial/) — primeiros passos, ganchos, etiquetas e fixtures; consultado em 2026-10-03.
