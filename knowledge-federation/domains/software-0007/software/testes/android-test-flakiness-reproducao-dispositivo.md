---
id: software.testes.tranche08.000179
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://developer.android.com/training/testing/instrumented-tests/stability", "https://developer.android.com/training/testing/different-screens"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android: tornar falhas instrumentadas reproduzíveis

## Em uma frase
Registre versão do sistema, configuração e estado inicial para que falhas instrumentadas possam ser reproduzidas fora do dispositivo original.

## Por que importa
Diferenças de API, orientação, animações e dados podem produzir comportamento distinto; sem metadados a falha fica difícil de separar de instabilidade.

## Como funciona
Fixe ou registre imagem do emulador, idioma, permissões, rede e dados iniciais. Capture logs e trace junto ao resultado sem transformar retry em aprovação silenciosa.

## Exemplo
Uma falha só em API recente registra versão, densidade e estado de permissão; o cenário mínimo pode então ser executado em matriz controlada.

## Limites e trade-offs
Ambiente repetível reduz variáveis, mas não substitui teste em aparelhos suportados nem elimina diferenças de fabricantes e recursos físicos.

## Como verificar
Rode novamente com configuração registrada e compare resultado; varie uma dimensão por vez até identificar se a causa é de ambiente ou produto.

## Conexões
- [[android-instrumented-sincronizacao-sem-sleep]] — Veja também: Android: sincronizar testes instrumentados sem sleeps fixos.
- [[android-multiplas-telas-configuracao]] — Veja também: Android: cobrir tamanhos de tela e configuração.

## Fontes
- [Android — Big test stability](https://developer.android.com/training/testing/instrumented-tests/stability) — sincronização e redução de flakiness em testes grandes; consultado em 2026-10-02.
- [Android — Different screen sizes](https://developer.android.com/training/testing/different-screens) — tamanhos de tela, configuração e restauração de estado; consultado em 2026-10-02.
