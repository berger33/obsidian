---
id: software.criacao_ia.tranche02.000128
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

# Engenharia de Contexto: usar testes unitários como especificação

## Em uma frase
Fornecer testes unitários existentes como especificação orienta a IA a produzir implementações corretas por construção.

## Por que importa
Descrições verbais podem conter ambiguidades, enquanto casos de teste com asserções definem formalmente as entradas, saídas e limites esperados.

## Como funciona
Inclua o arquivo de teste correspondente ao solicitar a implementação de uma função, instruindo o modelo a garantir que todas as asserções sejam satisfeitas.

## Exemplo
```markdown
@src/utils/calculator.test.ts
Implemente a funcao calculateTax() em src/utils/calculator.ts
de modo que satisfaca integralmente todos os cenarios de teste anexados.
```

## Limites e trade-offs
Se os testes forem incompletos ou contiverem asserções falhas, o modelo produzirá uma implementação enviesada pelos erros do próprio teste.

## Como verificar
Execute a suíte de testes após a geração do código e confirme a aprovação de 100% dos cenários especificados.

## Conexões
- [[cursor-revisar-diffs-inline-com-rejeicao-parcial]] — Veja também: Cursor: revisar diffs inline com rejeição granular.
- [[context-engineering-injetar-tipos-estaticos-e-interfaces]] — Veja também: Engenharia de Contexto: injetar tipos estáticos para evitar alucinações.
- [[copilot-gerar-testes-a-partir-de-comportamento]] — Conexão temática direta com copilot-gerar-testes-a-partir-de-comportamento.
- [[claude-code-validar-testes-antes-do-commit]] — Conexão temática direta com claude-code-validar-testes-antes-do-commit.
- [[qa-jogos-isolar-cenarios-de-regressao-de-gameplay]] — Conexão temática direta com qa-jogos-isolar-cenarios-de-regressao-de-gameplay.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
