---
id: software.criacao_ia.tranche01.000009
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat", "https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Copilot: registrar instruções do repositório

## Em uma frase

Instruções versionadas podem comunicar ao assistente convenções estáveis de build, teste, estilo e organização do projeto.

## Por que importa

A equipe evita repetir regras em cada prompt e reduz sugestões incompatíveis entre pessoas que trabalham no mesmo repositório.

## Como funciona

Mantenha orientações concisas, verificáveis e próximas do código; indique comandos reais e a localização de guias mais completos.

## Exemplo

Um arquivo de instruções pode dizer como rodar testes do pacote e lembrar que migrações de banco precisam de revisão específica.

## Limites e trade-offs

Regras desatualizadas viram uma fonte de erro; um documento de instruções não é mecanismo de segurança nem autorização para executar qualquer comando.

## Como verificar

Compare cada comando documentado com a configuração atual de CI e revise instruções quando mudar ferramenta, estrutura ou política.

## Conexões
- [[copilot-explicitar-casos-de-erro-no-prompt]] — Copilot: explicitar casos de erro no prompt.
- [[copilot-inspecionar-o-diff-antes-de-aceitar]] — Copilot: inspecionar o diff antes de aceitar.

## Fontes
- [GitHub Docs — Prompt engineering para Copilot Chat](https://docs.github.com/copilot/concepts/prompt-engineering-for-copilot-chat) — Orientações oficiais para prompts com contexto, objetivo e detalhes concretos. Consulta: 2026-10-04.
- [GitHub Docs — Fazer perguntas ao Copilot na IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide) — Documenta os modos Ask, Edit, Agent e Plan e o uso no ambiente de desenvolvimento. Consulta: 2026-10-04.
