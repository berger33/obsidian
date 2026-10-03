---
id: software.testes.tranche16.000979
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

# Vegeta: transformar o resumo em verificação automática

## Em uma frase
O relatório pode ser emitido em formato estruturado, o que permite extrair percentuais e proporções e reprovar a execução quando os valores desviam do esperado.

## Por que importa
Verificação automática impede que regressões de latência avancem sem revisão, substituindo a leitura manual do resumo.

## Como funciona
Grave o resultado estruturado, extraia as métricas escolhidas no pipeline e compare com limites versionados junto do projeto.

## Exemplo
Um limite pode exigir que a proporção de sucesso permaneça acima de um patamar e que o percentil de latência fique abaixo de um teto acordado.

## Limites e trade-offs
Limites baseados em execução única são frágeis, e o ambiente compartilhado do pipeline introduz variação que precisa ser separada do efeito da mudança.

## Como verificar
Aprove a verificação em uma execução de referência e provoque uma degradação controlada para confirmar que a falha é detectada.

## Conexões
- [[vegeta-timeouts-and-transport]] — Veja também: Vegeta: configurar tempo limite e transporte HTTP.
- [[vegeta-library-usage]] — Veja também: Vegeta: usar a biblioteca em programa próprio.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
