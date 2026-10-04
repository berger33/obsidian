---
id: software.testes.tranche19.001300
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/test-structure", "https://github.com/gruntwork-io/terratest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terratest: dividir o teste em estágios

## Em uma frase
A biblioteca de estágios permite separar aplicação, verificação e destruição em blocos que podem ser executados isoladamente por variáveis de ambiente.

## Por que importa
A divisão evita repetir a parte caríssima do ciclo quando apenas a verificação mudou e permite reter o ambiente para inspeção.

## Como funciona
Nomeie os estágios, salve o estado necessário para os seguintes e desative os estágios que não devem rodar naquela execução.

## Exemplo
Um intervalo de depuração pode pular destruição, inspecionar o ambiente e depois executar apenas o estágio de destruição.

## Limites e trade-offs
Estágios sem estado salvo falham ao tentar continuar, e ambientes retidos por engano acumulam custo.

## Como verificar
Execute um único estágio isolado e confirme que ele encontra o estado salvo pelos estágios anteriores.

## Conexões
- [[terratest-destroy]] — Veja também: Terratest: garantir a destruição dos recursos.
- [[terratest-retries]] — Veja também: Terratest: tratar erros transitórios com repetição.

## Fontes
- [Terratest — Módulo test-structure](https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/test-structure) — estágios de teste, estado salvo e variáveis de salto; consultado em 2026-10-03.
- [Terratest — repositório oficial](https://github.com/gruntwork-io/terratest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
