---
id: software.seguranca.tranche17.001676
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html#sec:verification-metadata", "https://docs.gradle.org/current/userguide/multi_project_builds.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Centralizar `verification-metadata.xml` no repositório para builds reproduzíveis

## Em uma frase
A documentação do Gradle coloca metadata de verificação em `gradle/verification-metadata.xml`, permitindo que builds do projeto compartilhem policy versionada.

## Por que importa
Configuração local invisível permite que dois desenvolvedores aceitem artefatos diferentes e torna difícil auditar a expansão do conjunto confiável.

## Como funciona
Inclua o arquivo no controle de versão, aplique o mesmo modo de verificação em CI e evite exceções globais que enfraqueçam a policy sem evidência.

## Exemplo
Uma alteração de dependência deve atualizar metadata no mesmo pull request e apresentar diffs de coordenadas e hashes aos revisores.

```text
git diff -- gradle/verification-metadata.xml
```

## Limites e trade-offs
Arquivos compartilhados só oferecem consistência se todos os builds relevantes realmente carregam a configuração e usam versões Gradle compatíveis.

## Como verificar
Clone o repositório em workspace limpo, execute build e confirme que a resolução não depende de metadata pessoal em `~/.gradle`.

## Conexões
- [[gradle-verification-metadata-trust-keys-export-review]] — Importar e confiar em chaves para verificação de assinaturas Gradle.
- [[gradle-verification-metadata-plugins-build-dependencies]] — Cobertura do Gradle Dependency Verification para plugins e configurações resolvidas.

## Fontes
- [Gradle — metadata compartilhada](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:verification-metadata) — localização/versionamento de `verification-metadata.xml` e escopo do build; consultado em 2026-10-04.
- [Gradle — Multi-Project Builds](https://docs.gradle.org/current/userguide/multi_project_builds.html) — estrutura de root project e subprojects que compartilham configuração; consultado em 2026-10-04.
