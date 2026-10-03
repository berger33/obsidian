---
id: software.testes.tranche17.001104
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
fontes: ["https://www.selenium.dev/documentation/webdriver/waits/", "https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: diagnosticar instabilidade

## Em uma frase
Falhas intermitentes costumam vir de esperas mal colocadas, dados compartilhados, animações ou dependências externas lentas, e não do driver.

## Por que importa
Tratar instabilidade com pausas maiores esconde a causa e degrada a confiança na suíte, que passa a ser ignorada quando falha.

## Como funciona
Investigue a origem com registro detalhado, isole dados por teste e substitua esperas fixas por condições observáveis.

## Exemplo
Um botão que às vezes não recebe o clique costuma estar coberto por elemento animado, e a espera pela animação terminar resolve a origem.

## Limites e trade-offs
Mascarar a falha com repetição automática reduz o sinal disponível e posterga a correção do problema real.

## Como verificar
Repita o caso que falha isoladamente, com dados próprios, e verifique se a falha desaparece, indicando dependência entre testes.

## Conexões
- [[selenium-screenshot-and-evidence]] — Veja também: Selenium: registrar evidências de falha.
- [[selenium-limits-and-practices]] — Veja também: Selenium: reconhecer limites e boas práticas.

## Fontes
- [Selenium — Waits](https://www.selenium.dev/documentation/webdriver/waits/) — espera implícita e explícita por condições observáveis; consultado em 2026-10-03.
- [Selenium — Page object models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/) — objetos de página e de componente e boas práticas de estruturação; consultado em 2026-10-03.
