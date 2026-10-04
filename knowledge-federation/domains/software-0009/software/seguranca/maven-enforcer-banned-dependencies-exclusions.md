---
id: software.seguranca.tranche17.001685
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
fontes: ["https://maven.apache.org/enforcer/enforcer-rules/bannedDependencies.html", "https://maven.apache.org/plugins/maven-dependency-plugin/tree-mojo.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `bannedDependencies`: recusar coordenadas Maven com escopo e exceções explícitos

## Em uma frase
A regra banned dependencies permite proibir dependências selecionadas por coordenadas, padrões e opções de escopo configuradas no POM.

## Por que importa
Uma dependência pode ser bloqueada por política interna, substituição de biblioteca ou risco conhecido, inclusive quando chega de forma transitiva.

## Como funciona
Defina coordenadas e transitivity deliberadamente, liste exceções pequenas e investigue caminho de entrada antes de excluir um artefato pai.

## Exemplo
Bloqueie uma coordenada depreciada e, quando necessário, permita um módulo específico com justificativa em vez de whitelistar todo o grupo.

```text
mvn enforcer:enforce
```

## Limites e trade-offs
A regra compara coordenadas e configuração, não a identidade criptográfica do pacote nem a presença de uma vulnerabilidade.

## Como verificar
Rode `dependency:tree`, confirme se a dependência direta ou transitiva é capturada e teste se exceções têm o escopo esperado.

## Conexões
- [[maven-enforcer-ban-dynamic-versions-reproducibilidade]] — Banir versões Maven dinâmicas para builds reprodutíveis.
- [[maven-enforcer-require-java-maven-version-build-environment]] — Exigir versões de Java e Maven compatíveis com o build.

## Fontes
- [Maven Enforcer — Banned Dependencies](https://maven.apache.org/enforcer/enforcer-rules/bannedDependencies.html) — coordenadas, padrões, includes/excludes e searchTransitive; consultado em 2026-10-04.
- [Maven Dependency Plugin — dependency:tree](https://maven.apache.org/plugins/maven-dependency-plugin/tree-mojo.html) — localização da origem direta ou transitiva de uma coordenada; consultado em 2026-10-04.
