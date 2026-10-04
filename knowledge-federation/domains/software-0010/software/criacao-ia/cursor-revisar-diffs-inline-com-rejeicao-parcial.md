---
id: software.criacao_ia.tranche02.000127
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://docs.cursor.com/context/rules-for-ai", "https://docs.cursor.com/context/@-symbols/@-codebase"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Cursor: revisar diffs inline com rejeição granular

## Em uma frase
A inspeção de diffs inline com capacidade de rejeição linha a linha permite aceitar apenas sugestões seguras e validadas.

## Por que importa
Aceitar blocos inteiros de código gerado pode introduzir alterações não solicitadas ou deletar comentários e tratamentos de exceção.

## Como funciona
Durante a edição inline (Ctrl+K ou Cmd+K), utilize os botões de aceitação e rejeição granular para filtrar mudanças desejadas e descartar trechos indesejados.

## Exemplo
```diff
- function parsePayload(data: unknown): UserData {
+ function parsePayload(data: unknown): UserData { // [Accept]
-   return data as UserData;
+   if (!data

## Limites e trade-offs


## Como verificar
typeof data !== 'object') throw new Error('Invalid'); // [Accept]
+   // Removendo log de auditoria desnecessario (trecho rejeitado pelo dev) // [Reject]
```

## Conexões
- [[cursor-priorizar-janela-de-contexto-essencial]] — Veja também: Cursor: priorizar arquivos essenciais na janela de contexto.
- [[context-engineering-usar-testes-como-especificacao]] — Veja também: Engenharia de Contexto: usar testes unitários como especificação.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
