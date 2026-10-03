---
id: software.testes.tranche17.001075
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
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html", "https://github.com/locustio/locust"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: interpretar resultados com cautela

## Em uma frase
O resumo apresenta latências por percentil, taxa de requisições e falhas, mas descreve apenas o ponto de vista do cliente simulado.

## Por que importa
Números de carga sem contexto de infraestrutura e de dados levam a conclusões erradas sobre a capacidade real do sistema.

## Como funciona
Registre a configuração usada, acompanhe a telemetria do serviço durante a execução e compare resultados obtidos no mesmo ambiente.

## Exemplo
Um teste com código de falha zero pode ainda ter latências de cauda inaceitáveis, que só aparecem ao ler percentuais altos.

## Limites e trade-offs
Diferenças pequenas entre execuções ficam dentro da variância do ambiente, e a escolha de dados influencia o custo das operações no banco.

## Como verificar
Repita a mesma configuração em dois dias distintos e verifique se a variação observada permite distinguir o efeito de uma mudança real.

## Conexões
- [[locust-headless-and-ci]] — Veja também: Locust: executar sem interface e automatizar.

## Fontes
- [Locust — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — classes de usuário, tarefas, pesos, tempos de espera e ciclo de vida; consultado em 2026-10-03.
- [Locust — repositório oficial](https://github.com/locustio/locust) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
