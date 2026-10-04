---
id: software.testes.tranche10.000395
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
fontes: ["https://vitest.dev/guide/mocking/modules", "https://vitest.dev/api/vi.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vitest Browser Mode: distinguir spy de substituição de export ESM

## Em uma frase
Em Browser Mode, módulos ESM nativos têm namespace de importação que não pode ser substituído como um objeto mutável comum.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Uma estratégia de mock que funciona no Node pode falhar ao tentar sobrescrever export já exposto pelo browser.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Use o suporte documentado de spy do Browser Mode, como spy: true quando aplicável, e verifique a API para a configuração instalada.

## Exemplo
Um teste mantém a implementação real do módulo no browser e espiona chamadas a um export sem reatribuir a namespace.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. A sintaxe e compatibilidade de Browser Mode são específicas do runner e não devem ser copiadas cegamente de um teste Node.

## Como verificar
Execute o mesmo contrato no modo browser e no pool Node se ambos forem parte da matriz do projeto.

## Conexões
- [[vitest-setsystemtime-nao-disparar-timers]] — Veja também: Vitest: separar setSystemTime do avanço de timers.
- [[vitest-projects-inheritance-opcoes-globais]] — Veja também: Vitest: separar configuração raiz e configuração de cada projeto.

## Fontes
- [Vitest — Module mocking](https://vitest.dev/guide/mocking/modules) — mocking de módulos, hoisting e limitações do Browser Mode; consultado em 2026-10-02.
- [Vitest — vi API](https://vitest.dev/api/vi.html) — mock functions, timers, relógio do sistema e ciclo de vida de mocks; consultado em 2026-10-02.
