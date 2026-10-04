---
id: software.seguranca.tranche17.001686
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
fontes: ["https://maven.apache.org/enforcer/enforcer-rules/requireJavaVersion.html", "https://maven.apache.org/enforcer/enforcer-rules/requireMavenVersion.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Exigir versões de Java e Maven compatíveis com o build

## Em uma frase
Regras Enforcer podem impor versões mínimas ou intervalos para Maven e JDK usados na construção do projeto.

## Por que importa
Diferenças locais de toolchain podem alterar compilação, plugins e resolução, dificultando reproduzir o artefato validado pela CI.

## Como funciona
Declare limites que correspondam ao runtime suportado, use Maven Wrapper e fixe imagem de CI para complementar as verificações no POM.

## Exemplo
Um build pode recusar JDK fora do intervalo aprovado e direcionar desenvolvedores ao wrapper e ao container de compilação oficial.

```text
mvn enforcer:enforce
```

## Limites e trade-offs
Verificar a versão declarada do runtime não prova que o JDK instalado é íntegro nem garante igualdade de todo ambiente.

## Como verificar
Teste a regra com versões abaixo e dentro do intervalo e compare a saída com `mvn -version` no job de release.

## Conexões
- [[maven-enforcer-banned-dependencies-exclusions]] — `bannedDependencies`: recusar coordenadas Maven com escopo e exceções explícitos.
- [[maven-enforcer-require-property-dependency-management]] — Exigir propriedades e campos de versão no Maven POM.

## Fontes
- [Maven Enforcer — Require Java Version](https://maven.apache.org/enforcer/enforcer-rules/requireJavaVersion.html) — regras de intervalo e normalização de versão JDK; consultado em 2026-10-04.
- [Maven Enforcer — Require Maven Version](https://maven.apache.org/enforcer/enforcer-rules/requireMavenVersion.html) — regras de versão Maven usadas pelo mesmo build; consultado em 2026-10-04.
