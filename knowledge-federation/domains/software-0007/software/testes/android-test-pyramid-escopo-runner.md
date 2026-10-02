---
id: software.testes.tranche08.000170
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
fontes: ["https://developer.android.com/training/testing/fundamentals", "https://developer.android.com/training/testing/other-components/ui-automator"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android: escolher escopo e runner de teste

## Em uma frase
Escolha teste local, instrumentado ou UI conforme a fronteira que precisa ser validada, evitando usar uma camada cara para toda regra.

## Por que importa
Testes locais tendem a ser rápidos; instrumentação inclui plataforma real ou emulada e é indicada quando comportamento Android participa do contrato.

## Como funciona
Separe lógica pura, integração com framework e fluxos de interface. Registre o que o runner executa e quais dependências reais ou substituídas entram em cada camada.

## Exemplo
Uma regra de cálculo fica em teste local; persistência Android usa teste instrumentado; permissão do sistema e fluxo de tela usa automação apropriada.

## Limites e trade-offs
A classificação não é uma pirâmide rígida: requisitos de plataforma, custo de emulador e risco do produto alteram a mistura ideal.

## Como verificar
Compare duração e defeitos encontrados por camada. Confirme que teste local não pretende verificar APIs reais e que o instrumentado cobre as fronteiras delegadas.

## Conexões
- [[android-separar-teste-ui-de-regra]] — Veja também: Android: não concentrar regras de negócio em teste de UI.
- [[android-uiautomator-fronteira-sistema]] — Veja também: Android: UI Automator para fronteiras de sistema.

## Fontes
- [Android — Fundamentals of testing](https://developer.android.com/training/testing/fundamentals) — escopo, ambiente e tipos de teste Android; consultado em 2026-10-02.
- [Android — UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) — interação com aplicativos e interface do sistema; consultado em 2026-10-02.
