---
id: software.criacao_ia.tranche02.000129
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

# Engenharia de Contexto: injetar tipos estáticos para evitar alucinações

## Em uma frase
Apresentar definições de tipos estáticos e interfaces restringe o espaço de busca do modelo e previne o uso de APIs inexistentes.

## Por que importa
Modelos generativos tendem a inventar métodos plausíveis quando não recebem contratos estritos das bibliotecas utilizadas.

## Como funciona
Injete contratos de interface TypeScript, Rust traits ou classes abstratas C# no prompt para guiar a implementação dos métodos concretos.

## Exemplo
```typescript
// Interface contratual fornecida no prompt de contexto
export interface IQuestReward {
  experience: number;
  items: Array<{ id: string; quantity: number }>;
  grantBonus(multiplier: number): void;
}
```

## Limites e trade-offs
Contratos desatualizados em relação à versão real da biblioteca geram erros de tipo no momento da compilação do projeto.

## Como verificar
Compile o projeto após a geração para assegurar que nenhum método não declarado na interface foi utilizado.

## Conexões
- [[context-engineering-usar-testes-como-especificacao]] — Veja também: Engenharia de Contexto: usar testes unitários como especificação.
- [[cursor-corrigir-erros-com-diagnosticos-do-compilador]] — Veja também: Cursor: corrigir erros alimentando diagnósticos do compilador.
- [[saida-estruturada-usar-json-schema-estrito]] — Conexão temática direta com saida-estruturada-usar-json-schema-estrito.
- [[function-calling-declarar-contrato-de-ferramenta]] — Conexão temática direta com function-calling-declarar-contrato-de-ferramenta.
- [[cursor-padronizar-regras-com-cursorrules]] — Conexão temática direta com cursor-padronizar-regras-com-cursorrules.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
