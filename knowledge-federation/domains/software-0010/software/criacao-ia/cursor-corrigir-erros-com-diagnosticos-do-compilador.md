---
id: software.criacao_ia.tranche02.000130
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

# Cursor: corrigir erros alimentando diagnósticos do compilador

## Em uma frase
Alimentar o modelo diretamente com as mensagens de erro do compilador ou linter acelera a correção de falhas de sintaxe e tipos.

## Por que importa
Descrever erros manualmente perde detalhes precisos como número de linha, código de erro e tipos esperados reportados pelo compilador.

## Como funciona
Copie a mensagem de erro emitida pelo compilador ou utilize o botão `Fix with AI` na lista de problemas do editor para que a IA analise o erro e o código adjacente.

## Exemplo
```bash
# Diagnostico do TypeScript alimentado no chat
src/auth.ts:42:15 - error TS2345: Argument of type 'string

## Limites e trade-offs
null' is not assignable to parameter of type 'string'.
> Corrija a condicao em src/auth.ts para tratar explicitamente o caso de valor nulo.
```

## Como verificar
Correções cegas de erros do linter podem mascarar bugs reais ao utilizar casts forçados (`as any`) em vez de checagens defensivas.

## Conexões
- [[context-engineering-injetar-tipos-estaticos-e-interfaces]] — Veja também: Engenharia de Contexto: injetar tipos estáticos para evitar alucinações.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
