---
id: software.testes.tranche13.000674
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://webdriver.io/docs/runner/", "https://webdriver.io/docs/configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: entender isolamento do Local Runner

## Em uma frase
No Local Runner, cada arquivo de teste roda em processo worker separado por capability, com sua própria sessão de browser.

## Por que importa
Separação por processo aumenta isolamento e concorrência, mas impede compartilhar automaticamente variáveis entre arquivos de teste.

## Como funciona
Mantenha fixtures no escopo do arquivo, agrupe specs que precisam de execução serial ou use o serviço oficial de shared store para o dado mínimo que realmente atravessa workers.

## Exemplo
Dois arquivos que criam pedidos podem usar sessões distintas e identificadores únicos, sem assumir que uma variável global definida no primeiro estará no segundo.

## Limites e trade-offs
Um shared store não substitui isolamento de dados no serviço de aplicação e pode transformar dependência entre arquivos em acoplamento difícil de depurar.

## Como verificar
Execute dois arquivos em workers diferentes, remova qualquer estado local compartilhado e confirme que cada um pode rodar sozinho.

## Conexões
- [[webdriverio-soft-assertion-aggregation]] — Veja também: WebdriverIO: acumular falhas independentes com soft assertions.
- [[webdriverio-browser-runner-boundary]] — Veja também: WebdriverIO: escolher Browser Runner para teste de componentes.

## Fontes
- [WebdriverIO — Runner](https://webdriver.io/docs/runner/) — local and browser runners, workers and isolation; consultado em 2026-10-02.
- [WebdriverIO — Configuration](https://webdriver.io/docs/configuration) — specs, capabilities, hooks and runner options; consultado em 2026-10-02.
