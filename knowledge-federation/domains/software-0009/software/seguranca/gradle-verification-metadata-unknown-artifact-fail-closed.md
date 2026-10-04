---
id: software.seguranca.tranche17.001674
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html#sec:verification-metadata", "https://docs.gradle.org/current/userguide/dependency_verification.html#sec:enabling-dependency-verification"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Tratar artefato sem entrada de verificação como mudança que exige revisão

## Em uma frase
Uma execução em modo de verificação pode falhar quando encontra artefato não declarado na metadata, evitando aceitar silenciosamente novos bytes.

## Por que importa
Novas dependências e variantes surgem ao mudar plugins, plataformas ou resolução; fazer o build parar torna a expansão de confiança visível no diff.

## Como funciona
Adicione entradas somente depois de confirmar versão, origem e checksum/assinatura; evite atualizar o arquivo de forma automática sem revisão.

## Exemplo
Um pull request que atualiza Gradle plugin pode receber falha de verificação e deve incluir a metadata necessária após revisão do artefato novo.

```text
./gradlew build
```

## Limites e trade-offs
Falha por item ausente não informa se a dependência é vulnerável; ela indica que a policy de integridade ainda não cobre aquele artefato.

## Como verificar
Introduza uma dependência controlada sem entrada, confirme a falha e valide que a entrada aprovada elimina apenas esse erro.

## Conexões
- [[gradle-checksum-versus-pgp-signature-verification]] — Checksums e assinaturas PGP no Gradle: propriedades diferentes de verificação.
- [[gradle-verification-metadata-trust-keys-export-review]] — Importar e confiar em chaves para verificação de assinaturas Gradle.

## Fontes
- [Gradle — artifacts sem metadata](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:verification-metadata) — falhas para componentes sem checksum/assinatura declarados; consultado em 2026-10-04.
- [Gradle — Dependency Verification](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:enabling-dependency-verification) — ativação do modo de verificação e efeito sobre a resolução; consultado em 2026-10-04.
