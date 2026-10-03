---
id: software.testes.tranche18.001165
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
fontes: ["https://docs.cypress.io/guides/overview/why-cypress", "https://github.com/cypress-io/cypress"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: investigar falhas com artefatos

## Em uma frase
A execução registra vídeos e capturas, permite consultar o log de comandos e o tráfego de rede, e oferece modo interativo para inspeção.

## Por que importa
Falhas em integração contínua são difíceis de reproduzir, e a evidência gravada no momento do erro encurta a análise.

## Como funciona
Grave artefatos apenas em falhas no pipeline, preserve-os como saída do trabalho e use o modo interativo durante o desenvolvimento.

## Exemplo
Uma captura imediatamente antes da falha mostra o estado da tela e a mensagem apresentada, orientando a correção.

## Limites e trade-offs
Vídeos e capturas podem conter dados pessoais e crescer rapidamente, exigindo política de retenção no repositório de artefatos.

## Como verificar
Provoque uma falha controlada e confirme que o artefato publicado contém a evidência do estado da aplicação.

## Conexões
- [[cypress-timeouts-and-stability]] — Veja também: Cypress: ajustar tempos e reduzir instabilidade.
- [[cypress-ci-parallelization]] — Veja também: Cypress: paralelizar e executar no pipeline.

## Fontes
- [Cypress — Documentation](https://docs.cypress.io/guides/overview/why-cypress) — visão geral do executor, comandos, artefatos e execução paralela; consultado em 2026-10-03.
- [Cypress — repositório oficial](https://github.com/cypress-io/cypress) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
