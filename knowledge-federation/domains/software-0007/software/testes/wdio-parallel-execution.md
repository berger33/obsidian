---
id: software.testes.tranche18.001175
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

# WebdriverIO: executar em paralelo

## Em uma frase
A configuração permite distribuir arquivos de teste entre instâncias de navegador, com limite de processos simultâneos definido por capacidade.

## Por que importa
A execução paralela reduz o tempo total, desde que os casos sejam independentes e os recursos da máquina suportem a carga.

## Como funciona
Defina o número de instâncias conforme a capacidade, mantenha dados isolados por processo e considere testes de ordem obrigatória como exceção explícita.

## Exemplo
Dois processos podem rodar arquivos distintos desde que criem registros próprios, evitando colisão de dados.

## Limites e trade-offs
Excesso de instâncias provoca disputa de memória e instabilidade, e casos com estado compartilhado falham de forma intermitente.

## Como verificar
Rode a suíte com uma e com várias instâncias e compare o resultado, investigando divergências como sinal de acoplamento.

## Conexões
- [[wdio-reporters-and-artifacts]] — Veja também: WebdriverIO: escolher relatórios e evidências.
- [[wdio-mobile-and-multiremote]] — Veja também: WebdriverIO: cobrir plataformas e múltiplos alvos.

## Fontes
- [WebdriverIO — Documentation](https://webdriver.io/docs/gettingstarted) — configuração, modos de execução, serviços e paralelismo; consultado em 2026-10-03.
- [WebdriverIO — repositório oficial](https://github.com/webdriverio/webdriverio) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
