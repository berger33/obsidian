---
id: software.testes.tranche16.000957
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
fontes: ["https://wix.github.io/Detox/docs/introduction/getting-started", "https://github.com/wix/Detox"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Detox: usar ações de dispositivo no fluxo

## Em uma frase
Ações de dispositivo cobrem operações fora da árvore de interface, como enviar o aplicativo ao segundo plano, retomá-lo e capturar a tela em um ponto nomeado.

## Por que importa
Fluxos móveis reais envolvem interrupções e retomadas, e testá-los apenas dentro do aplicativo deixa caminhos de ciclo de vida sem verificação.

## Como funciona
Encadeie as ações de dispositivo no momento exato do fluxo, mantendo o estado esperado explícito no próprio caso.

## Exemplo
Um cenário de rascunho pode enviar o aplicativo ao segundo plano, retomá-lo e verificar que o conteúdo não salvo continua disponível na tela.

## Limites e trade-offs
A retomada depende de o processo continuar vivo; encerramentos forçados pelo sistema exigem outro caminho de teste e não são reproduzidos por essa ação.

## Como verificar
Repita o ciclo de segundo plano e retomada duas vezes e confirme que o estado observado permanece consistente em ambas.

## Conexões
- [[detox-disable-synchronization-scope]] — Veja também: Detox: restringir a desativação da sincronização.
- [[detox-artifacts-failure]] — Veja também: Detox: preservar artefatos das falhas.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — repositório oficial](https://github.com/wix/Detox) — visão geral do projeto, documentação complementar e exemplos; consultado em 2026-10-03.
