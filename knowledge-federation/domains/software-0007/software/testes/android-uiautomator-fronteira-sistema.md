---
id: software.testes.tranche08.000172
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

# Android: UI Automator para fronteiras de sistema

## Em uma frase
Use UI Automator quando o cenário atravessar o app e elementos de interface do dispositivo ou de outro aplicativo.

## Por que importa
Testes limitados à árvore da aplicação não cobrem diálogos de permissão, configurações do sistema ou alternância entre apps.

## Como funciona
Defina a fronteira externa explicitamente, localize elementos do sistema por propriedades estáveis e valide o retorno ao aplicativo após a interação necessária.

## Exemplo
O cenário aceita uma permissão de notificação na caixa do sistema, volta ao app e confirma que o fluxo continua com o estado concedido.

## Limites e trade-offs
UI do sistema pode variar por versão, fabricante, idioma e configuração; seletores visuais frágeis elevam manutenção e não substituem teste de regra.

## Como verificar
Execute nas versões Android de suporte, cubra recusa e concessão e confirme que o teste falha com estado inesperado em vez de avançar por coordenadas fixas.

## Conexões
- [[android-permissoes-recusa-revocacao]] — Veja também: Android: testar concessão, recusa e revogação de permissões.
- [[android-compose-semantics-assertions]] — Veja também: Android Compose: testar semântica e ações expostas.

## Fontes
- [Android — UI Automator](https://developer.android.com/training/testing/other-components/ui-automator) — interação com aplicativos e interface do sistema; consultado em 2026-10-02.
- [Android — Fundamentals of testing](https://developer.android.com/training/testing/fundamentals) — escopo, ambiente e tipos de teste Android; consultado em 2026-10-02.
