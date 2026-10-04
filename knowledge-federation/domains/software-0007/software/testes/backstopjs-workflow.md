---
id: software.testes.tranche19.001318
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

# BackstopJS: comparar capturas contra referências

## Em uma frase
O fluxo gera capturas de referência, produz novas capturas na execução de teste e compara pixel a pixel contra a referência aprovada.

## Por que importa
A comparação visual detecta regressões de estilo que asserções de estrutura não percebem, como sobreposição e deslocamento.

## Como funciona
Gere a referência inicial, execute o teste a cada mudança relevante e só aprove após revisar a diferença.

## Exemplo
Uma alteração de espaçamento entre elementos pode passar pelos testes funcionais e ser flagrada pela comparação visual.

## Limites e trade-offs
Referências desatualizadas geram falhas constantes, e aprovar tudo sem revisão transforma a verificação em carimbo.

## Como verificar
Execute o teste sem alterar o código e confirme que ele passa, provando que as referências correspondem ao estado atual.

## Conexões
- [[backstopjs-scenarios]] — Veja também: BackstopJS: descrever cenários.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — repositório oficial](https://github.com/garris/BackstopJS) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
