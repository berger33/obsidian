---
id: software.criacao_ia.tranche02.000126
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

# Cursor: priorizar arquivos essenciais na janela de contexto

## Em uma frase
A seleção cuidadosa dos arquivos incluídos no contexto evita estouro da janela de atenção e preserva a precisão das respostas.

## Por que importa
Excesso de código irrelevante degrada a habilidade do modelo de focar em invariantes lógicos e regras de negócio específicas.

## Como funciona
Mantenha abertos apenas os arquivos diretamente relacionados à tarefa e feche abas secundárias antes de acionar a geração de código assistida.

## Exemplo
```markdown
<!-- Exemplo de prompt enxuto e focado -->
Apenas com base na interface exposta em src/contracts/IPayment.ts,
escreva a implementacao de PixPaymentGateway tratando timeout de conexao.
```

## Limites e trade-offs
Restringir excessivamente o contexto pode ocultar tipos utilitários ou dependências cruzadas necessárias para a compilação.

## Como verificar
Monitore o contador de tokens no rodapé da janela de chat e assegure que o prompt permaneça dentro dos limites eficientes do modelo.

## Conexões
- [[cursor-executar-scripts-no-terminal-integrado]] — Veja também: Cursor: executar scripts no terminal integrado com supervisão.
- [[cursor-revisar-diffs-inline-com-rejeicao-parcial]] — Veja também: Cursor: revisar diffs inline com rejeição granular.
- [[anthropic-api-controlar-limites-com-max-tokens]] — Conexão temática direta com anthropic-api-controlar-limites-com-max-tokens.
- [[cursor-otimizar-indexacao-com-cursorignore]] — Conexão temática direta com cursor-otimizar-indexacao-com-cursorignore.
- [[responses-api-limitar-o-tamanho-da-saida]] — Conexão temática direta com responses-api-limitar-o-tamanho-da-saida.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
