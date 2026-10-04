---
id: software.seguranca.tranche17.001687
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
fontes: ["https://maven.apache.org/enforcer/enforcer-rules/requireProperty.html", "https://maven.apache.org/enforcer/enforcer-rules/requirePluginVersions.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Exigir propriedades e campos de versão no Maven POM

## Em uma frase
O catálogo do Enforcer inclui regras para exigir propriedades, versões de plugins ou metadados específicos antes de executar o build.

## Por que importa
Campos ausentes podem levar a defaults implícitos e diferenças entre módulos, reduzindo visibilidade de configurações necessárias à release.

## Como funciona
Escolha requisitos que correspondam ao contrato real, mantenha a regra no parent POM e forneça mensagem de erro que indique a propriedade faltante.

## Exemplo
Uma regra pode exigir que uma propriedade de versão de biblioteca esteja definida, evitando que um módulo use valor local não revisado.

```text
mvn enforcer:enforce
```

## Limites e trade-offs
Exigir que uma propriedade exista não valida automaticamente se seu valor é correto ou se atende a política de segurança.

## Como verificar
Remova a propriedade numa fixture, rode Enforcer e confira se o erro identifica o campo sem mascarar outras falhas.

## Conexões
- [[maven-enforcer-require-java-maven-version-build-environment]] — Exigir versões de Java e Maven compatíveis com o build.
- [[maven-enforcer-configuracao-em-parent-versus-modulos]] — Centralizar regras Enforcer em parent POM sem perder escopo por módulo.

## Fontes
- [Maven Enforcer — Require Property](https://maven.apache.org/enforcer/enforcer-rules/requireProperty.html) — presença de propriedades e validação opcional por regex; consultado em 2026-10-04.
- [Maven Enforcer — Require Plugin Versions](https://maven.apache.org/enforcer/enforcer-rules/requirePluginVersions.html) — versões explícitas de plugins no POM ou pluginManagement; consultado em 2026-10-04.
