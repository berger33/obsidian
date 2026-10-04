---
id: software.seguranca.tranche17.001677
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html#sec:dependency-verification-scope", "https://docs.gradle.org/current/userguide/composite_builds.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cobertura do Gradle Dependency Verification para plugins e configurações resolvidas

## Em uma frase
A verificação é aplicada quando Gradle resolve dependências cobertas pela configuração do build; plugins e dependências de build devem ser incluídos na validação real.

## Por que importa
Uma equipe pode verificar bibliotecas de aplicação e esquecer componentes usados para executar a própria compilação, que também influenciam o artefato final.

## Como funciona
Revise os resolvers envolvidos, execute cenários que carregam plugins e configurações relevantes e confira se metadata contém os componentes observados.

## Exemplo
Um CI deve usar o wrapper e o build real do produto, incluindo plugins e tarefas de geração, para confirmar cobertura da cadeia de build.

```text
./gradlew help
```

## Limites e trade-offs
Escopo e comportamento variam por modo e configuração; builds incluídos usam a metadata do build consumidor, então a presença do arquivo não prova cobertura de toda resolução sem executar os cenários reais.

## Como verificar
Compare relatório de componentes resolvidos em build de aplicação e build de plugins, e introduza artefato conhecido para testar enforcement.

## Conexões
- [[gradle-verification-metadata-shared-project-scope]] — Centralizar `verification-metadata.xml` no repositório para builds reproduzíveis.
- [[gradle-dependency-locking-version-selection-diferenca-integridade]] — Dependency Locking e Dependency Verification no Gradle: versão fixa versus bytes verificados.

## Fontes
- [Gradle — plugins e dependências de build](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:dependency-verification-scope) — resoluções verificadas, plugins e build logic; consultado em 2026-10-04.
- [Gradle — Included Builds](https://docs.gradle.org/current/userguide/composite_builds.html) — escopo próprio de included builds em relação ao build consumidor; consultado em 2026-10-04.
