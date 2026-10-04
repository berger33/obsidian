---
id: software.criacao_ia.tranche02.000122
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

# Cursor: otimizar indexação vetorial com .cursorignore

## Em uma frase
O arquivo .cursorignore exclui arquivos binários, builds e dependências volumosas do índice de busca semântica do repositório.

## Por que importa
Indexar diretórios de cache ou bibliotecas de terceiros satura o índice vetorial com código irrelevante e degrada a precisão do contexto.

## Como funciona
Crie um arquivo `.cursorignore` listando pastas como `dist/`, `build/`, `node_modules/` e arquivos de dados pesados (`.sqlite`, `.csv`). O sistema de indexação do Cursor ignora esses caminhos ao gerar embeddings.

## Exemplo
```gitignore
# Arquivo .cursorignore para otimizacao do indice
node_modules/
dist/
coverage/
*.sqlite
*.log
```

## Limites e trade-offs
Ignorar diretórios essenciais por engano impede que o assistente localize definições e tipos legítimos do projeto.

## Como verificar
Verifique o status de indexação do repositório na tela de configurações do Cursor e confirme que apenas arquivos de código-fonte válidos foram processados.

## Conexões
- [[cursor-padronizar-regras-com-cursorrules]] — Veja também: Cursor: padronizar convenções no arquivo .cursorrules.
- [[cursor-usar-simbolos-de-contexto-docs-e-git]] — Veja também: Cursor: usar símbolos de contexto @Docs e @Git.
- [[continue-dev-indexar-codebase-com-embeddings-locais]] — Conexão temática direta com continue-dev-indexar-codebase-com-embeddings-locais.
- [[cursor-priorizar-janela-de-contexto-essencial]] — Conexão temática direta com cursor-priorizar-janela-de-contexto-essencial.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
