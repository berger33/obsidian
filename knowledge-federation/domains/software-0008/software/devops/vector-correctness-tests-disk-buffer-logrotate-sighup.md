---
id: software.devops.tranche02.000186
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/vectordotdev/vector/master/README.md", "https://github.com/vectordotdev/vector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Testes de corretude: persistência de buffer em disco, rotação de arquivos, truncamento, SIGHUP e JSON

## Em uma frase
A subseção `Correctness` em `Comparisons` do README destaca seis testes fundamentais de qualidade e atenção aos detalhes do `vector-test-harness` nos quais o Vector é aprovado (`✓`) em todos: **Disk Buffer Persistence** (`disk_buffer_persistence_correctness`), **File Rotate (create)** (`file_rotate_create_correctness`), **File Rotate (copytruncate)** (`file_rotate_truncate_correctness`), **File Truncation** (`file_truncate_correctness`), **Process (SIGHUP)** (`sighup_correctness`) e **JSON (wrapped)** (`wrapped_json_correctness`).

## Por que importa
Em produção, perda ou corrupção silenciosa de logs quase sempre ocorre em situações de borda: quando o `logrotate` aplica `copytruncate`, quando um arquivo é truncado, quando o processo recebe `SIGHUP` para recarregar a configuração ou quando o nó reinicia com eventos pendentes no buffer em disco.

## Como funciona
Habilite buffers persistentes em disco (`Disk Buffer Persistence`) nos sinks críticos do Vector, utilize `SIGHUP` para recarregar configurações sem perder conexões ativas e verifique como os arquivos de log são rotacionados (`create` vs `copytruncate`) nos hosts.

## Exemplo
Uma aplicação legada usa `logrotate` com `copytruncate`; o agente Vector detecta o truncamento corretamente e continua lendo os novos eventos sem perder linhas nem reler lixo binário.

## Limites e trade-offs
Buffers em disco exigem armazenamento persistente montado no pod ou diretório do host; se o diretório do buffer estiver em um `emptyDir` volátil e o pod for removido do nó, os dados ainda não enviados serão perdidos.

## Como verificar
Conferi a subseção Correctness em Comparisons no README oficial de `vectordotdev/vector`.

## Conexões
- [[vector-performance-benchmarks-test-harness]] — Veja também: Benchmarks de performance no vector-test-harness: TCP, File e HTTP.
- [[vector-sources-transforms-sinks-pipeline-model]] — Veja também: Modelo declarativo do pipeline: coleta em sources, processamento em transforms e entrega em sinks.

## Fontes
- [Vector — GitHub README](https://raw.githubusercontent.com/vectordotdev/vector/master/README.md) — Visão geral do Vector (pipeline de observabilidade em Rust para agent e aggregator), princípios, 5 casos de uso, escala na comunidade (500 TB/dia) e tabelas de performance e corretude.; consultado em 2026-10-03.
- [Vector — Repositório Oficial no GitHub](https://github.com/vectordotdev/vector) — Repositório oficial do Vector em Rust com código-fonte, workflows de integração e links de políticas.; consultado em 2026-10-03.
