---
id: software.testes.tranche08.000186
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
fontes: ["https://docs.flutter.dev/cookbook/testing/widget/finders", "https://docs.flutter.dev/cookbook/testing/widget/introduction"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Flutter: escolher Finder por semântica, texto ou chave

## Em uma frase
Escolha Finder que reflita o contrato do cenário e reserve Keys estáveis para elementos sem identificador visível adequado.

## Por que importa
Localização por posição na árvore interna acopla o teste à composição; texto ou semântica exercita melhor o que a interface expõe.

## Como funciona
Use texto e finders semânticos para elementos visíveis; quando repetição ou conteúdo dinâmico exigir, aplique ValueKey específica e única no widget relevante.

## Exemplo
Uma linha de pedido é encontrada pela chave do identificador e, dentro dela, o botão Remover é encontrado por texto acessível.

## Limites e trade-offs
Chave interna não prova que usuário consegue perceber o controle; texto também pode mudar por localização sem que a ação mude.

## Como verificar
Altere estrutura de widgets mantendo contrato e confirme estabilidade; verifique que chave duplicada ou elemento ausente faz o teste falhar claramente.

## Conexões
- [[flutter-widget-lista-rolagem-scrolluntilvisible]] — Veja também: Flutter: testar listas longas sem assumir posição fixa.
- [[rtl-consultas-prioridade-role-name]] — Veja também: Testing Library: priorizar consultas por papel e nome.

## Fontes
- [Flutter — Find widgets](https://docs.flutter.dev/cookbook/testing/widget/finders) — uso de Finder para localizar elementos no widget tree; consultado em 2026-10-02.
- [Flutter — Widget testing](https://docs.flutter.dev/cookbook/testing/widget/introduction) — testWidgets, pump, finders e matchers; consultado em 2026-10-02.
