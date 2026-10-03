---
id: software.testes.tranche17.001093
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://cucumber.io/docs/cucumber/api/", "https://github.com/cucumber/cucumber-js"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: escolher formatos de relatório

## Em uma frase
A execução pode gerar relatórios legíveis, arquivos estruturados e saídas consumíveis por servidores de integração, a partir do mesmo resultado.

## Por que importa
Formatos distintos atendem revisão humana, arquivamento de evidência e acompanhamento histórico no pipeline.

## Como funciona
Publique o formato estruturado como artefato, gere a página de leitura para revisão e mantenha os nomes dos cenários estáveis para permitir comparação.

## Exemplo
Um relatório de falha pode mostrar o passo exato com o texto do cenário e a captura de tela anexada pelo gancho.

## Limites e trade-offs
Relatórios com anexos podem carregar dados pessoais e crescer rapidamente, exigindo política de retenção.

## Como verificar
Gere dois formatos da mesma execução e confirme que a contagem de cenários e o resultado coincidem entre eles.

## Conexões
- [[cucumber-parallel-execution]] — Veja também: Cucumber: executar cenários em paralelo.
- [[cucumber-living-documentation]] — Veja também: Cucumber: manter a documentação viva.

## Fontes
- [Cucumber — Reference](https://cucumber.io/docs/cucumber/api/) — definições de passo, ganchos, etiquetas, paralelismo e relatórios; consultado em 2026-10-03.
- [Cucumber — repositório oficial](https://github.com/cucumber/cucumber-js) — implementação de referência, exemplos e documentação do projeto; consultado em 2026-10-03.
