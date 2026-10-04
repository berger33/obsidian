---
id: software.seguranca.tranche17.001671
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html", "https://dependency-check.github.io/DependencyCheck/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gradle Dependency Verification: verificar integridade de artefatos, não ausência de vulnerabilidades

## Em uma frase
Dependency Verification compara artefatos baixados com checksums e/ou assinaturas aceitos, protegendo contra conteúdo diferente do esperado durante resolução.

## Por que importa
Um pacote íntegro ainda pode conter falha conhecida ou código malicioso publicado legitimamente; integridade e avaliação de segurança são controles diferentes.

## Como funciona
Ative verificação no build, mantenha metadata revisável e combine-a com scanner de advisories, revisão de dependências e proveniência de release.

## Exemplo
Um pipeline pode falhar se um JAR mudar em relação ao checksum versionado e ainda executar scanner separado para advisories do mesmo grafo.

```text
./gradlew build
```

## Limites e trade-offs
A verificação não avalia semântica, vulnerabilidades ou intenção do código assinado; confiança na metadata inicial é parte do modelo de segurança.

## Como verificar
Edite um artefato de teste após registrar sua soma e confirme que Gradle recusa o conteúdo alterado; rode ferramenta de advisory separadamente.

## Conexões
- [[gradle-verification-metadata-bootstrap-review-manual]] — `verification-metadata.xml`: geração inicial é bootstrap, não estabelecimento automático de confiança.

## Fontes
- [Gradle — Dependency Verification](https://docs.gradle.org/current/userguide/dependency_verification.html) — checksums/assinaturas e limites da verificação de integridade dos artefatos; consultado em 2026-10-04.
- [OWASP Dependency-Check — Maven/Gradle SCA](https://dependency-check.github.io/DependencyCheck/) — scanner de advisories como controle separado de integridade de artefatos; consultado em 2026-10-04.
