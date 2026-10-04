---
id: software.seguranca.tranche17.001680
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
fontes: ["https://docs.gradle.org/current/userguide/dependency_verification.html", "https://dependency-check.github.io/DependencyCheck/dependency-check-gradle/index.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Incluir Dependency Verification em uma cadeia de controles de supply chain Gradle

## Em uma frase
A verificação de artefatos protege uma propriedade de integridade e deve ser combinada com controles de versão, advisories, SBOM e revisão de mudanças.

## Por que importa
Um pacote pode ter assinatura válida e ainda conter vulnerabilidade; um alerta de CVE também não prova que o arquivo baixado corresponde ao esperado.

## Como funciona
Associe metadata, lock state, scanner de advisories, provenance de build e evidência de release a um mesmo commit e conjunto de dependências.

## Exemplo
Um pipeline pode falhar em checksum inesperado, publicar SBOM e executar scanner de CVEs antes de assinar o artefato produzido.

## Limites e trade-offs
Combinar ferramentas não garante cobertura completa; cada fonte, base e etapa precisa de versão, escopo e política próprios.

## Como verificar
Teste cada controle com uma fixture apropriada e confirme que relatório e falha podem ser correlacionados ao artefato implantado.

## Conexões
- [[gradle-verification-refresh-upgrade-artefactos]] — Atualizar metadata de verificação em upgrades sem aceitar mudanças em massa.

## Fontes
- [Gradle — Dependency Verification](https://docs.gradle.org/current/userguide/dependency_verification.html) — escopo de integridade e limites do material de confiança; consultado em 2026-10-04.
- [OWASP Dependency-Check — Gradle](https://dependency-check.github.io/DependencyCheck/dependency-check-gradle/index.html) — análise separada de dependências contra fontes de vulnerabilidade; consultado em 2026-10-04.
