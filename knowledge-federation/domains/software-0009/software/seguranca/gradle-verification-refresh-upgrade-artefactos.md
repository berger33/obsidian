---
id: software.seguranca.tranche17.001679
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html#sec:bootstrapping-verification", "https://docs.gradle.org/current/userguide/dependency_locking.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Atualizar metadata de verificação em upgrades sem aceitar mudanças em massa

## Em uma frase
Uma mudança de versão pode exigir entradas novas de verificação, mas aceitar todos os artefatos observados numa única execução amplia confiança sem inspeção granular.

## Por que importa
Upgrades frequentes tornam tentador regenerar metadata inteira; isso pode esconder mudanças inesperadas em plugins ou transitivas junto às versões esperadas.

## Como funciona
Separe mudanças por componente, gere sugestões em ambiente reproduzível, compare hashes e mantenha uma lista explícita de itens não resolvidos.

## Exemplo
Atualize uma biblioteca em pull request dedicado, confirme versão publicada e altere somente as coordenadas relacionadas ao upgrade no XML.

```text
./gradlew --write-verification-metadata sha256 help
```

## Limites e trade-offs
Gradle não decide se alteração de checksum é legítima; a equipe precisa obter evidência da origem e considerar reprodutibilidade do artefato.

## Como verificar
Compare o diff de metadata com o diff de lock, teste build com cache vazio e investigue qualquer entrada não relacionada ao componente atualizado.

## Conexões
- [[gradle-dependency-locking-version-selection-diferenca-integridade]] — Dependency Locking e Dependency Verification no Gradle: versão fixa versus bytes verificados.
- [[gradle-verification-complemento-scanners-sbom]] — Incluir Dependency Verification em uma cadeia de controles de supply chain Gradle.

## Fontes
- [Gradle — atualizar verification metadata](https://docs.gradle.org/current/userguide/dependency_verification.html#sec:bootstrapping-verification) — regeneração controlada e revisão de metadata ao alterar dependências; consultado em 2026-10-04.
- [Gradle — Dependency Locking](https://docs.gradle.org/current/userguide/dependency_locking.html) — comparação de upgrades de versão com lock state; consultado em 2026-10-04.
