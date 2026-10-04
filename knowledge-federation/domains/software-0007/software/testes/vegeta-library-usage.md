---
id: software.testes.tranche16.000980
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib", "https://github.com/tsenart/vegeta"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vegeta: usar a biblioteca em programa próprio

## Em uma frase
A ferramenta expõe biblioteca em Go que permite definir alvos dinâmicos, alimentar dados variáveis e consumir resultados no mesmo processo.

## Por que importa
Cenários que dependem de identificadores gerados ou de lógica de negócio não cabem em arquivo estático e pedem um gerador programático.

## Como funciona
Use a biblioteca quando o alvo precisar ser calculado, mantendo a taxa e a duração explícitas e acumulando as métricas para análise ao final.

## Exemplo
Um programa pode gerar identificadores sequenciais para cada requisição e calcular percentuais a partir do conjunto acumulado de resultados.

## Limites e trade-offs
Código próprio transfere para o time a responsabilidade por aquecimento, paralelismo e tratamento de erros que a ferramenta já resolve na linha de comando.

## Como verificar
Compare as métricas do programa com as do ataque equivalente por linha de comando para validar a implementação antes de adotá-la.

## Conexões
- [[vegeta-thresholds-in-ci]] — Veja também: Vegeta: transformar o resumo em verificação automática.
- [[vegeta-load-model-limits]] — Veja também: Vegeta: reconhecer os limites do modelo de taxa constante.

## Fontes
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
