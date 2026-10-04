---
id: software.testes.tranche19.001327
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

# BackstopJS: reconhecer limites da comparação visual

## Em uma frase
A verificação mede diferença de pixels, não julga se a mudança é aceitável, e depende de ambiente estável para ser confiável.

## Por que importa
Excesso de cenários instáveis leva o time a ignorar falhas, o que anula o valor da verificação.

## Como funciona
Limite a cobertura aos componentes e fluxos críticos, mantenha o ambiente controlado e trate toda diferença detectada com decisão explícita.

## Exemplo
Um erro de sobreposição de botão em tela estreita é exemplo do tipo de regressão que a verificação pega bem.

## Limites e trade-offs
Variações de renderização entre sistemas operacionais geram diferenças que consomem tempo sem indicar problema real de produto.

## Como verificar
Compare capturas do mesmo cenário em dois ambientes e documente as diferenças que não correspondem a mudança de código.

## Conexões
- [[backstopjs-ci-integration]] — Veja também: BackstopJS: executar na esteira.

## Fontes
- [BackstopJS — Guia de uso](https://github.com/garris/BackstopJS/blob/master/README.md) — cenários, propriedades, tolerância, relatórios e aprovação; consultado em 2026-10-03.
- [BackstopJS — repositório oficial](https://github.com/garris/BackstopJS) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
