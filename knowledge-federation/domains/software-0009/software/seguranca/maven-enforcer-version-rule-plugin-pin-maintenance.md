---
id: software.seguranca.tranche17.001689
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
fontes: ["https://maven.apache.org/enforcer/enforcer-rules/requirePluginVersions.html", "https://maven.apache.org/guides/mini/guide-configuring-plugins.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Fixar a versão do Maven Enforcer Plugin e revisar mudanças de regras

## Em uma frase
Como parte do build, o plugin e a versão de suas regras devem estar declarados de forma estável para evitar mudanças silenciosas de comportamento.

## Por que importa
Um plugin não fixado pode introduzir novas regras, defaults ou compatibilidade diferente entre estações, alterando o resultado do gate.

## Como funciona
Declare versão explícita no gerenciamento de plugins, atualize por pull request e consulte documentação correspondente à versão escolhida.

## Exemplo
Uma atualização do plugin pode gerar job dedicado que compara logs e resolve warnings antes de ampliar a versão em todo o reactor.

```text
mvn help:effective-pom
```

## Limites e trade-offs
Versão fixa melhora previsibilidade, mas não valida a integridade do JAR nem impede que uma versão contenha defeito ou vulnerabilidade.

## Como verificar
Compare `mvn help:effective-pom` em máquinas limpas, confira resolução do plugin e rode a matriz de builds suportados após upgrade.

## Conexões
- [[maven-enforcer-configuracao-em-parent-versus-modulos]] — Centralizar regras Enforcer em parent POM sem perder escopo por módulo.
- [[maven-enforcer-policy-gate-nao-substitui-scanner-advisory]] — Maven Enforcer e scanners de CVE: policy de build não equivale a análise de advisories.

## Fontes
- [Maven Enforcer — Require Plugin Versions](https://maven.apache.org/enforcer/enforcer-rules/requirePluginVersions.html) — regra para exigir versões de plugins e defaults associados; consultado em 2026-10-04.
- [Apache Maven — Configuring Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html) — declaração e versionamento de plugins Maven no build; consultado em 2026-10-04.
