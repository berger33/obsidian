---
id: software.testes.tranche10.000408
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://github.com/docker-library/official-images/blob/f5a08cb993309e539ddddf5b23236d4442fb95a1/library/postgres", "https://java.testcontainers.org/modules/databases/jdbc/", "https://java.testcontainers.org/features/advanced_options/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testcontainers: fixar imagem com tag específica e digest quando necessário

## Em uma frase
Uma tag específica reduz mudanças inesperadas da imagem, enquanto um digest pode identificar exatamente o artefato resolvido.

## Por que importa
Testcontainers aproxima testes de integração de serviços reais, mas containers iniciados não significam necessariamente que o serviço já esteja pronto. Uma tag flutuante pode mudar sem alteração no repositório e produzir resultados divergentes entre execuções.

## Como funciona
Declare imagem e lifecycle, aguarde um sinal de readiness adequado ao protocolo e isole recursos mutáveis entre casos e workers. Use uma tag de versão e distribuição validada; se a política exigir identidade imutável, registre também o digest resolvido e altere a referência por mudança revisada.

## Exemplo
O índice oficial consultado no commit de 2026-09-24 lista postgres:16.15-bookworm; a suíte pode usar essa tag e registrar o digest efetivamente resolvido após validar migrations e consultas.

## Limites e trade-offs
Integração com Docker, custo de recursos, versão de imagem e comportamento do framework influenciam a reprodutibilidade e a duração da suíte. Mesmo uma tag patch/distro é um nome mutável; digest fixa o manifesto selecionado, mas arquitetura, engine, configuração e inicialização ainda afetam o ambiente.

## Como verificar
Confirme a tag no índice oficial, registre a imagem e o digest resolvido e execute em ambiente limpo para conferir plataforma e inicialização.

## Conexões
- [[testcontainers-compose-espera-servico-especifico]] — Veja também: Testcontainers Compose: esperar pelo serviço que o cliente usa.
- [[testcontainers-startup-parallel-independencia-recursos]] — Veja também: Testcontainers: paralelizar startup somente para serviços independentes.

## Fontes
- [Docker Official Images — PostgreSQL tags (commit f5a08cb, 2026-09-24)](https://github.com/docker-library/official-images/blob/f5a08cb993309e539ddddf5b23236d4442fb95a1/library/postgres) — tags e variantes de distribuição publicadas para a imagem oficial, incluindo postgres:16.15-bookworm no snapshot consultado; consultado em 2026-10-02.
- [Testcontainers for Java — JDBC support](https://java.testcontainers.org/modules/databases/jdbc/) — driver JDBC, URLs jdbc:tc e configuração de bancos temporários; consultado em 2026-10-02.
- [Testcontainers for Java — Advanced options](https://java.testcontainers.org/features/advanced_options/) — opções de inicialização e limites de recursos dos containers; consultado em 2026-10-02.
