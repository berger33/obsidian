---
id: software.testes.tranche08.000173
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
fontes: ["https://developer.android.com/develop/ui/compose/testing", "https://developer.android.com/training/testing/fundamentals"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android Compose: testar semântica e ações expostas

## Em uma frase
Localize nós de Compose pela semântica que a UI expõe e valide ações e estados observáveis, não a estrutura interna de composição.

## Por que importa
Testes por semântica acompanham o uso e acessibilidade; acoplamento a hierarquia interna pode quebrar sem alteração de comportamento.

## Como funciona
Use APIs de teste Compose para localizar por texto ou propriedade semântica, executar ação e verificar estado final. Crie tags apenas quando semântica natural for insuficiente.

## Exemplo
Toque no controle nomeado Favoritar e verifique que sua descrição de estado mudou; a assertion não precisa conhecer nome da função composable.

## Limites e trade-offs
Testes Compose não substituem cobertura de serviços, navegação de sistema ou comportamento completo em hardware; semantics customizadas devem ser deliberadas.

## Como verificar
Confira o merged semantics tree, valide o estado antes e depois e execute o fluxo em integração se depender de plataforma fora do composable.

## Conexões
- [[android-compose-clock-idle-animacoes]] — Veja também: Android Compose: controlar clock e animações em testes.
- [[android-process-death-restauracao-estado]] — Veja também: Android: testar restauração após recriação do processo.

## Fontes
- [Android — Compose testing](https://developer.android.com/develop/ui/compose/testing) — semântica, ações e assertions de UI Compose; consultado em 2026-10-02.
- [Android — Fundamentals of testing](https://developer.android.com/training/testing/fundamentals) — escopo, ambiente e tipos de teste Android; consultado em 2026-10-02.
