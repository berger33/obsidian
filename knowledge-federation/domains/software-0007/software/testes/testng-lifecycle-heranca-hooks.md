---
id: software.testes.tranche12.000574
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
fontes: ["https://testng.org/annotations.html", "https://testng.org/documentation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: ordem de hooks de configuração herdados

## Em uma frase
Os métodos `@Before...` e `@After...` descrevem fases diferentes do ciclo de vida e são herdados por classes de teste.

## Por que importa
Compartilhar preparação por superclasse evita repetição, mas a ordem entre níveis de herança afeta quais recursos estão disponíveis e quando a limpeza acontece.

## Como funciona
O TestNG executa configurações `Before` da superclasse para a subclasse e as configurações `After` no sentido inverso; nomeie cada hook pelo recurso que prepara ou libera.

## Exemplo
Uma classe base pode inicializar cliente e credenciais de teste, enquanto uma subclasse cria dados específicos; a limpeza específica acontece antes de encerrar o cliente comum.

## Limites e trade-offs
Colocar todo o estado em hooks herdados dificulta saber se uma falha ocorreu na fixture comum ou numa extensão particular da classe.

## Como verificar
Registre a ordem de chamadas em uma classe derivada e provoque falha no teste para confirmar que os hooks de saída ainda deixam o recurso no estado previsto.

## Conexões
- [[testng-groups-selecao]] — Veja também: TestNG: usar groups para selecionar conjuntos de testes.
- [[testng-dataprovider-parallel]] — Veja também: TestNG: DataProvider paralelo sem estado compartilhado.

## Fontes
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
- [TestNG — Documentation](https://testng.org/documentation.html) — grupos, XML, execução paralela, listeners e relatórios; consultado em 2026-10-02.
