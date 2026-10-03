---
id: software.testes.tranche17.001067
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

# Locust: ponderar tarefas do usuário

## Em uma frase
Cada tarefa recebe um peso que determina sua frequência relativa, permitindo representar a mistura de comportamentos observada no uso.

## Por que importa
Sem ponderação, todas as ações têm a mesma chance e a carga resultante não corresponde ao perfil real de tráfego.

## Como funciona
Atribua pesos conforme a proporção medida, mantenha cada tarefa com um objetivo claro e agrupe variações de dados dentro da própria tarefa.

## Exemplo
Uma tarefa de navegação pode receber peso maior do que a de finalização de compra, refletindo o funil observado.

## Limites e trade-offs
Pesos sem justificativa viram números arbitrários, e a proporção dos pesos não equivale à proporção de requisições quando cada tarefa dispara vários pedidos.

## Como verificar
Compare a contagem de execuções por tarefa no resumo com os pesos declarados e ajuste a interpretação quando houver múltiplas requisições por tarefa.

## Conexões
- [[locust-locustfile-structure]] — Veja também: Locust: escrever o arquivo de teste.
- [[locust-wait-time]] — Veja também: Locust: modelar o tempo entre ações.

## Fontes
- [Locust — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — classes de usuário, tarefas, pesos, tempos de espera e ciclo de vida; consultado em 2026-10-03.
- [Locust — Quickstart](https://docs.locust.io/en/stable/quickstart.html) — primeira execução, parâmetros de linha de comando e resumo de estatísticas; consultado em 2026-10-03.
