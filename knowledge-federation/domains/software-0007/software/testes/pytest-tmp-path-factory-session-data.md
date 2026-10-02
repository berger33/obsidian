---
id: software.testes.tranche09.000321
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
fontes: ["https://docs.pytest.org/en/stable/how-to/tmp_path.html", "https://docs.pytest.org/en/stable/reference/fixtures.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest: reservar tmp_path_factory para artefato caro compartilhado

## Em uma frase
tmp_path_factory permite criar diretórios temporários em escopo mais amplo, útil quando vários testes reutilizam setup caro.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Compartilhar artefato mutável entre funções economiza preparação, mas pode introduzir dependência de ordem e corrida.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Crie uma fixture session-scoped somente para dados imutáveis preparados uma vez; copie ou ramifique estado mutável para cada teste.

## Exemplo
Suite gera grande arquivo de índice uma vez e cada teste consulta cópia própria para testar atualização.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Factory session não torna conteúdo compartilhado seguro para mutação concorrente nem apropriado para segredo persistente.

## Como verificar
Rode testes em paralelo, valide hash do artefato base e confirme que nenhuma função alterou a cópia comum.

## Conexões
- [[pytest-tmp-path-per-test-files]] — Veja também: pytest: usar tmp_path para arquivos isolados por teste.
- [[pytest-yield-fixture-teardown-order]] — Veja também: pytest: ordenar teardown de fixtures dependentes.

## Fontes
- [pytest — Temporary directories and files](https://docs.pytest.org/en/stable/how-to/tmp_path.html) — tmp_path e tmp_path_factory por escopo de fixture; consultado em 2026-10-02.
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
