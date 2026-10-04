---
id: software.testes.tranche16.000960
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

# Detox: estabilizar a execução em integração contínua

## Em uma frase
Ambientes de integração contínua sofrem com animações habilitadas, emuladores lentos e recursos limitados, o que altera o tempo das transições.

## Por que importa
Grande parte da instabilidade atribuída ao framework vem de diferenças de ambiente e não de defeitos no aplicativo ou no teste.

## Como funciona
Desative animações no dispositivo de teste, dimensione o executor com recursos suficientes e ajuste limites apenas para telas reconhecidamente lentas.

## Exemplo
Um caso aprovado localmente pode falhar no pipeline quando a primeira transição de navegação demora mais do que o limite padrão de espera.

## Limites e trade-offs
Aumentar limites sem investigar esconde regressão de desempenho, e repetições automáticas podem transformar falha real em ruído aceito.

## Como verificar
Rode a suíte completa no executor de integração contínua ao menos duas vezes por revisão e compare tempos e falhas antes de ajustar qualquer limite.

## Conexões
- [[detox-configuration-file]] — Veja também: Detox: descrever alvos no arquivo de configuração.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — repositório oficial](https://github.com/wix/Detox) — visão geral do projeto, documentação complementar e exemplos; consultado em 2026-10-03.
