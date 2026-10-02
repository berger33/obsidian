---
id: software.testes.tranche14.000763
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://maven.apache.org/surefire/maven-surefire-plugin/examples/junit-platform.html", "https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven Surefire: conferir engines da JUnit Platform

## Em uma frase
A integração com JUnit Platform usa engines presentes nas dependências para executar frameworks compatíveis; no Surefire 3.6.0 o provider unificado é documentado.

## Por que importa
Dependência da API sem engine executável pode compilar testes e ainda deixar casos ausentes na descoberta.

## Como funciona
Declare o engine apropriado no escopo de teste e confira a seleção de provider correspondente à versão do plugin e do framework.

## Exemplo
Um módulo Jupiter adiciona `junit-jupiter-engine`; a saída de execução e os relatórios devem mostrar testes daquela engine, não apenas a compilação das classes.

## Limites e trade-offs
Compatibilidade de versões e engines não é universal; versões antigas ou suites especiais podem exigir ajustes diferentes.

## Como verificar
Faça uma classe de teste mínima por engine e valide descoberta em CI ao atualizar Maven, plugin ou framework.

## Conexões
- [[maven-single-test-selection]] — Veja também: Maven Surefire: selecionar classe sem confundir o escopo.
- [[maven-test-class-naming-patterns]] — Veja também: Maven Surefire: tornar convenções de nome parte da descoberta.

## Fontes
- [Maven Surefire — JUnit Platform](https://maven.apache.org/surefire/maven-surefire-plugin/examples/junit-platform.html) — integração com engines JUnit Platform e seleção de classes; consultado em 2026-10-02.
- [Maven Surefire — test goal](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html) — parâmetros do goal test, forkCount, seleção, execução paralela e sistema de propriedades; consultado em 2026-10-02.
