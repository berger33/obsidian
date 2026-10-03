---
id: software.testes.tranche15.000881
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pestphp.com/docs/datasets", "https://pestphp.com/docs/hooks"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: criar dataset bound depois do setup de cada teste

## Em uma frase
Um dataset bound pode ser resolvido após o hook `beforeEach`, útil quando os registros de entrada dependem de banco ou de outro estado montado para cada caso.

## Por que importa
Materializar um modelo antes do setup comum pode deixar a fixture desatualizada ou fazê-la pertencer à conexão errada; adiar a resolução preserva a ordem de lifecycle entre preparação e consumo dos parâmetros.

## Como funciona
O recurso evita duplicar setup, mas continua sujeito ao isolamento do teste que o produz.

## Exemplo
Configure um dataset bound para obter usuários criados depois de `beforeEach` preparar o banco, e associe-o com `->with(...)` ao teste que valida a regra de negócio.

## Limites e trade-offs
Se o dataset fizer criação de estado compartilhado, retries ou paralelismo podem repetir esse efeito; confirme que a integração e as transações limpam cada cenário.

## Como verificar
Execute o mesmo teste isoladamente e junto à suíte, verificando que cada linha recebe dados recém-preparados e que nenhum registro vaza para o caso seguinte.

## Conexões
- [[pest-datasets-parametros-nomeados]] — Veja também: Pest 5: mapear datasets associativos por nome de parâmetro.
- [[pest-ci-ignora-testes-focados-com-only]] — Veja também: Pest 5: fazer o job de CI ignorar focos locais marcados only.

## Fontes
- [Pest 5 — Datasets](https://pestphp.com/docs/datasets) — datasets inline/compartilhados, chaves, parâmetros nomeados e bound datasets; consultado em 2026-10-02.
- [Pest 5 — Hooks](https://pestphp.com/docs/hooks) — ciclo beforeEach/afterEach e hooks de arquivo; consultado em 2026-10-02.
