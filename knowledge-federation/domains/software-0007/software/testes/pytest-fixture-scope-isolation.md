---
id: software.testes.tranche09.000323
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://docs.pytest.org/en/stable/reference/fixtures.html", "https://docs.pytest.org/en/stable/how-to/tmp_path.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest: alinhar escopo de fixture ao ciclo de vida do recurso

## Em uma frase
Function, class, module e session scopes controlam quantas vezes pytest cria uma fixture durante a execução.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Escopo longo para objeto mutável pode compartilhar estado inesperado; escopo curto para container caro pode desperdiçar minutos.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Escolha escopo pelo lifecycle real e mantenha dados de teste isolados mesmo quando infraestrutura é compartilhada.

## Exemplo
Container PostgreSQL é session-scoped, mas cada teste abre transação e namespace de dados controlados.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Escopo maior não garante serialização em workers xdist e fixture function-scoped não pode ser dependência de fixture de escopo mais longo.

## Como verificar
Execute dois testes que alteram estado em paralelo e confirme isolamento lógico apesar do container compartilhado.

## Conexões
- [[pytest-yield-fixture-teardown-order]] — Veja também: pytest: ordenar teardown de fixtures dependentes.
- [[pytest-parametrize-ids-values-reference]] — Veja também: pytest: nomear parâmetros e proteger dados mutáveis.

## Fontes
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
- [pytest — Temporary directories and files](https://docs.pytest.org/en/stable/how-to/tmp_path.html) — tmp_path e tmp_path_factory por escopo de fixture; consultado em 2026-10-02.
