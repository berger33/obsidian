---
id: software.seguranca.tranche17.001688
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
fontes: ["https://maven.apache.org/enforcer/maven-enforcer-plugin/usage.html", "https://maven.apache.org/pom.html#Inheritance"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Centralizar regras Enforcer em parent POM sem perder escopo por módulo

## Em uma frase
Configurar regras em parent POM ajuda a aplicar política compartilhada, mas a efetiva herança e execução devem ser verificadas nos módulos do reactor.

## Por que importa
Um módulo que não herda ou não ativa o plugin pode ficar fora do controle apesar da configuração visível na raiz.

## Como funciona
Revise POM efetivo, perfis ativos e execução de cada módulo, mantendo regras específicas somente onde o contrato realmente difere.

## Exemplo
No monorepo Maven, rode goal no reactor inteiro e inspecione logs por módulo para confirmar que todos executaram o mesmo conjunto de regras.

```text
mvn enforcer:enforce
```

## Limites e trade-offs
Configuração central não garante enforcement se builds usam POM diferente, perfil desativado ou invocação parcial sem lifecycle adequado.

## Como verificar
Use `help:effective-pom`, execute a regra por reactor e inclua módulo de teste com violação para demonstrar cobertura.

## Conexões
- [[maven-enforcer-require-property-dependency-management]] — Exigir propriedades e campos de versão no Maven POM.
- [[maven-enforcer-version-rule-plugin-pin-maintenance]] — Fixar a versão do Maven Enforcer Plugin e revisar mudanças de regras.

## Fontes
- [Maven Enforcer — Usage](https://maven.apache.org/enforcer/maven-enforcer-plugin/usage.html) — regras do plugin declaradas em POM e execução por módulo; consultado em 2026-10-04.
- [Apache Maven — POM Inheritance](https://maven.apache.org/pom.html#Inheritance) — herança entre parent POM e módulos e limites de configuração efetiva; consultado em 2026-10-04.
