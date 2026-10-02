---
id: software.testes.tranche09.000329
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
fontes: ["https://docs.pytest.org/en/stable/how-to/skipping.html", "https://docs.pytest.org/en/stable/reference/fixtures.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest: ativar strict para xfail não mascarar regressão

## Em uma frase
xfail documenta falha conhecida esperada; com strict ativo, um caso que passa inesperadamente pode falhar como XPASS.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Sem strict, correção acidental pode permanecer escondida como resultado aceitável e o marcador nunca ser removido.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Associe xfail a issue e condição específica e habilite strict para exigir revisão quando comportamento mudar.

## Exemplo
Bug conhecido retorna resultado correto após correção; pipeline sinaliza XPASS e força remoção do xfail ou ajuste do cenário.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Não use xfail para instabilidade genérica nem marque toda plataforma quando falha só ocorre numa condição identificada.

## Como verificar
Execute caso ainda falho e versão corrigida e confirme que o segundo caso faz o job falhar como XPASS strict.

## Conexões
- [[pytest-monkeypatch-env-teardown]] — Veja também: pytest: escopar monkeypatch de ambiente e dependências.

## Fontes
- [pytest — Skip and xfail](https://docs.pytest.org/en/stable/how-to/skipping.html) — skip, xfail e strict xfail; consultado em 2026-10-02.
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
