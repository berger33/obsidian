---
id: software.testes.tranche20.001391
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
fontes: ["https://keploy.io/docs/", "https://github.com/keploy/keploy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Keploy: repetir na esteira de integração

## Em uma frase
No modo de repetição, os pedidos gravados são reenviados, os mocks são servidos no lugar das dependências e o resultado é comparado com o registro.

## Por que importa
A repetição determinística transforma os artefatos gravados em verificação de regressão executável a cada revisão.

## Como funciona
Suba a aplicação, execute a repetição e trate a saída diferente do registro como falha que interrompe o trabalho.

## Exemplo
A esteira pode rodar a suíte gravada em cada revisão de código, sem banco nem serviços externos disponíveis.

## Limites e trade-offs
Respostas que mudam legitimamente entre ambientes geram diferenças apontadas como falha, e a comparação exige normalização de campos voláteis.

## Como verificar
Provoque uma mudança de comportamento e confirme que a repetição falha indicando o caso e a diferença observada.

## Conexões
- [[keploy-dependency-mocks]] — Veja também: Keploy: registrar dependências como mocks.
- [[keploy-test-assertions]] — Veja também: Keploy: ler e ajustar as verificações geradas.

## Fontes
- [Keploy — Documentação](https://keploy.io/docs/) — instalação, gravação de tráfego, repetição e integração; consultado em 2026-10-03.
- [Keploy — repositório oficial](https://github.com/keploy/keploy) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
