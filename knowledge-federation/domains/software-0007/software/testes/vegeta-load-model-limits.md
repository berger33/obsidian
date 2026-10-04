---
id: software.testes.tranche16.000981
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
fontes: ["https://github.com/tsenart/vegeta", "https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vegeta: reconhecer os limites do modelo de taxa constante

## Em uma frase
O ataque mantém taxa fixa de início de requisições, comportamento que difere de sistemas reais com usuários que esperam respostas antes de agir.

## Por que importa
Interpretar o resultado como simulação de uso real superestima a pressão sobre conexões e subestima efeitos de jornada longa com estado.

## Como funciona
Use o modelo para medir capacidade e saturação de endpoints e complemente com ferramentas de jornada quando o objetivo for representar comportamento de usuários.

## Exemplo
Uma medição de saturação pode elevar a taxa em degraus sucessivos até que a latência deixe de permanecer estável entre patamares.

## Limites e trade-offs
Métricas sem observabilidade do servidor não indicam qual recurso saturou, e uma taxa constante pode mascarar filas internas que só aparecem em modo fechado.

## Como verificar
Compare a curva de latência em vários patamares de taxa e identifique o ponto em que o crescimento deixa de ser proporcional ao aumento de carga.

## Conexões
- [[vegeta-library-usage]] — Veja também: Vegeta: usar a biblioteca em programa próprio.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
