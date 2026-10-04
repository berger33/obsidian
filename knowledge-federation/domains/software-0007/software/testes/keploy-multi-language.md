---
id: software.testes.tranche20.001396
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

# Keploy: usar com diferentes linguagens

## Em uma frase
A captura ocorre na camada de rede e funciona com aplicações escritas em diferentes linguagens, sem alteração no código da aplicação.

## Por que importa
A independência de linguagem permite adotar a ferramenta em projetos heterogêneos com o mesmo fluxo de trabalho.

## Como funciona
Verifique a versão da aplicação e os requisitos de ambiente, execute a gravação e mantenha os artefatos no repositório correspondente.

## Exemplo
Serviços em linguagens distintas podem compartilhar o mesmo repositório de artefatos e a mesma rotina de repetição na esteira.

## Limites e trade-offs
Chamadas internas entre serviços podem ser capturadas como dependência, e a atribuição de cada caso ao serviço correto precisa ser verificada.

## Como verificar
Execute a repetição em dois serviços e confirme que cada suíte valida apenas o serviço a que pertence.

## Conexões
- [[keploy-kubernetes-and-sandbox]] — Veja também: Keploy: gravar em ambiente conteinerizado.
- [[keploy-legacy-and-migration]] — Veja também: Keploy: cobrir sistemas legados e migrações.

## Fontes
- [Keploy — Documentação](https://keploy.io/docs/) — instalação, gravação de tráfego, repetição e integração; consultado em 2026-10-03.
- [Keploy — repositório oficial](https://github.com/keploy/keploy) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
