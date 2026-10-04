---
id: software.testes.tranche10.000398
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://vitest.dev/guide/coverage", "https://vitest.dev/guide/projects"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vitest: declarar provider e formato de relatório de coverage

## Em uma frase
Vitest suporta cobertura via provider nativo v8 ou instrumentação Istanbul, com configuração de reporters.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Um job pode falhar por falta do provider opcional ou publicar formato que o serviço de CI não consome.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Instale o provider escolhido, declare formatos necessários e mantenha paths e exclusões alinhados ao código-fonte do projeto.

## Exemplo
A CI gera text para logs e HTML para revisão local usando o provider aprovado pela equipe.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. Um relatório mostra linhas executadas, não correção funcional; exclusões de arquivos também alteram o denominador apresentado.

## Como verificar
Compare arquivos incluídos, provider e resumo do runner com a política de cobertura registrada para o repositório.

## Conexões
- [[vitest-isolation-parallelism-tradeoff]] — Veja também: Vitest: avaliar custo antes de desativar isolamento.
- [[vitest-snapshot-diff-revisao-intencional]] — Veja também: Vitest: revisar o diff antes de atualizar snapshot.

## Fontes
- [Vitest — Coverage](https://vitest.dev/guide/coverage) — providers e opções de relatório de cobertura; consultado em 2026-10-02.
- [Vitest — Test projects](https://vitest.dev/guide/projects) — configuração, herança e opções globais de projetos; consultado em 2026-10-02.
