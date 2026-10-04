---
id: software.seguranca.tranche17.001683
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://maven.apache.org/enforcer/enforcer-rules/dependencyConvergence.html", "https://maven.apache.org/plugins/maven-dependency-plugin/tree-mojo.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `dependencyConvergence`: detectar versões transitivas divergentes no grafo Maven

## Em uma frase
A regra dependency convergence sinaliza quando caminhos diferentes no grafo resolvem versões divergentes da mesma dependência.

## Por que importa
Conflitos podem tornar o classpath sensível à ordem de resolução e levar a comportamento que varia entre módulos ou ambientes.

## Como funciona
Inspecione a árvore, alinhe versões por dependency management ou atualize pais responsáveis e documente exceções inevitáveis.

## Exemplo
Se dois módulos puxam versões diferentes de uma biblioteca, a regra falha e orienta a convergência para versão compatível revisada.

```text
mvn enforcer:enforce
```

## Limites e trade-offs
Divergência não significa automaticamente vulnerabilidade nem incompatibilidade observável; convergir para uma versão não validada também pode introduzir regressões.

## Como verificar
Rode `mvn dependency:tree`, identifique os caminhos duplicados e execute testes após alinhar a versão selecionada.

## Conexões
- [[maven-enforcer-fail-default-true-policy]] — `fail` no Maven Enforcer: falhar por padrão e tratar warn-only com intenção.
- [[maven-enforcer-ban-dynamic-versions-reproducibilidade]] — Banir versões Maven dinâmicas para builds reprodutíveis.

## Fontes
- [Maven Enforcer — Dependency Convergence](https://maven.apache.org/enforcer/enforcer-rules/dependencyConvergence.html) — detecção de versões divergentes da mesma dependência no grafo; consultado em 2026-10-04.
- [Maven Dependency Plugin — dependency:tree](https://maven.apache.org/plugins/maven-dependency-plugin/tree-mojo.html) — inspeção dos caminhos e versões resolvidos no classpath; consultado em 2026-10-04.
