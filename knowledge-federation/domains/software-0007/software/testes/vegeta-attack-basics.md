---
id: software.testes.tranche16.000972
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

# Vegeta: executar um ataque de taxa constante

## Em uma frase
O subcomando de ataque recebe alvos, uma taxa em requisições por segundo e uma duração, emitindo um fluxo binário com os resultados.

## Por que importa
Medições sob taxa controlada permitem comparar revisões com a mesma carga, o que uma execução ad hoc não consegue oferecer.

## Como funciona
Informe o arquivo de alvos, defina taxa e duração explícitas, e grave a saída em arquivo para análise posterior.

## Exemplo
Um ataque de curta duração contra um serviço de saúde serve como verificação inicial antes de séries mais longas.

## Limites e trade-offs
A execução real pode ultrapassar o tempo pedido porque as últimas respostas pendentes ainda precisam terminar, então o tempo de parede não é igual à duração configurada.

## Como verificar
Repita o mesmo ataque duas vezes e compare o total de requisições com o produto entre taxa e duração, considerando o período de escoamento.

## Conexões
- [[vegeta-targets-file]] — Veja também: Vegeta: descrever alvos com cabeçalhos e corpos.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
