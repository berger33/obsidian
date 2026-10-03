---
id: software.devops.tranche02.000185
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

# Benchmarks de performance no vector-test-harness: TCP, File e HTTP

## Em uma frase
A subseção `Performance` em `Comparisons` do README apresenta os testes de linha de base do repositório `vectordotdev/vector-test-harness` comparando Vector, Filebeat, FluentBit, FluentD, Logstash, SplunkUF e SplunkHF em cinco cenários: `TCP to Blackhole` (Vector em **86 mib/s** contra 64.4 mib/s do FluentBit e 40.6 mib/s do Logstash), `File to TCP` (Vector em **76.7 mib/s** contra 35 mib/s do FluentBit e 7.8 mib/s do Filebeat), `Regex Parsing` (Vector em 13.2 mib/s e FluentBit em **20.5 mib/s**), `TCP to HTTP` (Vector em **26.7 mib/s** contra 19.6 mib/s do FluentBit) e `TCP to TCP` (Vector em 69.9 mib/s e SplunkUF em **70.4 mib/s**).

## Por que importa
A própria tabela oficial do Vector é transparente ao mostrar tanto os cenários em que o Vector lidera (`TCP to Blackhole`, `File to TCP` e `TCP to HTTP`) quanto o cenário em que o Fluent Bit obteve maior taxa bruta (`Regex Parsing`), reforçando que o desempenho real depende do tipo de entrada, parsing e saída.

## Como funciona
Consulte os casos de teste em `vectordotdev/vector-test-harness` e execute benchmarks com o formato real dos seus logs e transformações antes de dimensionar a quantidade de CPU dos seus coletores.

## Exemplo
Para leitura intensiva de arquivos em disco e envio por HTTP (`File to TCP` / `TCP to HTTP`), a equipe dimensiona os recursos com base na alta vazão por núcleo do Vector, enquanto evita regexes desnecessárias quando o log já está em JSON estruturado.

## Limites e trade-offs
Benchmarks sintéticos servem como referência de linha de base; o throughput em produção varia conforme latência de rede do destino, compressão, TLS e complexidade das transformações.

## Como verificar
Conferi a subseção Performance em Comparisons no README oficial de `vectordotdev/vector`.

## Conexões
- [[vector-community-scale-500tb-daily-and-production-users]] — Veja também: Escala comprovada na comunidade: mais de 100 mil downloads diários e 500 TB/dia no maior usuário.
- [[vector-correctness-tests-disk-buffer-logrotate-sighup]] — Veja também: Testes de corretude: persistência de buffer em disco, rotação de arquivos, truncamento, SIGHUP e JSON.

## Fontes
- [Vector — GitHub README](https://raw.githubusercontent.com/vectordotdev/vector/master/README.md) — Visão geral do Vector (pipeline de observabilidade em Rust para agent e aggregator), princípios, 5 casos de uso, escala na comunidade (500 TB/dia) e tabelas de performance e corretude.; consultado em 2026-10-03.
- [Vector — Repositório Oficial no GitHub](https://github.com/vectordotdev/vector) — Repositório oficial do Vector em Rust com código-fonte, workflows de integração e links de políticas.; consultado em 2026-10-03.
