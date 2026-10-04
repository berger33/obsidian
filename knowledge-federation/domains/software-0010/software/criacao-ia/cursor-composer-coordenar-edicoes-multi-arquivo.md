---
id: software.criacao_ia.tranche02.000124
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

# Cursor Composer: coordenar edições multi-arquivo com checkpoint

## Em uma frase
O Composer do Cursor aplica modificações coordenadas em múltiplos arquivos simultaneamente a partir de um único plano de ação.

## Por que importa
Refatorações em grande escala, como alterações de assinaturas de métodos e migrações de esquemas, exigem consistência entre diferentes camadas do software.

## Como funciona
Abra o painel Composer (Ctrl+I ou Cmd+I), descreva a alteração arquitetural e vincule os módulos afetados. O Composer gera diffs paralelos nos arquivos envolvidos, permitindo revisão individual antes da confirmação.

## Exemplo
```markdown
<!-- Prompt no Composer -->
Refatore o servico de inventario em src/inventory/:
1. Crie a interface IInventoryItem em types.ts
2. Atualize o controller InventoryController.ts
3. Ajuste os testes unitarios correspondentes em tests/inventory.test.ts
```

## Limites e trade-offs
Modificações simultâneas em muitos arquivos podem gerar inconsistências de tipagem se o modelo não mantiver a coesão das interfaces.

## Como verificar
Revise os diffs apresentados em cada aba pelo Composer antes de clicar em `Accept All` e execute a suíte de testes do projeto.

## Conexões
- [[cursor-usar-simbolos-de-contexto-docs-e-git]] — Veja também: Cursor: usar símbolos de contexto @Docs e @Git.
- [[cursor-executar-scripts-no-terminal-integrado]] — Veja também: Cursor: executar scripts no terminal integrado com supervisão.
- [[claude-code-orquestrar-subagentes-especializados]] — Conexão temática direta com claude-code-orquestrar-subagentes-especializados.
- [[cursor-revisar-diffs-inline-com-rejeicao-parcial]] — Conexão temática direta com cursor-revisar-diffs-inline-com-rejeicao-parcial.
- [[cursor-corrigir-erros-com-diagnosticos-do-compilador]] — Conexão temática direta com cursor-corrigir-erros-com-diagnosticos-do-compilador.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
