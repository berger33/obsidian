---
id: software.seguranca.tranche17.001673
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html#sec:verification-metadata", "https://docs.gradle.org/current/userguide/dependency_verification.html#sec:signature-verification"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Checksums e assinaturas PGP no Gradle: propriedades diferentes de verificação

## Em uma frase
Gradle permite registrar checksums para igualdade de bytes e assinaturas para validar uma relação criptográfica com chaves públicas confiadas.

## Por que importa
Um checksum pode detectar mudança em um artefato conhecido, enquanto assinatura acrescenta evidência ligada à chave; nenhuma propriedade, isoladamente, prova qualidade do código.

## Como funciona
Escolha estratégia compatível com o fornecedor, registre fingerprints e metadados necessários e confirme a origem da chave por processo independente.

## Exemplo
Para um artefato que publica assinatura verificável, confira a chave aprovada e mantenha tanto coordenada quanto policy versionadas no repositório.

```text
./gradlew --write-verification-metadata sha256,pgp help
```

## Limites e trade-offs
Chaves podem ser rotacionadas ou comprometidas; checksums copiados da mesma origem que o artefato não fornecem validação independente da origem.

## Como verificar
Altere bytes de um fixture, teste falha de checksum e assinatura e valide que uma chave não autorizada não é aceita.

## Conexões
- [[gradle-verification-metadata-bootstrap-review-manual]] — `verification-metadata.xml`: geração inicial é bootstrap, não estabelecimento automático de confiança.
- [[gradle-verification-metadata-unknown-artifact-fail-closed]] — Tratar artefato sem entrada de verificação como mudança que exige revisão.

## Fontes
- [Gradle — checksum verification](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:verification-metadata) — checksums armazenados em metadata e validação de bytes; consultado em 2026-10-04.
- [Gradle — signature verification](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:signature-verification) — assinaturas PGP, chaves e trust metadata; consultado em 2026-10-04.
