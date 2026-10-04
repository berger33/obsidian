---
id: software.criacao_ia.tranche02.000121
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

# Cursor: padronizar convenções no arquivo .cursorrules

## Em uma frase
O arquivo .cursorrules na raiz do projeto orienta a IA com instruções contextuais persistentes sobre a arquitetura do código.

## Por que importa
Manter diretrizes arquiteturais claras no repositório evita que o modelo sugira padrões legados ou estruturas de pastas inadequadas.

## Como funciona
Insira um arquivo `.cursorrules` contendo restrições de tipagem, preferências de bibliotecas e padrões de componentes. O editor carrega automaticamente essas instruções ao montar os prompts do chat e do inline edit.

## Exemplo
```markdown
# Regras do Projeto no .cursorrules
- Preferir funcoes utilitarias puras a classes de servico anemicas.
- Para manipulacao de datas, utilizar exclusivamente a biblioteca date-fns.
- Toda nova rota de API deve conter validacao de payload com schemas Zod.
```

## Limites e trade-offs
Regras prolixas ou genéricas reduzem a eficácia do assistente e podem gerar comportamentos contraditórios com o código existente.

## Como verificar
Abra o chat do Cursor, solicite a criação de um novo componente e avalie se as convenções declaradas no `.cursorrules` foram estritamente respeitadas.

## Conexões
- [[cursor-otimizar-indexacao-com-cursorignore]] — Veja também: Cursor: otimizar indexação vetorial com .cursorignore.
- [[continue-dev-padronizar-regras-de-projeto]] — Conexão temática direta com continue-dev-padronizar-regras-de-projeto.
- [[claude-code-definir-instrucoes-claudemd]] — Conexão temática direta com claude-code-definir-instrucoes-claudemd.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
