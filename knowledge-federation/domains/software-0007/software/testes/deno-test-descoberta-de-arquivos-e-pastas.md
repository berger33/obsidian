---
id: software.testes.tranche15.000890
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
fontes: ["https://docs.deno.com/runtime/reference/cli/test/", "https://docs.deno.com/runtime/test/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Deno test: alinhar nome e localização às regras de descoberta

## Em uma frase
Sem caminhos explícitos, `deno test` procura módulos de teste usando convenções de nome e também reconhece scripts dentro de diretórios `__tests__`.

## Por que importa
A descoberta automática facilita suítes novas, mas uma convenção diferente pode fazer um arquivo ser ignorado sem erro aparente.

## Como funciona
A documentação lista extensões e padrões reconhecidos; uma configuração explícita de caminho reduz surpresa em projetos com layout próprio.

## Exemplo
Mantenha arquivos como `*_test.ts` ou `feature.test.ts` no local esperado e use `deno test path/to/file_test.ts` quando estiver investigando um único módulo.

## Limites e trade-offs
Arquivo encontrado não significa que toda definição nele será executada: filtros e marcas de skip/only ainda afetam o plano, e arquivos carregados por ferramenta externa seguem outro contrato.

## Como verificar
Execute `deno test` sem argumentos e confira a contagem de módulos no log; compare com inventário de testes do repositório para detectar convenções fora do padrão.

## Conexões
- [[deno-test-permissoes-minimas-por-teste]] — Veja também: Deno test: restringir permissões por teste sem ampliar a concessão da CLI.

## Fontes
- [Deno Runtime — deno test](https://docs.deno.com/runtime/reference/cli/test/) — flags de filtro, shard, cobertura, snapshots e execução do runner; consultado em 2026-10-02.
- [Deno Runtime — Testing](https://docs.deno.com/runtime/test/) — steps, timeouts, affected tests, permissões, snapshots, sanitizers e reporters; consultado em 2026-10-02.
