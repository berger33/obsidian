---
id: software.testes.tranche12.000578
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

# TestNG: usar listeners para observar execução

## Em uma frase
Listeners recebem eventos ou oportunidades de extensão durante a execução e podem ser registrados por anotação ou configuração da suite.

## Por que importa
Observabilidade centralizada permite gerar métricas, anexos ou políticas comuns sem misturar instrumentação repetitiva em cada método de teste.

## Como funciona
Escolha a interface de listener adequada ao ciclo que precisa observar, registre-a no ponto da suite e mantenha assertions do requisito dentro dos testes correspondentes.

## Exemplo
Um listener pode anexar identificador de build e tempo de execução ao relatório quando cada teste começa e termina.

## Limites e trade-offs
Listeners globais também podem alterar status, interceptar métodos ou ser acionados em mais de uma suite; lógica invisível neles pode dificultar entender por que um teste falhou.

## Como verificar
Execute uma suite mínima com sucesso e falha controlados e confira se cada evento é emitido uma vez e se o resultado original permanece verificável.

## Conexões
- [[testng-factory-instancias]] — Veja também: TestNG: criar instâncias de teste com `@Factory`.
- [[testng-invocationcount-timeout]] — Veja também: TestNG: interpretar `invocationCount` e seu timeout.

## Fontes
- [TestNG — Documentation](https://testng.org/documentation.html) — grupos, XML, execução paralela, listeners e relatórios; consultado em 2026-10-02.
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
