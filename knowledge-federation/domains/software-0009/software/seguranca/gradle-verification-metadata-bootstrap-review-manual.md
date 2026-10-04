---
id: software.seguranca.tranche17.001672
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html#sec:bootstrapping-verification", "https://docs.gradle.org/current/userguide/command_line_interface.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `verification-metadata.xml`: geração inicial é bootstrap, não estabelecimento automático de confiança

## Em uma frase
Gradle pode gerar verification metadata durante uma execução, mas os valores coletados refletem o que foi resolvido naquele ambiente e precisam de revisão.

## Por que importa
Aceitar cegamente hashes obtidos de um download inesperado pode fixar bytes comprometidos como referência confiável.

## Como funciona
Gere metadata em ambiente controlado, confirme origem e versões esperadas e revise checksums ou chaves antes de ativar enforcement em CI.

## Exemplo
Após executar `./gradlew --write-verification-metadata sha256 help`, inspecione cada coordenada adicionada e compare com uma fonte independente aprovada.

```text
./gradlew --write-verification-metadata sha256 help
```

## Limites e trade-offs
Um hash prova igualdade com bytes conhecidos, não que a fonte inicial era autêntica; bootstrap online não deve ser confundido com revisão de fornecedor.

## Como verificar
Revise diff completo de `gradle/verification-metadata.xml`, compare coordenadas com lockfile e repita a resolução em máquina limpa.

## Conexões
- [[gradle-dependency-verification-integridade-nao-vulnerabilidade]] — Gradle Dependency Verification: verificar integridade de artefatos, não ausência de vulnerabilidades.
- [[gradle-checksum-versus-pgp-signature-verification]] — Checksums e assinaturas PGP no Gradle: propriedades diferentes de verificação.

## Fontes
- [Gradle — bootstrap de verification metadata](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:bootstrapping-verification) — geração inicial com `--write-verification-metadata` e revisão do resultado; consultado em 2026-10-04.
- [Gradle — Command-Line Interface](https://docs.gradle.org/current/userguide/command_line_interface.html) — uso de flags globais do wrapper durante a geração de metadata; consultado em 2026-10-04.
