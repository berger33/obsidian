---
id: software.testes.tranche10.000390
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

# Vitest: considerar hoisting de vi.mock antes do import

## Em uma frase
vi.mock é elevado pelo transformador do Vitest para executar antes dos imports estáticos do módulo de teste.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Uma factory que lê variável de topo pode ser executada antes da inicialização dessa variável e falhar em temporal dead zone.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Use vi.hoisted para valores necessários pela factory ou mova a preparação para a própria factory com importOriginal quando apropriado.

## Exemplo
O teste cria um mock hoisted da função de relógio e só depois importa o módulo que a consome.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. Hoisting depende do transformador e das regras do ambiente; uma importação dinâmica tem timing diferente.

## Como verificar
Inspecione o módulo realmente carregado e faça uma execução mínima com a versão/configuração Vite usada pelo projeto.

## Conexões
- [[vitest-domock-mock-runtime-import]] — Veja também: Vitest: usar vi.doMock para substituição não hoisted.

## Fontes
- [Vitest — vi API](https://vitest.dev/api/vi.html) — mock functions, timers, relógio do sistema e ciclo de vida de mocks; consultado em 2026-10-02.
- [Vitest — Module mocking](https://vitest.dev/guide/mocking/modules) — mocking de módulos, hoisting e limitações do Browser Mode; consultado em 2026-10-02.
