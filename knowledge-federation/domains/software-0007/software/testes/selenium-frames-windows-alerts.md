---
id: software.testes.tranche17.001100
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
fontes: ["https://www.selenium.dev/documentation/webdriver/waits/", "https://github.com/SeleniumHQ/selenium"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: alternar entre contextos

## Em uma frase
O driver permite entrar em quadros, mudar de janela e tratar caixas de diálogo, sempre com troca explícita de contexto antes de interagir.

## Por que importa
Conteúdo em quadros e janelas secundárias não é alcançado pelos mesmos comandos, e esquecer a troca produz erros difíceis de interpretar.

## Como funciona
Mude para o contexto correto antes de agir, guarde a referência original para voltar e trate a caixa de diálogo conforme o tipo esperado.

## Exemplo
Um fluxo de pagamento pode abrir janela de confirmação e exigir retorno à janela principal após a conclusão.

## Limites e trade-offs
Não voltar ao contexto original deixa o restante do teste procurando elementos na página errada, e diálogos inesperados bloqueiam a execução.

## Como verificar
Force a abertura de uma janela secundária e confirme que o teste retorna ao contexto principal antes da verificação final.

## Conexões
- [[selenium-actions-api]] — Veja também: Selenium: executar interações complexas.
- [[selenium-grid-distributed]] — Veja também: Selenium: distribuir sessões com a grade.

## Fontes
- [Selenium — Waits](https://www.selenium.dev/documentation/webdriver/waits/) — espera implícita e explícita por condições observáveis; consultado em 2026-10-03.
- [Selenium — repositório oficial](https://github.com/SeleniumHQ/selenium) — código-fonte e documentação das ligações por linguagem; consultado em 2026-10-03.
