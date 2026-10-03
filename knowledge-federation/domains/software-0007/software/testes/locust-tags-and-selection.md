---
id: software.testes.tranche17.001072
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
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html", "https://docs.locust.io/en/stable/quickstart.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: selecionar tarefas por etiquetas

## Em uma frase
Tarefas podem receber etiquetas e a execução pode incluir ou excluir etiquetas específicas, permitindo reaproveitar o mesmo arquivo em cenários diferentes.

## Por que importa
Suítes grandes precisam de recortes para testes rápidos sem duplicar arquivos de carga.

## Como funciona
Aplique etiquetas por área ou tipo de fluxo, documente a convenção e use a seleção por linha de comando conforme o objetivo da execução.

## Exemplo
Uma execução de fumaça pode incluir apenas tarefas marcadas como leitura, deixando os fluxos de escrita para a rodada completa.

## Limites e trade-offs
Etiquetas inconsistentes quebram a seleção silenciosamente, e a exclusão de uma tarefa pode alterar a proporção entre as restantes.

## Como verificar
Execute com e sem filtro de etiqueta e compare a lista de tarefas ativas apresentada no início do teste.

## Conexões
- [[locust-response-validation]] — Veja também: Locust: marcar falhas com validação explícita.
- [[locust-distributed-execution]] — Veja também: Locust: distribuir a carga entre processos.

## Fontes
- [Locust — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — classes de usuário, tarefas, pesos, tempos de espera e ciclo de vida; consultado em 2026-10-03.
- [Locust — Quickstart](https://docs.locust.io/en/stable/quickstart.html) — primeira execução, parâmetros de linha de comando e resumo de estatísticas; consultado em 2026-10-03.
