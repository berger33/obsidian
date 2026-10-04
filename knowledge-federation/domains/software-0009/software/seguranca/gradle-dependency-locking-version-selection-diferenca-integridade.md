---
id: software.seguranca.tranche17.001678
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_locking.html", "https://docs.gradle.org/current/userguide/dependency_verification.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dependency Locking e Dependency Verification no Gradle: versão fixa versus bytes verificados

## Em uma frase
Dependency Locking registra versões selecionadas para preservar resolução, enquanto Dependency Verification confere integridade dos artefatos obtidos.

## Por que importa
Um lockfile pode fixar coordenada e versão sem impedir que o conteúdo servido para essa coordenada mude; são camadas complementares.

## Como funciona
Ative locking para reprodutibilidade de seleção e mantenha verification metadata para confiança em bytes e assinaturas, revisando ambos no mesmo fluxo de upgrade.

## Exemplo
Atualizar uma dependência deve mostrar versão nova no lock e checksums correspondentes na metadata, ambos associados ao commit e à CI.

```text
./gradlew dependencies
```

## Limites e trade-offs
Nenhum dos mecanismos detecta por si só vulnerabilidades conhecidas nem garante que uma versão fixa tenha sido revisada manualmente.

## Como verificar
Inspecione lock state e XML separadamente, altere um artefato mantendo coordenada fixa e confirme que verificação detecta diferença.

## Conexões
- [[gradle-verification-metadata-plugins-build-dependencies]] — Cobertura do Gradle Dependency Verification para plugins e configurações resolvidas.
- [[gradle-verification-refresh-upgrade-artefactos]] — Atualizar metadata de verificação em upgrades sem aceitar mudanças em massa.

## Fontes
- [Gradle — Dependency Locking](https://docs.gradle.org/current/userguide/dependency_locking.html) — fixação das versões selecionadas no grafo de dependências; consultado em 2026-10-04.
- [Gradle — Dependency Verification](https://docs.gradle.org/current/userguide/dependency_verification.html) — checagem separada de integridade de checksums/assinaturas; consultado em 2026-10-04.
