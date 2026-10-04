---
id: software.testes.tranche09.000324
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

# pytest: nomear parâmetros e proteger dados mutáveis

## Em uma frase
pytest.mark.parametrize cria múltiplas invocações; valores dos parâmetros são passados como estão, sem cópia automática.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Mutação de lista ou dicionário em um caso pode afetar outro caso parametrizado que compartilha o mesmo objeto.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Use IDs legíveis e factories/cópias quando cenário modifica estrutura mutável.

## Exemplo
Três formatos de payload recebem IDs estáveis; cada caso clona fixture antes de remover chaves durante o exercício.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Uma cópia profunda pode ser desnecessária para estruturas imutáveis e alterar a semântica testada.

## Como verificar
Inspecione a coleção antes de cada invocação, rode em ordem diferente e confirme que IDs localizam a falha individual.

## Conexões
- [[pytest-fixture-scope-isolation]] — Veja também: pytest: alinhar escopo de fixture ao ciclo de vida do recurso.
- [[pytest-indirect-param-fixture-setup]] — Veja também: pytest: usar indirect parametrization para setup configurável.

## Fontes
- [pytest — Parametrizing tests](https://docs.pytest.org/en/stable/how-to/parametrize.html) — parametrização de testes, IDs e geração de casos; consultado em 2026-10-02.
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
