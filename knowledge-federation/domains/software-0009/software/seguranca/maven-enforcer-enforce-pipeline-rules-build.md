---
id: software.seguranca.tranche17.001681
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
fontes: ["https://maven.apache.org/enforcer/maven-enforcer-plugin/usage.html#the-enforcer-enforce-mojo", "https://maven.apache.org/enforcer/maven-enforcer-plugin/enforce-mojo.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `maven-enforcer-plugin`: aplicar requisitos de build com regras declaradas

## Em uma frase
O Maven Enforcer executa verificações configuradas durante o build e pode impedir que projetos violem requisitos técnicos estabelecidos no POM.

## Por que importa
Regras locais e explícitas tornam convenções de versões, dependências e ambiente executáveis em vez de depender de memória do maintainer.

## Como funciona
Configure plugin e regras na estrutura Maven apropriada, rode `enforcer:enforce` em CI e revise falhas como mudanças de contrato do build.

## Exemplo
Um parent POM pode centralizar regras compartilhadas e as builds de módulos podem executá-las antes de empacotar artefatos.

```text
mvn enforcer:enforce
```

## Limites e trade-offs
Enforcer verifica condições configuradas; não é um scanner de CVEs nem substitui testes funcionais ou revisão de código.

## Como verificar
Confirme a versão do plugin, as regras realmente ativadas e que uma configuração deliberadamente inválida falha na CI.

## Conexões
- [[maven-enforcer-fail-default-true-policy]] — `fail` no Maven Enforcer: falhar por padrão e tratar warn-only com intenção.

## Fontes
- [Maven Enforcer — Usage](https://maven.apache.org/enforcer/maven-enforcer-plugin/usage.html#the-enforcer-enforce-mojo) — configuração declarativa das regras e finalidade do goal `enforce`; consultado em 2026-10-04.
- [Maven Enforcer — `enforcer:enforce` goal](https://maven.apache.org/enforcer/maven-enforcer-plugin/enforce-mojo.html) — escopo de execução por módulo e fase de lifecycle; consultado em 2026-10-04.
