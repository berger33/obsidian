---
id: software.testes.tranche16.000950
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

# Detox: confiar na sincronização com operações pendentes

## Em uma frase
O Detox observa rede, temporizadores e animações do aplicativo e espera a estabilização antes de executar cada ação ou asserção.

## Por que importa
Testes móveis falham por agir enquanto a interface ainda processa trabalho assíncrono, e pausas fixas escondem esse acoplamento em vez de resolvê-lo.

## Como funciona
Deixe a sincronização padrão trabalhar e investigue a causa sempre que precisar desativá-la, porque a exceção costuma indicar operação que a ferramenta não consegue reconhecer.

## Exemplo
Uma tela que busca dados ao abrir pode ser testada tocando no botão seguinte diretamente, já que o framework aguarda a conclusão da chamada pendente.

## Limites e trade-offs
A sincronização cobre o que consegue observar; tarefas em módulos nativos ou em laços longos podem escapar da detecção e exigir espera explícita.

## Como verificar
Introduza uma operação artificialmente longa no aplicativo e confirme que a ação seguinte só ocorre após a estabilização, sem pausa inserida no teste.

## Conexões
- [[detox-testid-selectors]] — Veja também: Detox: preferir identificadores de testabilidade.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — repositório oficial](https://github.com/wix/Detox) — visão geral do projeto, documentação complementar e exemplos; consultado em 2026-10-03.
