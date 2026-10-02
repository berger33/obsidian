---
id: software.testes.tranche14.000824
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://nox.thea.codes/en/stable/config.html", "https://nox.thea.codes/en/stable/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nox: tirar tarefas auxiliares da execução padrão

## Em uma frase
Por padrão Nox executa todas as sessões configuradas, a menos que opções ou `default=False` alterem a seleção padrão.

## Por que importa
Uma sessão de deploy, benchmark caro ou ambiente interativo não deve entrar na suite de verificação comum por acidente.

## Como funciona
Marque tarefas não rotineiras como `default=False` e mantenha sessões de lint/test explicitamente relevantes para a execução padrão.

## Exemplo
Uma sessão `docs-preview` pode ficar disponível por nome para uso local, mas não executa sempre que a CI chama `nox`.

## Limites e trade-offs
`default=False` não impede seleção explícita; a política deve ser documentada para quem mantém o noxfile.

## Como verificar
Liste as sessões e execute Nox sem argumentos para confirmar que apenas tarefas pretendidas fazem parte do conjunto padrão.

## Conexões
- [[nox-no-virtualenv-scope]] — Veja também: Nox: dispensar virtualenv apenas quando o ambiente atual for parte do contrato.
- [[nox-requires-session-dependency-order]] — Veja também: Nox: declarar dependências entre sessões com requires.

## Fontes
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
- [Nox — Command-line usage](https://nox.thea.codes/en/stable/usage.html) — seleção e listagem de sessões, reuso de virtualenvs e opções de CLI; consultado em 2026-10-02.
