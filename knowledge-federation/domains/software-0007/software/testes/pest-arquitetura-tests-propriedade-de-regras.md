---
id: software.testes.tranche15.000889
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pestphp.com/docs/arch-testing", "https://pestphp.com/docs/cli-api-reference"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: expressar regras arquiteturais como testes executáveis

## Em uma frase
Testes de arquitetura verificam propriedades estruturais sobre classes e namespaces, como dependências proibidas ou convenções de organização, em vez de observar uma única entrada e saída funcional.

## Por que importa
Uma regra automatizada transforma uma decisão de design em contrato verificável em revisões futuras; a página de arquitetura do Pest oferece a API para selecionar classes e encadear expectativas estruturais.

## Como funciona
A regra é mais valiosa quando tem escopo preciso e mensagem de falha compreensível.

## Exemplo
Defina um teste arquitetural que selecione classes do domínio e proíba referência a um namespace de infraestrutura; inclua exemplos permitidos e proibidos para validar a regra.

## Limites e trade-offs
Restrições excessivas podem bloquear refatorações legítimas e dependências permitidas por uma exceção real; arquitetura precisa de julgamento e não deve ser reduzida a uma lista arbitrária de regras.

## Como verificar
Introduza uma classe inválida no namespace de teste e confirme que o relatório identifica a violação, depois remova-a e rode a suíte completa para validar a regra no projeto.

## Conexões
- [[pest-browser-espera-timeout-e-flakiness]] — Veja também: Pest 5: calibrar o timeout e entender o auto-wait do Playwright.

## Fontes
- [Pest 5 — Architecture Testing](https://pestphp.com/docs/arch-testing) — expectativas de namespace, uso, tipo de classe e presets arquiteturais; consultado em 2026-10-02.
- [Pest 5 — CLI API Reference](https://pestphp.com/docs/cli-api-reference) — opções de seleção, execução, paralelismo, shards e reporters; consultado em 2026-10-02.
