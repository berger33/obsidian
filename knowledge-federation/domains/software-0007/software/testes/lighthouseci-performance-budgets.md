---
id: software.testes.tranche16.001018
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

# Lighthouse CI: usar orçamento de desempenho

## Em uma frase
Um arquivo de orçamento declara limites de tamanho ou quantidade por tipo de recurso, e a auditoria correspondente pode ser verificada na esteira.

## Por que importa
Orçamento traduz a intenção em número revisável, tornando visível o custo de cada recurso adicionado à página.

## Como funciona
Declare o orçamento em arquivo próprio, aponte a configuração para ele e transforme a auditoria de orçamento em erro na verificação.

## Exemplo
Um limite de peso para imagens e scripts permite detectar aumento causado por biblioteca nova antes de a página chegar a produção.

## Limites e trade-offs
Orçamentos desatualizados bloqueiam mudanças legítimas, e limites por recurso não capturam custo de execução nem de requisições encadeadas.

## Como verificar
Compare o consumo atual com o orçamento declarado e ajuste o arquivo em discussão explícita, registrando a decisão.

## Conexões
- [[lighthouseci-numeric-assertions]] — Veja também: Lighthouse CI: definir limites numéricos e agregação.
- [[lighthouseci-upload-targets]] — Veja também: Lighthouse CI: escolher destino dos resultados.

## Fontes
- [Lighthouse CI — Configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) — seções collect, assert e upload, presets, asserções e orçamentos; consultado em 2026-10-03.
- [Lighthouse CI — repositório oficial](https://github.com/GoogleChrome/lighthouse-ci) — comandos, integração contínua e documentação do projeto; consultado em 2026-10-03.
