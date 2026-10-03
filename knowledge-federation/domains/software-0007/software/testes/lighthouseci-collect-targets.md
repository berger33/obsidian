---
id: software.testes.tranche16.001014
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://googlechrome.github.io/lighthouse-ci/docs/configuration.html", "https://github.com/GoogleChrome/lighthouse-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Lighthouse CI: definir páginas e servidor de coleta

## Em uma frase
A coleta recebe uma lista de endereços, um diretório estático ou um comando que sobe o servidor, com padrão e prazo para considerar o serviço pronto.

## Por que importa
Medir a aplicação certa exige que a página esteja servida de forma reproduzível, e não dependente de terminal aberto por acaso.

## Como funciona
Liste as páginas mais representativas, prefira artefato estático quando existir e use comando de servidor com padrão de prontidão e prazo explícitos.

## Exemplo
Um conjunto inicial pode cobrir a página inicial, a listagem e a página de detalhe, evitando medir rotas irrelevantes para a experiência.

## Limites e trade-offs
Listas extensas aumentam muito o tempo do pipeline, e o padrão de prontidão errado faz a coleta começar antes de o serviço responder.

## Como verificar
Rode a coleta com a lista completa e confirme que cada endereço declarado aparece no diretório de resultados.

## Conexões
- [[lighthouseci-autorun-steps]] — Veja também: Lighthouse CI: entender o fluxo automático.
- [[lighthouseci-number-of-runs]] — Veja também: Lighthouse CI: reduzir variação com repetições.

## Fontes
- [Lighthouse CI — Configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) — seções collect, assert e upload, presets, asserções e orçamentos; consultado em 2026-10-03.
- [Lighthouse CI — repositório oficial](https://github.com/GoogleChrome/lighthouse-ci) — comandos, integração contínua e documentação do projeto; consultado em 2026-10-03.
