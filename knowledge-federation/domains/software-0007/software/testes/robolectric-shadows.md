---
id: software.testes.tranche20.001441
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://robolectric.org/configuring/", "https://robolectric.org/extending/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robolectric: substituir serviços com sombras

## Em uma frase
Sombras são implementações próprias que substituem classes do sistema, com métodos que devolvem valores controlados e registram o efeito das chamadas.

## Por que importa
As sombras permitem verificar interações com o sistema, como intenções disparadas e mensagens exibidas, sem aparelho real.

## Como funciona
Use sombras embutidas quando existirem, crie sombra própria apenas para serviço não coberto e declare-a na configuração do teste.

## Exemplo
A sombra da tela pode registrar a última mensagem exibida e a intenção disparada ao tocar no botão.

## Limites e trade-offs
Sombras próprias duplicam comportamento que já existe na biblioteca, e registros excessivos nas sombras viram dependência interna difícil de manter.

## Como verificar
Remova a sombra declarada e confirme que o caso deixa de encontrar o registro correspondente.

## Conexões
- [[robolectric-sdk-configuration]] — Veja também: Robolectric: escolher a versão de sistema.
- [[robolectric-activity-lifecycle]] — Veja também: Robolectric: controlar o ciclo de vida de telas.

## Fontes
- [Robolectric — Configuração](https://robolectric.org/configuring/) — versão de sistema, sombras, propriedades e repositórios; consultado em 2026-10-03.
- [Robolectric — Sombras](https://robolectric.org/extending/) — implementação de sombras, anotações e acesso ao objeto real; consultado em 2026-10-03.
