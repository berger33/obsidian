---
id: software.testes.tranche08.000189
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
fontes: ["https://docs.flutter.dev/testing/testing-plugins", "https://docs.flutter.dev/testing/integration-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Flutter: separar contrato simulado de regressão em dispositivo

## Em uma frase
Mantenha testes rápidos com dependências controladas e poucos cenários em dispositivo para detectar divergência de plugin e plataforma.

## Por que importa
O mock acelera combinações de erro e borda; dispositivo valida a integração real onde channel, lifecycle ou código nativo participa.

## Como funciona
Defina contrato da dependência, cubra cenários Dart com fake ou mock e escolha integração focada em comportamento que o mock não executa.

## Exemplo
Falhas de permissão são cobertas em widget tests pelo fake; um caso em emulador confirma que plugin real retorna estado coerente.

## Limites e trade-offs
Um caso em emulador não cobre todas as versões e fabricantes; mocks podem continuar corretos mesmo após mudança nativa incompatível.

## Como verificar
Associe cada teste à camada declarada, execute matriz mínima de plataforma suportada e compare valores retornados com o contrato do plugin.

## Conexões
- [[flutter-plugin-channel-mock-fronteira]] — Veja também: Flutter: mockar canais de plugin sem alegar teste nativo.
- [[flutter-integration-dispositivo-fluxo]] — Veja também: Flutter: desenhar testes de integração em dispositivo.

## Fontes
- [Flutter — Testing plugins](https://docs.flutter.dev/testing/testing-plugins) — limites entre Dart, canais de plataforma e código nativo; consultado em 2026-10-02.
- [Flutter — Integration tests](https://docs.flutter.dev/testing/integration-tests) — execução em dispositivo/emulador e validação de fluxos; consultado em 2026-10-02.
