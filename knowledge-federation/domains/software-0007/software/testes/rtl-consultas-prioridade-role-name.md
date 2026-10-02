---
id: software.testes.tranche08.000161
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://testing-library.com/docs/queries/about/", "https://testing-library.com/docs/guiding-principles/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testing Library: priorizar consultas por papel e nome

## Em uma frase
Escolha consultas que expressem como o elemento é percebido, priorizando papel acessível e nome antes de seletores estruturais.

## Por que importa
A consulta semântica tende a ser estável entre refatorações e, ao mesmo tempo, expõe controles que usuários de tecnologia assistiva precisam encontrar.

## Como funciona
Comece por getByRole com nome acessível; use label ou texto visível quando apropriado. Recorra a test ID quando não houver semântica utilizável e justifique a exceção.

## Exemplo
Um teste encontra o botão Salvar pelo papel e nome acessível; uma alteração que remove o rótulo passa a falhar por motivo compreensível.

## Limites e trade-offs
Nem toda estrutura customizada tem papel nativo e uma consulta por papel não garante conformidade completa com WCAG ou comportamento de leitor de tela.

## Como verificar
Inspecione a árvore acessível e confirme que nome e papel são únicos no contexto. Execute também verificações específicas de acessibilidade quando o requisito exigir.

## Conexões
- [[rtl-formulario-erro-associacao-label]] — Veja também: Testing Library: validar formulários pela relação label-controle.
- [[android-compose-semantics-assertions]] — Veja também: Android Compose: testar semântica e ações expostas.

## Fontes
- [Testing Library — About Queries](https://testing-library.com/docs/queries/about/) — seleção de elementos por papel, nome e prioridade; consultado em 2026-10-02.
- [Testing Library — Guiding Principles](https://testing-library.com/docs/guiding-principles/) — testes que refletem a utilização observável; consultado em 2026-10-02.
