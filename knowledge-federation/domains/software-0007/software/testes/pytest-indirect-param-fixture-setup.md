---
id: software.testes.tranche09.000325
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
fontes: ["https://docs.pytest.org/en/stable/how-to/parametrize.html", "https://docs.pytest.org/en/stable/reference/fixtures.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest: usar indirect parametrization para setup configurável

## Em uma frase
Parametrização indirect encaminha valores para fixture via request.param, permitindo que ela construa recurso durante a preparação.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Parametrizar objetos já montados no collection pode abrir conexões cedo demais e esconder lifecycle do recurso.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Passe apenas dados de configuração como parâmetro e instancie o recurso na fixture com cleanup definido.

## Exemplo
IDs de backend escolhem SQLite ou banco temporário; fixture constrói conexão durante setup e fecha após o caso.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Parâmetros e fixtures podem multiplicar testes rapidamente; escolha combinações alinhadas ao risco.

## Como verificar
Confirme ordem de collection e setup e que cada configuração fecha o recurso após falha ou conclusão.

## Conexões
- [[pytest-parametrize-ids-values-reference]] — Veja também: pytest: nomear parâmetros e proteger dados mutáveis.
- [[pytest-autouse-fixture-hidden-side-effects]] — Veja também: pytest: limitar efeitos ocultos de fixtures autouse.

## Fontes
- [pytest — Parametrizing tests](https://docs.pytest.org/en/stable/how-to/parametrize.html) — parametrização de testes, IDs e geração de casos; consultado em 2026-10-02.
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
