---
id: software.testes.tranche16.000967
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
fontes: ["https://www.artillery.io/docs/reference/extensions/ensure", "https://www.artillery.io/docs/get-started/first-test"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Artillery: verificar respostas com asserções

## Em uma frase
A extensão de asserções permite declarar condições sobre cada resposta, como código de status e campo do corpo, falhando o passo quando o contrato não é atendido.

## Por que importa
Sem verificação de conteúdo, uma resposta com erro de aplicação mas código de sucesso passa como comportamento normal sob carga.

## Como funciona
Declare as condições no passo que as produz, usando campos estáveis do contrato e evitando comparações de corpo inteiro quando houver valores voláteis.

## Exemplo
Um passo de criação pode exigir código de sucesso e presença do identificador no corpo antes de permitir a continuação do cenário.

## Limites e trade-offs
Cada asserção acrescenta trabalho ao gerador de carga e pode reduzir a taxa alcançada; o custo precisa ser considerado ao interpretar a medição.

## Como verificar
Introduza um campo ausente no serviço de teste e confirme que o passo falha com mensagem apontando a condição violada.

## Conexões
- [[artillery-browser-engine]] — Veja também: Artillery: medir navegador com mecanismo de browser.
- [[artillery-quick-and-run]] — Veja também: Artillery: escolher entre execução rápida e arquivo.

## Fontes
- [Artillery — ensure](https://www.artillery.io/docs/reference/extensions/ensure) — limites e condições sobre métricas com código de saída não nulo; consultado em 2026-10-03.
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
