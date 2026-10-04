---
id: software.testes.tranche24.001848
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/google/fuzzbench/master/README.md", "https://google.github.io/fuzzbench/getting-started/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Documentação e canais do projeto

## Em uma frase
O README encerra os canais: documentação detalhada no site google.github.io/fuzzbench ("Read our detailed documentation to learn how to use FuzzBench"), discussão e anúncios na mailing list fuzzbench-users (Google Groups), e contato privado no fuzzbench@google.com — três portas declaradas, da consulta técnica ao contato direto.

## Por que importa
Para serviço de infraestrutura acadêmica, a separação lista pública/email privado define o protocolo de uso: dúvidas operacionais e announcements têm arquivo público, casos sensíveis (submissões com dados não publicados) têm canal direto — sem isso, tudo vira ruído em issue tracker.

## Como funciona
Comece pelo site de documentação para uso; mailing list para acompanhamento de mudanças do serviço; o email é o caminho que o próprio README nomeia para o que é "private".

## Exemplo
O padrão declarado no fim do README: getting-started, documentação, lista, email — a nota registra a topologia de suporte como o projeto a oferece.

## Limites e trade-offs
O README funciona como índice desses destinos; seu conteúdo (URLs e nomes) pode mudar sem afetar a capacidade descrita aqui.

## Como verificar
As seções Documentation e Contacts do README oficial definem a nota.

## Conexões
- [[fuzzbench-periodic-reports]] — Veja também: Relatórios públicos e recorrentes.
- [[fuzzbench-feedback-loop]] — Veja também: O convite de feedback e o escopo de melhoria contínua.

## Fontes
- [FuzzBench — README oficial](https://raw.githubusercontent.com/google/fuzzbench/master/README.md) — README oficial do FuzzBench com definição do serviço gratuito, API de integração, benchmarks OSS-Fuzz, biblioteca de reporting e escala do sample report.; consultado em 2026-10-03.
- [FuzzBench — Getting Started (documentação oficial)](https://google.github.io/fuzzbench/getting-started/) — Guia oficial Getting Started do FuzzBench para integração de fuzzers e execução de experimentos.; consultado em 2026-10-03.
