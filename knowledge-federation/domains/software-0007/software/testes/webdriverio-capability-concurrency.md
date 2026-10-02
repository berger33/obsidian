---
id: software.testes.tranche13.000677
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
fontes: ["https://webdriver.io/docs/configuration", "https://webdriver.io/docs/runner/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: limitar workers pela capacidade disponível

## Em uma frase
Configuração do runner combina capabilities de browser e limites de execução concorrente.

## Por que importa
Aumentar workers sem medir capacidade do grid pode criar fila, saturar máquina ou fazer tempo de resposta parecer defeito da aplicação.

## Como funciona
Declare capabilities realmente suportadas, escolha limite global compatível com o serviço de browser e ajuste specs por grupo de custo em vez de multiplicar sessões cegamente.

## Exemplo
Uma CI com quatro slots no grid pode executar quatro sessões e aguardar a próxima quando há mais arquivos que slots disponíveis.

## Limites e trade-offs
Mais paralelismo reduz tempo somente até o gargalo de recursos; parâmetros de CI precisam ser comparados em agentes equivalentes.

## Como verificar
Registre duração, fila e falhas em duas configurações de workers e só aceite aumento se os recursos não estiverem saturados.

## Conexões
- [[webdriverio-selector-contract]] — Veja também: WebdriverIO: escolher seletor que sobreviva a refatoração visual.
- [[webdriverio-spec-file-retries]] — Veja também: WebdriverIO: diagnosticar antes de ativar retry de spec.

## Fontes
- [WebdriverIO — Configuration](https://webdriver.io/docs/configuration) — specs, capabilities, hooks and runner options; consultado em 2026-10-02.
- [WebdriverIO — Runner](https://webdriver.io/docs/runner/) — local and browser runners, workers and isolation; consultado em 2026-10-02.
