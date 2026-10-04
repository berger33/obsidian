---
id: software.testes.tranche18.001222
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://www.npmjs.com/package/@axe-core/playwright", "https://github.com/dequelabs/axe-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: integrar ao teste de navegador

## Em uma frase
O pacote de integração injeta a biblioteca na página e executa a análise durante o teste de interface, com limite de tempo e opções.

## Por que importa
Analisar dentro do teste de navegador permite verificar estados que só existem após interação.

## Como funciona
Injete a biblioteca na página, execute a análise em pontos definidos do fluxo e falhe o teste conforme a política de violações escolhida.

## Exemplo
Um fluxo pode analisar a tela após abrir o formulário de cadastro e antes de enviar os dados.

## Limites e trade-offs
Analisar a página inteira em cada passo alonga muito a suíte, e o momento da análise precisa corresponder ao estado que se quer verificar.

## Como verificar
Execute a análise antes e depois de abrir um componente e compare as violações encontradas em cada estado.

## Conexões
- [[axe-experimental-rules]] — Veja também: axe-core: tratar regras experimentais.
- [[axe-ci-policy]] — Veja também: axe-core: definir política de bloqueio no pipeline.

## Fontes
- [axe-core — Integração com Playwright](https://www.npmjs.com/package/@axe-core/playwright) — execução da análise durante testes de navegador; consultado em 2026-10-03.
- [axe-core — repositório oficial](https://github.com/dequelabs/axe-core) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
