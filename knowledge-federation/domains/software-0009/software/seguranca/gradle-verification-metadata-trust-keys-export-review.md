---
id: software.seguranca.tranche17.001675
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html#sec:signature-verification", "https://docs.gradle.org/current/userguide/dependency_verification.html#sec:bootstrapping-verification"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Importar e confiar em chaves para verificação de assinaturas Gradle

## Em uma frase
O arquivo de metadata pode armazenar chaves usadas na validação de assinatura, por isso identidade, origem e escopo de cada chave precisam de revisão.

## Por que importa
Uma chave incluída apenas porque uma execução a encontrou pode transformar uma assinatura desconhecida em conteúdo aceito pelo build.

## Como funciona
Confirme fingerprints por canal independente, limite a associação ao componente esperado e trate rotação como mudança de policy com revisão explícita.

## Exemplo
Antes de adicionar uma chave nova, obtenha fingerprint do fornecedor por documentação autenticada ou processo interno e compare-a com a informação da metadata.

## Limites e trade-offs
Assinatura válida comprova posse da chave associada ao pacote, não reputação do mantenedor nem segurança do conteúdo assinado.

## Como verificar
Revise a entrada de chave no XML, compare fingerprint com registro confiável e execute build com chave incorreta em fixture isolada.

## Conexões
- [[gradle-verification-metadata-unknown-artifact-fail-closed]] — Tratar artefato sem entrada de verificação como mudança que exige revisão.
- [[gradle-verification-metadata-shared-project-scope]] — Centralizar `verification-metadata.xml` no repositório para builds reproduzíveis.

## Fontes
- [Gradle — trust keys e assinatura](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:signature-verification) — chaves confiadas e verificação de assinatura de artefatos; consultado em 2026-10-04.
- [Gradle — bootstrapping trusted keys](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:bootstrapping-verification) — revisão de chaves obtidas durante bootstrap; consultado em 2026-10-04.
