---
id: software.testes.tranche14.000799
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://developer.android.com/training/testing/espresso/web", "https://developer.android.com/training/testing/espresso"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso-Web: testar WebView dentro de fluxo híbrido

## Em uma frase
Espresso-Web é apropriado para exercitar o WebView como parte de uma aplicação híbrida e pode ser combinado a operações Espresso em views nativas.

## Por que importa
A fronteira nativo-web pode ser o próprio requisito; testar apenas o site em browser comum deixa de cobrir a integração com o app Android.

## Como funciona
Use API WebInteraction para localizar elemento e executar ação via WebDriver atoms, coordenando o passo com controles nativos quando necessário.

## Exemplo
Um teste pode preencher um formulário dentro do WebView, submeter e depois confirmar o resultado numa toolbar nativa.

## Limites e trade-offs
Para um site sem interação com controles Android, um framework web dedicado pode rodar mais rápido e sem dispositivo ou JVM.

## Como verificar
Confirme qual parte depende de integração nativa e mantenha testes WebView separados dos testes web independentes quando a cobertura diferir.

## Conexões
- [[espresso-suppress-accessibility-narrowly]] — Veja também: Espresso: restringir supressões de findings de acessibilidade.

## Fontes
- [Android — Espresso Web](https://developer.android.com/training/testing/espresso/web) — WebView em aplicações híbridas, WebInteraction e integração com UI nativa; consultado em 2026-10-02.
- [Android — Espresso](https://developer.android.com/training/testing/espresso) — ações de UI, assertions, sincronização automática e pacotes do Espresso; consultado em 2026-10-02.
