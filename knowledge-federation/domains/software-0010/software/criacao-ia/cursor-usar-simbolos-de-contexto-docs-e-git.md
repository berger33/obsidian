---
id: software.criacao_ia.tranche02.000123
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

# Cursor: usar símbolos de contexto @Docs e @Git

## Em uma frase
Os símbolos contextuais (@Docs, @Git, @Files) direcionam fontes de dados específicas para a janela de raciocínio da IA.

## Por que importa
Apontar manualmente os arquivos e a documentação reduz o custo de tokens e elimina a necessidade de adivinhações por parte do modelo.

## Como funciona
Digite `@` seguido do identificador do arquivo (`@src/auth.ts`), do histórico recente do Git (`@Git`) ou de uma documentação indexada (`@Docs`) no prompt do chat para vincular trechos exatos de informação.

## Exemplo
```markdown
@src/models/user.ts @src/controllers/auth.ts
Atualize a rota de registro para salvar o hash da senha utilizando a nova interface do modelo.
```

## Limites e trade-offs
Vincular um número excessivo de arquivos longos em um mesmo prompt pode esgotar o orçamento de contexto e degradar o raciocínio.

## Como verificar
Envie uma solicitação utilizando `@Files` apontando para dois módulos complementares e verifique se as edições propostas integram corretamente as dependências.

## Conexões
- [[cursor-otimizar-indexacao-com-cursorignore]] — Veja também: Cursor: otimizar indexação vetorial com .cursorignore.
- [[cursor-composer-coordenar-edicoes-multi-arquivo]] — Veja também: Cursor Composer: coordenar edições multi-arquivo com checkpoint.
- [[continue-dev-customizar-context-providers]] — Conexão temática direta com continue-dev-customizar-context-providers.
- [[cursor-priorizar-janela-de-contexto-essencial]] — Conexão temática direta com cursor-priorizar-janela-de-contexto-essencial.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
