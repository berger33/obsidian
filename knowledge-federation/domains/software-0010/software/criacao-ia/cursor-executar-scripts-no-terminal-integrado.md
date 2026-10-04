---
id: software.criacao_ia.tranche02.000125
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

# Cursor: executar scripts no terminal integrado com supervisão

## Em uma frase
A execução supervisionada de comandos de terminal pelo assistente agiliza tarefas de compilação, instalação de pacotes e migrações.

## Por que importa
Permitir que a IA execute verificações diretamente no terminal reduz o atrito de alternância de janelas e acelera ciclos de feedback.

## Como funciona
Solicite no chat a execução de comandos como `npm test` ou `cargo check`. O assistente monta o comando e solicita confirmação visual no terminal antes de iniciar o processo, capturando a saída para depuração.

## Exemplo
```bash
# Comando sugerido pela IA aguardando clique de confirmacao
npm run test:unit -- src/auth.test.ts
[Accept and Run] [Cancel]
```

## Limites e trade-offs
Executar scripts sem inspecionar os argumentos pode introduzir comandos destrutivos ou instalações de dependências incorretas.

## Como verificar
Solicite a execução de um script de teste e verifique se o assistente exibe a caixa de confirmação antes de rodar o processo no shell.

## Conexões
- [[cursor-composer-coordenar-edicoes-multi-arquivo]] — Veja também: Cursor Composer: coordenar edições multi-arquivo com checkpoint.
- [[cursor-priorizar-janela-de-contexto-essencial]] — Veja também: Cursor: priorizar arquivos essenciais na janela de contexto.
- [[claude-code-gerenciar-permissoes-de-execucao-de-comandos]] — Conexão temática direta com claude-code-gerenciar-permissoes-de-execucao-de-comandos.
- [[cursor-corrigir-erros-com-diagnosticos-do-compilador]] — Conexão temática direta com cursor-corrigir-erros-com-diagnosticos-do-compilador.
- [[qa-jogos-executar-playtests-headless-em-ci]] — Conexão temática direta com qa-jogos-executar-playtests-headless-em-ci.

## Fontes
- [Cursor Documentation — Rules for AI](https://docs.cursor.com/context/rules-for-ai) — Guia oficial de configuração de regras persistentes de projeto (.cursorrules) e system prompts. Consulta: 2026-10-04.
- [Cursor Documentation — Codebase Indexing & Context](https://docs.cursor.com/context/@-symbols/@-codebase) — Documentação sobre indexação vetorial, símbolos @codebase, @docs, @git e gerenciamento de contexto. Consulta: 2026-10-04.
