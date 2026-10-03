---
id: software.testes.tranche16.000951
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
fontes: ["https://wix.github.io/Detox/docs/introduction/getting-started", "https://wix.github.io/Detox/docs/introduction/project-setup"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Detox: preferir identificadores de testabilidade

## Em uma frase
Matchers baseados em identificador procuram o valor de testabilidade definido no componente, enquanto texto e rótulo dependem de conteúdo visível.

## Por que importa
Rótulos mudam com idioma, revisão de texto e contexto, e uma busca por texto passa a encontrar vários candidatos sem que ninguém perceba.

## Como funciona
Defina identificadores estáveis por tela ou fluxo, use o matcher correspondente nas ações e reserva matchers de texto para verificações de conteúdo exibido.

## Exemplo
Um botão de entrar com identificador dedicado pode ser tocado por esse identificador, e outra asserção verifica que o rótulo apresentado corresponde ao esperado.

## Limites e trade-offs
Identificador ausente ou repetido em dois elementos produz erro de ambiguidade; a convenção precisa ser mantida pelo time do aplicativo, não inventada no teste.

## Como verificar
Renomeie um rótulo visível e confirme que o teste continua passando; duplique um identificador e verifique que a execução falha por ambiguidade.

## Conexões
- [[detox-synchronization-gray-box]] — Veja também: Detox: confiar na sincronização com operações pendentes.
- [[detox-launchapp-options]] — Veja também: Detox: controlar o lançamento do aplicativo.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — Project Setup](https://wix.github.io/Detox/docs/introduction/project-setup) — configuração por alvo, arquivo de configuração e comandos de build e teste; consultado em 2026-10-03.
