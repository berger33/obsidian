---
id: software.testes.tranche23.001661
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/karma-runner/karma/blob/master/README.md", "https://blog.angular.io/moving-angular-cli-to-jest-and-web-test-runner-ef85ef69ceca"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karma está descontinuado: só correções de segurança

## Em uma frase
O anúncio no topo do README oficial é direto: "Karma is deprecated and is not accepting new features or general bug fixes"; correções críticas de segurança continuam até 12 meses depois de o suporte a Web Test Runner do Angular CLI ser marcado como estável.

## Por que importa
Ignorar esse status leva a iniciar projetos novos sobre uma base que não evolui; a nota serve para que a escolha de um runner em 2026 parta de quem sabe que o Karma entrou em contagem regressiva.

## Como funciona
O time recomenda caminhos de migração: o ecossistema Angular adiciona suporte a Jest e Web Test Runner; fora dele, Web Test Runner e jasmine-browser-runner são alternativas baseadas em navegador, e Jest e Vitest são alternativas Node.

## Exemplo
Antes de adicionar o Karma a um projeto novo, leia o aviso no README e avalie jasmine-browser-runner (navegador) ou Vitest (Node); projetos legados com Karma continuam utilizáveis enquanto recebem patches de segurança.

## Limites e trade-offs
O aviso é a posição do mantenedor, não uma data-limite rígida: correções de segurança continuam "as necessary", e nenhum cronograma público de encerramento total acompanha o texto.

## Como verificar
Abra o README do repositório karma-runner/karma e confirme o bloco de deprecação, o prazo vinculado ao Angular CLI e a lista de ferramentas sugeridas para migração.

## Conexões
- [[karma-what-it-is]] — Veja também: Karma: um executor de JavaScript em navegadores reais.
- [[karma-not-a-framework]] — Veja também: Karma não é framework de teste nem biblioteca de asserção.

## Fontes
- [Karma — README oficial](https://github.com/karma-runner/karma/blob/master/README.md) — proposta, descontinuação, adaptadores e quando usar; consultado em 2026-10-03.
- [Angular Blog — Moving Angular CLI to Jest and Web Test Runner](https://blog.angular.io/moving-angular-cli-to-jest-and-web-test-runner-ef85ef69ceca) — anúncio de migração linkado pelo README do Karma; consultado em 2026-10-03.
