---
id: software.testes.tranche12.000573
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://testng.org/documentation.html", "https://testng.org/annotations.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: usar groups para selecionar conjuntos de testes

## Em uma frase
Groups etiquetam métodos ou classes e podem ser incluídos ou excluídos em configuração XML ou na linha de comando.

## Por que importa
A seleção por grupo permite construir suítes de smoke, integração ou plataforma sem duplicar classes, desde que os nomes representem uma finalidade consistente.

## Como funciona
Atribua grupos na anotação `@Test`, filtre-os na suite e mantenha convenção para grupos herdados quando a anotação estiver na classe.

## Exemplo
Uma pipeline pode executar o grupo `smoke` em cada pull request e reservar o grupo `external` para um job que dispõe de credenciais específicas.

## Limites e trade-offs
Group filtering não controla a ordem dos métodos do grupo e um conjunto mal nomeado pode esconder testes de uma execução padrão por acidente.

## Como verificar
Liste ou execute cada suite configurada e compare os nomes descobertos com a política de seleção esperada para a pipeline.

## Conexões
- [[testng-dependencies-hard-soft]] — Veja também: TestNG: dependências hard e soft entre testes.
- [[testng-lifecycle-heranca-hooks]] — Veja também: TestNG: ordem de hooks de configuração herdados.

## Fontes
- [TestNG — Documentation](https://testng.org/documentation.html) — grupos, XML, execução paralela, listeners e relatórios; consultado em 2026-10-02.
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
