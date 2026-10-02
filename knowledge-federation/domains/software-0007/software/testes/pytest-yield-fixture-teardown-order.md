---
id: software.testes.tranche09.000322
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

# pytest: ordenar teardown de fixtures dependentes

## Em uma frase
Fixtures que usam yield podem executar teardown após o teste, e dependências definem a ordem de preparação e desmontagem.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Se recurso externo não é fechado por causa de falha no setup, testes seguintes podem herdar conexão ou lock.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Registre cleanup imediatamente depois de criar recurso e componha fixtures para que dependências sejam desmontadas na ordem apropriada.

## Exemplo
Fixture abre servidor local e registra encerramento antes de preparar banco dependente; o teardown fecha banco antes do servidor.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Código que falha antes de chegar ao yield pode não executar a parte pós-yield daquela fixture.

## Como verificar
Force falha em cada etapa de setup e confirme que todos os recursos já criados são limpos.

## Conexões
- [[pytest-tmp-path-factory-session-data]] — Veja também: pytest: reservar tmp_path_factory para artefato caro compartilhado.
- [[pytest-fixture-scope-isolation]] — Veja também: pytest: alinhar escopo de fixture ao ciclo de vida do recurso.

## Fontes
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
- [pytest — Temporary directories and files](https://docs.pytest.org/en/stable/how-to/tmp_path.html) — tmp_path e tmp_path_factory por escopo de fixture; consultado em 2026-10-02.
