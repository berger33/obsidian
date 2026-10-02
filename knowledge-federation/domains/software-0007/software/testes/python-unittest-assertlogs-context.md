---
id: software.testes.tranche14.000849
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://docs.python.org/3/library/unittest.html", "https://docs.python.org/3/library/unittest.mock.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Python unittest: capturar logs do escopo da operação

## Em uma frase
`assertLogs()` captura registros de logging de um logger durante um bloco e permite verificar nível e conteúdo sem interceptar stdout.

## Por que importa
Logs podem constituir evidência operacional do contrato de erro e o helper evita depender da configuração global do console.

## Como funciona
Indique logger e nível mínimo, execute a operação no context manager e inspecione records ou saída capturada.

## Exemplo
Uma falha de integração confirma registro `WARNING` com identificador de correlação e mensagem sem imprimir credencial.

## Limites e trade-offs
Mensagem literal longa é instável e logs globais concorrentes podem fazer o teste capturar ruído de outro caso.

## Como verificar
Limite ao logger específico, use assertion sobre campos sem segredos e faça o teste sob configuração padrão da aplicação.

## Conexões
- [[python-isolated-asyncio-testcase-lifecycle]] — Veja também: Python unittest: isolar ciclo de vida de caso assíncrono.

## Fontes
- [Python 3.14 — unittest](https://docs.python.org/3/library/unittest.html) — TestCase, fixtures, subtests, suites, discovery, runners e logging; consultado em 2026-10-02.
- [Python 3.14 — unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — Mock, patch, autospec, spec_set, calls e escopo de substituições; consultado em 2026-10-02.
