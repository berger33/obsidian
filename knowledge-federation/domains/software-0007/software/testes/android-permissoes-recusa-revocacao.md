---
id: software.testes.tranche08.000177
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
fontes: ["https://developer.android.com/training/testing/other-components/ui-automator", "https://developer.android.com/training/testing/fundamentals"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android: testar concessão, recusa e revogação de permissões

## Em uma frase
Cubra estados de permissão concedida, recusada e alterada nas configurações quando eles mudam o fluxo do aplicativo.

## Por que importa
Um teste apenas com permissão concedida não encontra bloqueios ou mensagens inadequadas para quem recusa ou revoga acesso.

## Como funciona
Inicie cada cenário em estado conhecido, acione a solicitação de permissão e verifique o comportamento em caso positivo e negativo. Faça reset explícito entre execuções.

## Exemplo
Sem permissão de localização, o mapa explica a limitação e oferece alternativa; após concessão, atualiza posição sem exigir reinstalação manual.

## Limites e trade-offs
Políticas e diálogos variam conforme API e configuração do sistema; testo de UI deve declarar versões e não depender de texto transitório sem necessidade.

## Como verificar
Execute cada estado em ambiente limpo, confirme que revogação em Settings é percebida e que o teste seguinte não herda permissão anterior.

## Conexões
- [[android-uiautomator-fronteira-sistema]] — Veja também: Android: UI Automator para fronteiras de sistema.
- [[android-compose-semantics-assertions]] — Veja também: Android Compose: testar semântica e ações expostas.

## Fontes
- [Android — UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) — interação com aplicativos e interface do sistema; consultado em 2026-10-02.
- [Android — Fundamentals of testing](https://developer.android.com/training/testing/fundamentals) — escopo, ambiente e tipos de teste Android; consultado em 2026-10-02.
