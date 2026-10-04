---
id: software.testes.tranche09.000320
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

# pytest: usar tmp_path para arquivos isolados por teste

## Em uma frase
A fixture tmp_path fornece um diretório temporário exclusivo para cada invocação de teste que solicita esse recurso.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Arquivos escritos em pasta compartilhada podem sobreviver entre testes, colidir em paralelo ou contaminar reexecuções.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Escreva inputs e outputs sob tmp_path e passe caminhos explícitos às funções sob teste.

## Exemplo
Dois testes serializam configurações distintas no próprio diretório e confirmam que nenhum leu o arquivo do outro.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Não dependa de caminho absoluto específico nem retenha o diretório depois que o teste termina.

## Como verificar
Execute em paralelo e verifique que cada fixture aponta a diretório diferente e que o teste tolera cleanup.

## Conexões
- [[pytest-tmp-path-factory-session-data]] — Veja também: pytest: reservar tmp_path_factory para artefato caro compartilhado.

## Fontes
- [pytest — Temporary directories and files](https://docs.pytest.org/en/stable/how-to/tmp_path.html) — tmp_path e tmp_path_factory por escopo de fixture; consultado em 2026-10-02.
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
