---
id: software.testes.tranche08.000180
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
fontes: ["https://docs.flutter.dev/testing/overview", "https://docs.flutter.dev/testing/integration-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Flutter: distribuir testes entre unit, widget e integração

## Em uma frase
Selecione unit, widget ou integration test conforme a camada que precisa ser exercitada e o custo aceitável do feedback.

## Por que importa
Testes unitários são rápidos para lógica; widget tests cobrem composição e interação; integração exercita app em dispositivo ou emulador.

## Como funciona
Mapeie risco para camada: regra pura, árvore de widgets, ou comportamento de plataforma e fluxo completo. Evite duplicar toda combinação em integração sem benefício claro.

## Exemplo
A regra de desconto tem unit tests; o formulário tem widget test; login com plugin e navegação do app recebe cenário integrado em ambiente suportado.

## Limites e trade-offs
Nenhuma camada oferece sozinha toda a confiança. Um widget test não comprova código nativo de plugin e integração costuma ser mais lenta.

## Como verificar
Revise cada caso pelo defeito que pode detectar e execute suites separadamente para observar duração, estabilidade e cobertura das fronteiras.

## Conexões
- [[flutter-integration-dispositivo-fluxo]] — Veja também: Flutter: desenhar testes de integração em dispositivo.
- [[flutter-plugin-channel-mock-fronteira]] — Veja também: Flutter: mockar canais de plugin sem alegar teste nativo.

## Fontes
- [Flutter — Testing apps](https://docs.flutter.dev/testing/overview) — níveis unit, widget e integration com trade-offs; consultado em 2026-10-02.
- [Flutter — Integration tests](https://docs.flutter.dev/testing/integration-tests) — execução em dispositivo/emulador e validação de fluxos; consultado em 2026-10-02.
