---
id: software.testes.tranche17.001092
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

# Cucumber: executar cenários em paralelo

## Em uma frase
A execução pode distribuir cenários entre processos, respeitando limites de paralelismo e mantendo relatórios individuais por processo.

## Por que importa
Suítes de aceitação crescem e passam a dominar o tempo do pipeline, e o paralelismo reduz a espera sem alterar os cenários.

## Como funciona
Mantenha cenários independentes, isole dados por execução e ajuste o número de processos à capacidade da máquina e do ambiente de teste.

## Exemplo
Dois processos podem rodar fluxos distintos desde que criem registros com identificadores próprios, evitando colisão de dados.

## Limites e trade-offs
Cenários com estado compartilhado ou que dependem de ordem quebram quando paralelizados, e o relatório precisa ser combinado corretamente.

## Como verificar
Execute a suíte com um processo e com vários e compare o resultado, investigando qualquer diferença como sinal de acoplamento oculto.

## Conexões
- [[cucumber-background-and-data-tables]] — Veja também: Cucumber: compartilhar contexto e tabelas.
- [[cucumber-reports]] — Veja também: Cucumber: escolher formatos de relatório.

## Fontes
- [Cucumber — Reference](https://cucumber.io/docs/cucumber/api/) — definições de passo, ganchos, etiquetas, paralelismo e relatórios; consultado em 2026-10-03.
- [Cucumber — repositório oficial](https://github.com/cucumber/cucumber-js) — implementação de referência, exemplos e documentação do projeto; consultado em 2026-10-03.
