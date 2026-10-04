---
id: software.testes.tranche08.000184
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
fontes: ["https://docs.flutter.dev/cookbook/testing/widget/orientation", "https://docs.flutter.dev/cookbook/testing/widget/introduction"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Flutter: validar orientação retrato e paisagem

## Em uma frase
Inclua orientação apenas quando suportada pelo produto e verifique adaptação do layout em vez de exigir pixels idênticos.

## Por que importa
Mudança de orientação altera espaço disponível e pode revelar conteúdo inacessível, overflow ou estado de tela descartado.

## Como funciona
Configure o binding e tamanho de tela para cada orientação, construa o widget e verifique elementos críticos e continuidade do estado relevante.

## Exemplo
Um formulário conserva valores em retrato e paisagem, enquanto a ação primária continua alcançável por rolagem no espaço menor.

## Limites e trade-offs
Widget test não reproduz integralmente sensor, lifecycle e transição física do dispositivo; use integração se esses efeitos forem parte do requisito.

## Como verificar
Execute ambos os tamanhos, inspecione overflow e confirme que navegação ou campos não desaparecem após a mudança.

## Conexões
- [[flutter-widget-erro-overflow-responsivo]] — Veja também: Flutter: detectar overflow e conteúdo inacessível em widget tests.
- [[android-multiplas-telas-configuracao]] — Veja também: Android: cobrir tamanhos de tela e configuração.

## Fontes
- [Flutter — Test orientation](https://docs.flutter.dev/cookbook/testing/widget/orientation) — cenários de retrato e paisagem em widget tests; consultado em 2026-10-02.
- [Flutter — Widget testing](https://docs.flutter.dev/cookbook/testing/widget/introduction) — testWidgets, pump, finders e matchers; consultado em 2026-10-02.
