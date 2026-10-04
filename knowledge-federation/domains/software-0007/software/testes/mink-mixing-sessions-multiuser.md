---
id: software.testes.tranche25.001874
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/minkphp/Mink/master/README.md", "https://github.com/minkphp/Mink"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Misturar sessões no mesmo teste para simular múltiplos usuários

## Em uma frase
O final do exemplo do README oficial ilustra o motivo de manter várias sessões registradas ("this all is done to make possible mixing sessions"): o código chama $mink->getSession('goutte1')->getPage()->findLink('Chat')->click() e logo na linha seguinte $mink->getSession('goutte2')->getPage()->findLink('Chat')->click().

## Por que importa
Testar interações multiusuário — como salas de chat, bloqueio concorrente de registros ou aprovação por dois perfis distintos — exige cookies e estados de navegação isolados; duas instâncias de Session no mesmo Mink têm estado completamente separado.

## Como funciona
Registre duas sessões nomeadas (por exemplo, 'goutte1' e 'goutte2' ou 'admin' e 'cliente'), autentique cada uma com credenciais diferentes e intercale ações chamando $mink->getSession('nome') em cada passo do cenário.

## Exemplo
No exemplo do README, goutte1 e goutte2 são instâncias separadas de Session(new GoutteDriver(new GoutteClient())), de modo que clicar em 'Chat' em goutte1 não compartilha sessão HTTP com goutte2.

## Limites e trade-offs
Se as duas sessões compartilharem a mesma instância subjacente de cliente ou driver em vez de instâncias distintas, o isolamento de cookies pode ser perdido; instancie um Driver/Client novo por Session como faz o exemplo oficial.

## Como verificar
Conferi as linhas finais do Usage Example no README oficial do Mink.

## Conexões
- [[mink-sessions-and-default-session]] — Veja também: Registro de múltiplas sessões e setDefaultSessionName.
- [[mink-visit-page-findlink-click]] — Veja também: Fluxo básico de navegação e interação: visit, getPage, findLink, click e getContent.

## Fontes
- [Mink — README oficial](https://raw.githubusercontent.com/minkphp/Mink/master/README.md) — README oficial do Mink com links úteis, exemplo de múltiplas sessões GoutteDriver e driver customizado, setDefaultSessionName, getSession e contribuidores.; consultado em 2026-10-03.
- [Repositório oficial minkphp/Mink](https://github.com/minkphp/Mink) — Repositório oficial do Mink no GitHub com classes Mink, Session, DocumentElement, DriverInterface e workflows de CI.; consultado em 2026-10-03.
