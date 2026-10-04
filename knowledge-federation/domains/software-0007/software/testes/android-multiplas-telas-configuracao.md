---
id: software.testes.tranche08.000175
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
fontes: ["https://developer.android.com/training/testing/different-screens", "https://developer.android.com/training/testing/fundamentals"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android: cobrir tamanhos de tela e configuração

## Em uma frase
Valide layouts em configurações representativas de tela e densidade, sem assumir uma única dimensão de dispositivo.

## Por que importa
Quebras de layout podem depender de largura, orientação, densidade e recursos disponíveis, mesmo quando lógica funcional permanece correta.

## Como funciona
Selecione combinações que representam classes de risco, preserve screenshots ou assertions semânticas e teste mudança de configuração quando o estado deve ser mantido.

## Exemplo
O mesmo fluxo de formulário é aberto em tela estreita e larga; o teste verifica que ação principal continua visível e que valores preenchidos sobrevivem à rotação.

## Limites e trade-offs
Uma matriz exaustiva de dispositivos é cara; os cenários devem ser escolhidos por suporte, telemetria e risco, não por número arbitrário.

## Como verificar
Execute presets de emulador diferentes, inspecione conteúdo cortado e valide restauração após rotação e redimensionamento quando aplicável.

## Conexões
- [[android-process-death-restauracao-estado]] — Veja também: Android: testar restauração após recriação do processo.
- [[flutter-orientacao-layout-widget-test]] — Veja também: Flutter: validar orientação retrato e paisagem.

## Fontes
- [Android — Different screen sizes](https://developer.android.com/training/testing/different-screens) — tamanhos de tela, configuração e restauração de estado; consultado em 2026-10-02.
- [Android — Fundamentals of testing](https://developer.android.com/training/testing/fundamentals) — escopo, ambiente e tipos de teste Android; consultado em 2026-10-02.
