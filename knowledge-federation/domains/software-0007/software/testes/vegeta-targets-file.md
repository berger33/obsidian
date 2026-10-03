---
id: software.testes.tranche16.000973
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

# Vegeta: descrever alvos com cabeçalhos e corpos

## Em uma frase
O arquivo de alvos contém método e URL por linha, aceitando cabeçalhos adicionais no bloco seguinte e referência a arquivo de corpo para requisições que enviam dados.

## Por que importa
Centralizar os alvos permite variar o conjunto de rotas sem reescrever a linha de comando e mantém o teste versionado junto do serviço.

## Como funciona
Separe os alvos em linhas, indique o corpo por referência de arquivo quando houver envio e leia o arquivo lentamente apenas se a lista for gerada dinamicamente.

## Exemplo
Um alvo de criação pode declarar método e URL, cabeçalho de autorização e o arquivo JSON que compõe o corpo da requisição.

## Limites e trade-offs
Linhas em branco separam blocos e um erro de formatação silencioso muda o alvo efetivamente atingido; o arquivo precisa ser revisado como código.

## Como verificar
Execute o ataque com um alvo deliberadamente inválido e confirme que a falha aparece no relatório em vez de ser ignorada.

## Conexões
- [[vegeta-attack-basics]] — Veja também: Vegeta: executar um ataque de taxa constante.
- [[vegeta-report-metrics]] — Veja também: Vegeta: ler o relatório de resultados.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
