---
id: software.seguranca.tranche17.001684
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
fontes: ["https://maven.apache.org/enforcer/enforcer-rules/banDynamicVersions.html", "https://maven.apache.org/enforcer/maven-enforcer-plugin/usage.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Banir versões Maven dinâmicas para builds reprodutíveis

## Em uma frase
A regra ban dynamic versions pode rejeitar ranges e seletores mutáveis que deixam a mesma configuração resolver versões diferentes ao longo do tempo.

## Por que importa
Resolução flutuante enfraquece auditoria e reproduzibilidade, pois o artefato construído pode variar sem mudança do POM versionado.

## Como funciona
Prefira versões explícitas ou mecanismo controlado de lock e revise atualizações como diffs; trate snapshots e ranges conforme política do repositório.

## Exemplo
Habilite a regra no parent POM e use atualização automatizada revisada em pull requests para manter versões sem ranges silenciosos.

```text
mvn enforcer:enforce
```

## Limites e trade-offs
Fixar versão não garante que artefato seja íntegro ou sem vulnerabilidades; snapshots podem ter políticas de uso distintas por ambiente.

## Como verificar
Inspecione o effective POM, inclua uma versão dinâmica de teste e confirme que o Enforcer identifica a configuração.

## Conexões
- [[maven-enforcer-dependency-convergence-transitive-conflicts]] — `dependencyConvergence`: detectar versões transitivas divergentes no grafo Maven.
- [[maven-enforcer-banned-dependencies-exclusions]] — `bannedDependencies`: recusar coordenadas Maven com escopo e exceções explícitos.

## Fontes
- [Maven Enforcer — Ban Dynamic Versions](https://maven.apache.org/enforcer/enforcer-rules/banDynamicVersions.html) — rejeição de ranges e seletores Maven dinâmicos; consultado em 2026-10-04.
- [Maven Enforcer — Usage](https://maven.apache.org/enforcer/maven-enforcer-plugin/usage.html) — ativação de regras no POM e execução no lifecycle; consultado em 2026-10-04.
