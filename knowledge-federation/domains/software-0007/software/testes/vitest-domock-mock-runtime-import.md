---
id: software.testes.tranche10.000391
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
fontes: ["https://vitest.dev/api/vi.html", "https://vitest.dev/guide/mocking/modules"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vitest: usar vi.doMock para substituição não hoisted

## Em uma frase
vi.doMock registra um mock em runtime e não é içado como vi.mock.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Em testes que precisam configurar uma resposta diferente por caso, um mock hoisted pode ser aplicado antes da preparação específica.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Configure vi.doMock e importe dinamicamente o módulo depois, controlando o cache de imports quando o teste exige nova avaliação.

## Exemplo
Duas invocações importam dinamicamente o consumidor após vi.doMock com factories diferentes e afirmam cada resultado isoladamente.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. Imports estáticos já avaliados não são substituídos retroativamente; resetModules limpa cache, mas não reescreve referências existentes.

## Como verificar
Confirme qual import foi avaliado em cada caso e remova mocks depois para evitar efeito sobre testes seguintes.

## Conexões
- [[vitest-vi-mock-hoisting-importacao]] — Veja também: Vitest: considerar hoisting de vi.mock antes do import.
- [[vitest-setupfiles-mocks-modulos-cache]] — Veja também: Vitest: planejar mocks registrados em setupFiles.

## Fontes
- [Vitest — vi API](https://vitest.dev/api/vi.html) — mock functions, timers, relógio do sistema e ciclo de vida de mocks; consultado em 2026-10-02.
- [Vitest — Module mocking](https://vitest.dev/guide/mocking/modules) — mocking de módulos, hoisting e limitações do Browser Mode; consultado em 2026-10-02.
