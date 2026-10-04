---
id: software.criacao_ia.tranche02.000102
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
fontes: ["https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview", "https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Claude Code: configurar instruções de projeto no arquivo CLAUDE.md

## Em uma frase
O arquivo CLAUDE.md padroniza comandos de build, testes e diretrizes de estilo para o assistente de linha de comando.

## Por que importa
Centralizar regras estáveis do repositório em um arquivo dedicado evita a repetição manual de contexto em cada prompt e reduz alterações fora dos padrões da equipe.

## Como funciona
Coloque um arquivo `CLAUDE.md` na raiz do repositório contendo comandos frequentes de compilação, execução de testes unitários e convenções de nomenclatura. O Claude Code lê este documento no início da sessão para alinhar suas ações às práticas do projeto.

## Exemplo
```markdown
# Diretrizes do Projeto para Claude Code

## Comandos de Build e Testes
- Build: `npm run build`
- Testes: `npm test -- --watchAll=false`
- Linter: `npm run lint`

## Convencoes de Codigo
- Utilizar TypeScript estrito e tipagem explicita em funcoes publicas.
- Manter funcoes utilitarias puras e cobertas por testes unitarios em tests/.
```

## Limites e trade-offs
Instruções ambíguas ou desatualizadas no `CLAUDE.md` podem levar o assistente a executar suítes de teste obsoletas ou aplicar estilos conflitantes.

## Como verificar
Crie o arquivo `CLAUDE.md` na raiz, inicie o `claude` e solicite a execução da suíte de testes padrão para confirmar que o comando configurado é adotado.

## Conexões
- [[claude-code-iniciar-sessao-interativa-cli]] — Veja também: Claude Code: iniciar sessão interativa no terminal.
- [[claude-code-gerenciar-permissoes-de-execucao-de-comandos]] — Veja também: Claude Code: gerenciar permissões de execução de comandos.
- [[copilot-registrar-instrucoes-do-repositorio]] — Conexão temática direta com copilot-registrar-instrucoes-do-repositorio.
- [[claude-code-validar-testes-antes-do-commit]] — Conexão temática direta com claude-code-validar-testes-antes-do-commit.

## Fontes
- [Anthropic Docs — Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Documentação oficial da cli claude code, comandos interativos, claude.md e arquitetura de agentes. Consulta: 2026-10-04.
- [Anthropic Docs — Claude Code Tutorials](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials) — Tutoriais oficiais de uso prático, permissões no terminal, ferramentas e fluxos de trabalho. Consulta: 2026-10-04.
