---
id: software.testes.tranche19.001325
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/garris/BackstopJS/blob/master/README.md", "https://github.com/garris/BackstopJS"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# BackstopJS: revisar o relatório e aprovar mudanças

## Em uma frase
O relatório apresenta comparação lado a lado com destaque da diferença, e o comando de aprovação promove as capturas recentes a novas referências.

## Por que importa
A revisão humana da diferença é o ponto em que se decide se a mudança visual é intencional antes de atualizar a referência.

## Como funciona
Revise o relatório antes de aprovar, filtre a aprovação pelo cenário pretendido e versione as referências atualizadas junto do código.

## Exemplo
Uma mudança deliberada de tipografia exige revisar as capturas afetadas e aprovar apenas essas antes de enviar a alteração.

## Limites e trade-offs
Aprovar em massa aceita regressões não percebidas, e referências não versionadas divergem entre máquinas e ambiente de integração.

## Como verificar
Aprove um cenário específico e confirme que a execução seguinte passa nele e continua falhando nos demais inalterados.

## Conexões
- [[backstopjs-viewports]] — Veja também: BackstopJS: cobrir tamanhos de tela.
- [[backstopjs-ci-integration]] — Veja também: BackstopJS: executar na esteira.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — repositório oficial](https://github.com/garris/BackstopJS) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
