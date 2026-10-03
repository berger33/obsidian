---
id: software.testes.tranche18.001169
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
fontes: ["https://webdriver.io/docs/gettingstarted", "https://github.com/webdriverio/webdriverio"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: controlar o modo síncrono e assíncrono

## Em uma frase
O framework oferece modo síncrono que oculta as promessas e modo assíncrono explícito, com regras distintas de configuração.

## Por que importa
Misturar os dois estilos produz erros confusos, e a escolha precisa ser uniforme em toda a suíte para manter a leitura.

## Como funciona
Defina o modo na configuração do projeto, mantenha a mesma convenção nos arquivos e trate operações assíncronas com espera explícita.

## Exemplo
No modo síncrono as chamadas aparecem sem aguardar promessa, e no assíncrono cada chamada precisa ser aguardada antes da seguinte.

## Limites e trade-offs
Esquecer de aguardar no modo assíncrono faz a verificação rodar antes da ação concluir, produzindo falha intermitente.

## Como verificar
Execute a suíte nos dois modos e confirme que os resultados funcionais coincidem antes de fixar a convenção.

## Conexões
- [[wdio-waiting-strategies]] — Veja também: WebdriverIO: esperar condições de elemento.
- [[wdio-element-commands]] — Veja também: WebdriverIO: compor ações de elemento.

## Fontes
- [WebdriverIO — Documentation](https://webdriver.io/docs/gettingstarted) — configuração, modos de execução, serviços e paralelismo; consultado em 2026-10-03.
- [WebdriverIO — repositório oficial](https://github.com/webdriverio/webdriverio) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
